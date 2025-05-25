import pandas as pd
import json
import ast
from collections import Counter


def parse_expert_response(text):
    """
    Parses a stringified list of dicts from Excel cells.
    Handles both JSON and Python-style formatting.
    """
    if pd.isna(text):
        return []
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        try:
            return ast.literal_eval(text)
        except Exception as e:
            print(f"Warning: failed to parse: {text}\nError: {e}")
            return []


def extract_labels_per_type(expert_responses, label_type):
    """
    Extracts symptoms or sections from structured expert annotations.

    Args:
        expert_responses (list of str): JSON-like strings
        label_type (str): 'symptom' or 'section'

    Returns:
        list of list of str: per-expert list of labels
    """
    all_labels = []
    for expert_text in expert_responses:
        parsed = parse_expert_response(expert_text)
        labels = [
            item[label_type].strip().lower() for item in parsed if label_type in item
        ]
        all_labels.append(labels)
    return all_labels


def compute_overlap_agreement(annotations, min_agree=3):
    """
    Returns True if any label appears in >= min_agree different expert lists.
    """
    flat = [label for sublist in annotations for label in sublist]
    counter = Counter(flat)
    if not counter:
        return False, "", 0.0
    most_common, count = counter.most_common(1)[0]
    agreement_rate = count / len(annotations)
    return count >= min_agree, most_common, agreement_rate


def get_most_common_annotation(expert_responses):
    """
    Returns the most common full structured annotation across experts as JSON string.
    """
    normalized = [
        json.dumps(parse_expert_response(resp), sort_keys=True)
        for resp in expert_responses
    ]
    most_common_json, _ = Counter(normalized).most_common(1)[0]
    return most_common_json


if __name__ == "__main__":
    input_file = "expert_annotations.xlsx"
    output_file = "validated_ground_truth.xlsx"

    df = pd.read_excel(input_file)
    validated_rows = []

    for idx, row in df.iterrows():
        vignette_id = row["Vignette ID"]
        expert_responses = [row[f"Expert {i}"] for i in range(1, 6)]

        print(f"\n--- Vignette ID: {vignette_id} ---")
        for i, resp in enumerate(expert_responses, start=1):
            print(f"Expert {i} raw: {resp}")
            print(f"Expert {i} parsed: {parse_expert_response(resp)}")

        # Extract symptoms and sections
        symptom_lists = extract_labels_per_type(expert_responses, "symptom")
        section_lists = extract_labels_per_type(expert_responses, "section")

        print("Parsed symptoms per expert:", symptom_lists)
        print("Parsed sections per expert:", section_lists)

        # Validate overlap
        symptom_valid, top_symptom, symptom_agreement = compute_overlap_agreement(
            symptom_lists
        )
        section_valid, top_section, section_agreement = compute_overlap_agreement(
            section_lists
        )

        print(
            f"Symptom agreement: {symptom_agreement:.2f}, top: {top_symptom}, valid: {symptom_valid}"
        )
        print(
            f"Section agreement: {section_agreement:.2f}, top: {top_section}, valid: {section_valid}"
        )

        # Determine ground truth
        if symptom_valid and section_valid:
            ground_truth = get_most_common_annotation(expert_responses)
        else:
            ground_truth = "CONSENSUS_NEEDED"

        validated_rows.append(
            {
                "Vignette ID": vignette_id,
                "Ground Truth": ground_truth,
                "Symptom Agreement Rate": round(symptom_agreement, 2),
                "Section Agreement Rate": round(section_agreement, 2),
                "Top Symptom": top_symptom,
                "Top Section": top_section,
            }
        )

    pd.DataFrame(validated_rows).to_excel(output_file, index=False)
    print(f"\n✅ Validation complete. Output saved to {output_file}")
