import pandas as pd
import re

def calculate_metrics(filename):
    # Loading the Excel file
    data = pd.read_excel(filename)
    print(data.columns)
    
    # Removing rows where 'Estimated symptom' is 'Error'
    data_filtered = data[data['Estimated Symptom'] != 'Error']
    
 
    for index, row in data_filtered.iterrows():
        
        if pd.isna(row["Symptom"]):
            data_filtered.at[index, "Symptom"] = [None]
        else:
            data_filtered.at[index, "Symptom"] = [re.sub(r"[^a-zA-Z0-9]", "", item).lower()
                                                            for item in row["Symptom"].split(",")
                                                            if item.strip()]
        if pd.isna(row["Estimated Symptom"]):
            data_filtered.at[index, "Estimated Symptom"] = [None]
        else:
            data_filtered.at[index, "Estimated Symptom"] = [re.sub(r"[^a-zA-Z0-9]", "", item).lower()
                                                            for item in row["Estimated Symptom"].split(",")
                                                            if item.strip()]

    data_long = pd.DataFrame(columns=["StatementNr", "Symptom", "Estimated Symptom", "Correct"])

    for index, row in data_filtered.iterrows():
        # Iterate over the lists in "Symptom" and "Estimated Symptom"
        print("ID: ", index)
        symptoms = set(row["Symptom"])
        print(symptoms)
        estimated_symptoms = set(row["Estimated Symptom"])
        print(estimated_symptoms)
        hits = pd.DataFrame({
                "StatementNr": [index] * len(list(symptoms & estimated_symptoms)),
                "Symptom": list(symptoms & estimated_symptoms),
                "Estimated Symptom": list(symptoms & estimated_symptoms),
                "Correct": [True] * len(list(symptoms & estimated_symptoms))
                })
        if symptoms != {None}:
            print("test")
            misses = pd.DataFrame({
                    "StatementNr": [index] * len(list(symptoms - estimated_symptoms)),
                    "Symptom": list(symptoms - estimated_symptoms),
                    "Estimated Symptom": [None] * len(list(symptoms - estimated_symptoms)),
                    "Correct": [False] * len(list(symptoms - estimated_symptoms))
                    })
        if estimated_symptoms != {None}:
            false_pos = pd.DataFrame({
                    "StatementNr": [index] * len(list(estimated_symptoms - symptoms)),
                    "Symptom": [None] * len(list(estimated_symptoms - symptoms)),
                    "Estimated Symptom": list(estimated_symptoms - symptoms),
                    "Correct": [False] * len(list(estimated_symptoms - symptoms))
                    })
        
        data_long = pd.concat([data_long, hits, misses, false_pos], ignore_index=True)
        
    # Calculating accuracy
    section_correct_all_true = data_long.groupby("StatementNr")["Correct"].all()
    accuracy = (section_correct_all_true.sum() / len(section_correct_all_true))
    
    print(f"Accuracy over all sections: {accuracy}")

    # Calculating Precision
    if(None != data_long['Estimated Symptom'].values.any()):
        precision_rows = data_long[(data_long['Symptom'].notna()) & (data_long['Estimated Symptom'].notna())]
        precision = len(precision_rows) / len(data_long[data_long['Estimated Symptom'].notna()])
    else:
        precision = None
    
    print(f"Precision over all symptoms: {precision}")

    # Calculating Sensitivity/Recall
    if(None != data_long['Symptom'].values.any()):
        sensitivity_rows = data_long[(data_long['Symptom'].notna()) & (data_long['Estimated Symptom'].notna())]
        sensitivity = len(sensitivity_rows) / len(data_long[data_long['Symptom'].notna()])
    else:
        sensitivity = None
    
    print(f"Sensitivity/Recall over all symptoms: {sensitivity}")

    # Calculating Specificity
    if(None in data_long['Symptom'].values):
        specificity_rows = data_long[(data_long['Symptom'].isna()) & (data_long['Estimated Symptom'].isna())]
        specificity = len(specificity_rows) / len(data_long[data_long['Symptom'].isna()])
    else:
        specificity = None

    print(f"Specificity over all symptoms: {specificity}")

    # Calculating F1 score
    if(precision and sensitivity):
        f1 = 2*(precision * sensitivity) /(precision + sensitivity)
    else:
        f1 = None
    print(f"F1 score: {f1}")


    result = pd.DataFrame({"Accuracy":[accuracy], "Sensitivity/Recall":[sensitivity], "Specificity":[specificity], "F1":[f1]})
    result.to_csv(f'{filename}_metrics.csv', index=False)  
    
d = pd.read_excel("TP1results.xlsx")
    
dNew = calculate_metrics("TP1results.xlsx")

