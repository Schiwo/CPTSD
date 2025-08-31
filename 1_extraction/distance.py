# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:38:07 2025

@author: schiltem93
"""
import pandas as pd
import numpy as np
import re
from transformers import AutoTokenizer


def calculate_distances(filename):
    # Helper functions
    def get_token_indices(section, original_text, offsets):
        start_idx = original_text.find(section)
        if start_idx == -1:
            raise "Error: Section not found in original statement."
        end_idx = start_idx + len(section)

        token_indices = [
            i
            for i, (start, end) in enumerate(offsets)
            if start >= start_idx and end <= end_idx
        ]
        return token_indices

    def central_token_index(token_indices):
        return token_indices[len(token_indices) // 2]  # Midpoint

    tokenizer = AutoTokenizer.from_pretrained("bert-base-german-cased")
    # Loading the Excel file
    data = pd.read_excel(filename)

    # Removing rows where 'Estimated symptom' is 'Error'
    data_filtered = data[data["Estimated Symptom"] != "Error"]

    for index, row in data_filtered.iterrows():
        if pd.isna(row["Section"]):
            data_filtered.at[index, "Section"] = [None]
        else:
            data_filtered.at[index, "Section"] = [
                re.sub(r'["\']', "", item.strip()) for item in row["Section"].split("/")
            ]
        if pd.isna(row["Estimated Section"]):
            print("Test")
            data_filtered.at[index, "Estimated Section"] = [None]
        else:
            data_filtered.at[index, "Estimated Section"] = [
                re.sub(r'["\']', "", item.strip())
                for item in row["Estimated Section"].split("/")
            ]

    data_long = pd.DataFrame(
        columns=[
            "StatementNr",
            "Statement",
            "Section",
            "Estimated Section",
            "d",
            "overlap",
        ]
    )
    for index, row in data_filtered.iterrows():

        # Iterate over the lists in "Section" and "Estimated Section"
        statement = row["Statement"]
        tokenized = tokenizer(
            statement, return_offsets_mapping=True, add_special_tokens=False
        )
        tokens = tokenized.tokens()  # List of token strings
        offsets = tokenized["offset_mapping"]  # Character offsets for each token

        estimated_sections = row["Estimated Section"]
        if not None in estimated_sections:
            estimated_indices = [
                get_token_indices(section, statement, offsets)
                for section in estimated_sections
            ]
        else:
            estimated_indices = None

        for ground_truth in row["Section"]:
            if ground_truth is None:
                if estimated_indices is None:
                    continue
                else:
                    data_long = pd.concat(
                        [
                            data_long,
                            pd.DataFrame(
                                {
                                    "StatementNr": [index] * len(estimated_sections),
                                    "Statement": [statement] * len(estimated_sections),
                                    "Section": [None] * len(estimated_sections),
                                    "Estimated Section": estimated_sections,
                                    "d": [np.inf] * len(estimated_sections),
                                    "overlap": [None] * len(estimated_sections),
                                }
                            ),
                        ],
                        ignore_index=True,
                    )
                    continue
            if estimated_indices is None:
                data_long = pd.concat(
                    [
                        data_long,
                        pd.DataFrame(
                            {
                                "StatementNr": [index],
                                "Statement": [statement],
                                "Section": [ground_truth],
                                "Estimated Section": [None],
                                "d": [np.inf],
                                "overlap": [None],
                            }
                        ),
                    ],
                    ignore_index=True,
                )
                continue
            # Find token indices for the ground truth and estimated sections
            ground_truth_indices = get_token_indices(ground_truth, statement, offsets)
            # Get the central token index for the ground truth
            ground_truth_central = central_token_index(ground_truth_indices)

            # Calculate the mid-token distance to each estimated section
            distances = []
            for estimated in estimated_indices:
                if estimated:  # Ensure the section exists in the tokenized sequence
                    # print(estimated)
                    estimated_central = central_token_index(estimated)
                    distance = abs(ground_truth_central - estimated_central)
                    distances.append(distance)
                else:
                    distances.append(None)  # Section not found
            minId = np.argmin(distances)
            minDistance = distances[minId]
            minDistanceSection = estimated_sections[minId]

            # Calculate overlap with of the ground truth with the sum of all estimated sections.
            sum_of_estimated_tokens = {
                token for section in estimated_indices for token in section
            }
            overlap = len(set(ground_truth_indices) & sum_of_estimated_tokens) / len(
                set(ground_truth_indices)
            )

            # Display results
            print("Tokens:", tokens)
            print(f"Complete statement: '{statement}'")
            print(f"Ground truth central token index: {ground_truth_central}")
            print(f"of the ground truth section: '{ground_truth}'")
            print(f"Minimum Mid-token distance is: {minDistance}")
            print(f"to the estimated section: '{minDistanceSection}'")
            print(
                f"The overlap of the ground truth with all estimated sections is: {overlap}"
            )

            data_long = pd.concat(
                [
                    data_long,
                    pd.DataFrame(
                        {
                            "StatementNr": [index],
                            "Statement": [statement],
                            "Section": [ground_truth],
                            "Estimated Section": [minDistanceSection],
                            "d": [minDistance],
                            "overlap": [overlap],
                        }
                    ),
                ],
                ignore_index=True,
            )

    return data_long

    # result.to_csv(f'{filename}_distances.csv', index=False)


d = pd.read_excel("TP1results.xlsx")

dNew = calculate_distances("TP1results.xlsx")
