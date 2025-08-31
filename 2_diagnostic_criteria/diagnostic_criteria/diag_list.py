# Diagnostic (task 2)

from openai import OpenAI, BadRequestError
import pandas as pd
import argparse
import copy
import ast
from prompts_diag_list import diag_list_de  # or any choosen prompt


# Exacting symptoms only (not giving sections to the LLM because of context length limit, plus we give them whole interview already)
def extract_symptoms_only(estimation_column):
    symptoms = []

    for item in estimation_column:
        # Handle stringified list of dicts
        if isinstance(item, str):
            try:
                item_list = ast.literal_eval(item)
            except (SyntaxError, ValueError):
                item_list = []
        elif isinstance(item, list):
            item_list = item
        else:
            item_list = []

        for entry in item_list:
            if isinstance(entry, dict) and "symptom" in entry:
                symptoms.append(entry["symptom"])

    return list(set(symptoms))  # Remove duplicates


def generate_diagnosis_from_statements_and_symptoms(df, api_key, output_filename):
    client = OpenAI(api_key=api_key)

    print("Step 1: Checking required columns")
    if not {"Statement", "Estimation"}.issubset(df.columns):
        print("Missing columns: 'Statement' and/or 'Estimation'")
        return

    print("Step 2: Combining interview statements")
    combined_statements = "\n\n".join(df["Statement"].astype(str))

    print("Step 3: Extracting symptoms")
    symptom_list = extract_symptoms_only(df["Estimation"])
    combined_symptoms = "\n".join(symptom_list)
    print(f"Found {len(symptom_list)} unique symptoms.")

    model = "gpt-4"
    messages = [
        diag_list_de[0],
        {
            "role": "user",
            "content": f"{diag_list_de[1]['content']}\n\nInterview:\n{combined_statements}\n\nDetected Symptoms:\n{combined_symptoms}",
        },
    ]

    try:
        print("Step 4: Sending request to OpenAI")
        model = "gpt-4"
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=250,  # less than 150 words,
            timeout=90,
        )

        result = response.choices[0].message.content.strip()

        print(f"Step 5: Saving output to {output_filename}.txt")
        with open(f"{output_filename}.txt", "w", encoding="utf-8") as output_file:
            output_file.write(result)

        print("Diagnostic criteria generated successfully.")

    except BadRequestError as e:
        print(f"OpenAI request failed: {e}")
        with open(f"{output_filename}.txt", "w", encoding="utf-8") as output_file:
            output_file.write(f"Error: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate diagnostic criteria suggestions from LLM"
    )
    parser.add_argument(
        "--data",
        help="Input Excel file with Statement and Estimation column",
        required=True,
    )
    parser.add_argument("--apikey", help="Your OpenAI API key", required=True)
    parser.add_argument(
        "--result", help="Output filename (without extension)", required=True
    )

    args = parser.parse_args()
    data_filename = args.data
    api_key = args.apikey
    result_filename = args.result

    # Load data
    data = pd.read_excel(f"{data_filename}.xlsx")

    # Run the diagnostic generation
    generate_diagnosis_from_statements_and_symptoms(data, api_key, result_filename)
