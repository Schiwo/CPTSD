import pandas as pd
import argparse
from openai import OpenAI

parser = argparse.ArgumentParser(
    description="Summarize interview with symptoms and criteria"
)
parser.add_argument(
    "--symptoms_excel", help="Excel file with 'Estimation' column", required=True
)
parser.add_argument(
    "--criteria_txt", help="Text file with diagnostic criteria", required=True
)
parser.add_argument("--apikey", help="Your OpenAI API key", required=True)
parser.add_argument("--output", help="Output summary file name (txt)", required=True)
args = parser.parse_args()


# Load symptoms & sections from Excel
def load_symptoms_from_excel(file_path):
    df = pd.read_excel(file_path)
    if "Estimation" not in df.columns:
        raise ValueError("Excel must contain 'Estimation' column")
    symptoms = df["Estimation"].dropna().unique().tolist()
    print(f"Loaded {len(symptoms)} entries from 'Estimation' column.")
    return "\n".join(symptoms)


# Load diagnostic criteria from txt
def load_criteria_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
    print(f"Diagnostic criteria file loaded.")
    return text


# Summary
def generate_summary(symptoms_text, criteria_text, api_key):
    print("Sending data to GPT model for summarization")
    client = OpenAI(api_key=api_key)

    prompt = (
        "Du bist ein erfahrener Psychiater. Fasse bitte den Fall des Patienten in maximal 250 Wörtern zusammen, sodass die Zusammenfassung direkt als Übergabe an den behandelnden Psychiater genutzt werden kann.\
        Verwende hierfür die  Symptome, Abschnitte und erfüllten Diagnosekriterien aus dem Input.\
        Deine Aufgabe ist es:\
        1. wichtige biografische Elemente zusammenzufassen\
        2. relevante Symptome und Diagnosekriterien darzustellen\
        2. eine oder mehrere Verdachtsdiagnosen (mit F-Code) zu nennen\
        3. die Komplexität des Falls zwischen 1 (einfach) und 3 (komplex) zu bewerten und kurz begründen.\
        4. die Sicherheit deiner Diagnoseeinschätzung in Prozent angeben (max 100) und kurz begründen.\
        Halte dich an dieses Format:\
        Biografische Zusammenfassung: <Text>\
        Symptome und Diagnosekriterien: <Text>\
        Verdachtsdiagnose: <F-Code>, <Begründung>\
        Komplexität: <1-3>, <Begründung>\
        Sicherheit: <0-100 Prozent>, <Begründung>\
        Bitte sei prägnant, klinisch und begründe deine Überlegungen. Wenn die Beweise unzureichend sind, gib dies an.\
        Wenn du subjektive biografische Elemente weitergibst, nutze den Konjunktiv oder Zitate, und interpretiere nicht.\n\n"
        f"Symptoms & Sections:\n{symptoms_text}\n\nDiagnostic Criteria:\n{criteria_text}"
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message.content


# Save summary as file
def save_summary(content, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Summary saved to {filename}")


if __name__ == "__main__":
    symptoms_text = load_symptoms_from_excel(args.symptoms_excel)
    criteria_text = load_criteria_from_txt(args.criteria_txt)

    summary = generate_summary(symptoms_text, criteria_text, args.apikey)
    save_summary(summary, args.output)

    print(f"Summary saved to {args.output}")
