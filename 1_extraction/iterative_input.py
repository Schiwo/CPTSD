# In this module, we try a new approach, giving as input only one question-answer bundle, as well as context information (summary of the interview, previous output).

import argparse, json
from copy import deepcopy
import pandas as pd
from tqdm import tqdm
from openai import OpenAI, BadRequestError
from prompts.prompts_zeroshot import zeroshot_de_1
from pathlib import Path

DEFAULT_MODEL = "gpt-4o-mini"
DEFAULT_TEMPERATURE = 0.0
MAX_TOKENS = 450  # ~250 words
TIMEOUT_SECS = 90


def build_messages(base_msgs, summary: str, prev_output: list, next_line: str):
    ctx = (
        f"Interview summary (fixed each turn):\n{summary or ''}\n\n"
        f"Previously extracted items (from the last line):\n{json.dumps(prev_output, ensure_ascii=False)}\n\n"
        f"This is the next line in the interview (question + answer):\n{next_line}"
    )
    msgs = deepcopy(base_msgs)  # don't mutate zeroshot_de_1
    msgs[-1]["content"] += "\n\n" + ctx
    return msgs


def parse_json_list(txt: str):
    # Try strict load first
    try:
        data = json.loads(txt)
        return data if isinstance(data, list) else None
    except Exception:
        pass
    # Heuristic: grab the outermost list
    s, e = txt.find("["), txt.rfind("]")
    if s != -1 and e != -1 and e > s:
        try:
            data = json.loads(txt[s : e + 1].replace("'", '"'))
            return data if isinstance(data, list) else None
        except Exception:
            try:
                data = json.loads(txt[s : e + 1])
                return data if isinstance(data, list) else None
            except Exception:
                return None
    return None


def run(df, api_key, out_name, summary, model, temperature):
    client = OpenAI(api_key=api_key)
    for col in ("Estimation", "Error"):
        if col not in df.columns:
            df[col] = ""

    summary_content = Path(summary).read_text()

    prev_output = []  # empty for the very first line

    for i, row in tqdm(df.iterrows(), total=len(df)):
        try:
            line = row["Statement"].strip()
            msgs = build_messages(zeroshot_de_1, summary_content, prev_output, line)

            # IMPORTANT: do NOT force response_format=json_object since we expect a LIST
            resp = client.chat.completions.create(
                model=model,
                messages=msgs,
                max_tokens=450,  # limit of approx 250 words
                temperature=temperature,
                timeout=90,
            )
            content = resp.choices[0].message.content
            parsed = parse_json_list(content)

            if parsed is None:
                df.at[i, "Estimation"] = content
                df.at[i, "Error"] = "JSON list parse failed"
                # keep prev_output unchanged if parse failed
                continue

            # Save and carry forward
            df.at[i, "Estimation"] = json.dumps(parsed, ensure_ascii=False)
            df.at[i, "Error"] = ""
            prev_output = parsed

        except BadRequestError as e:
            df.at[i, "Estimation"] = "Error"
            df.at[i, "Error"] = f"BadRequestError: {e}"
            # keep prev_output as-is
        except Exception as e:
            df.at[i, "Estimation"] = "Error"
            df.at[i, "Error"] = f"Exception: {e}"
            # keep prev_output as-is

    df.to_excel(f"{out_name}.xlsx", index=False)


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Iterative per-line inference: summary + previous output + next line."
    )
    p.add_argument(
        "--data",
        required=True,
        help="Excel without extension (e.g., 'input' for 'input.xlsx')",
    )
    p.add_argument("--apikey", required=True)
    p.add_argument("--result", required=True, help="Output Excel without extension")
    p.add_argument(
        "--summary", default="", help="Txt file containing the interview summary"
    )
    p.add_argument("--model", default=DEFAULT_MODEL)
    p.add_argument("--temperature", type=float, default=0.0)
    a = p.parse_args()

    df = pd.read_excel(f"{a.data}.xlsx")
    run(df, a.apikey, a.result, a.summary, a.model, a.temperature)
