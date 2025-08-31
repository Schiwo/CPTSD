# The following file contains chain-of-thought prompts for finding bipolarity and depression symptoms.

# Short is the adapted version from this repository, translated from corean to english and german.
# We use the same sentences as in zero-shot prompting in order to reduce bias and be able to compare both methods. Only sentences related to chain-of-thought (step-by-step) have been added.
# As in zero-shot version:
# Symptoms have been changed to Major depression episode and Bipolar disorder.
# Sentences are simpler and more direct.

# There is no original prompt for chain-of-thoughts in the paper.

cot_short_en_1 = (
    {
        "role": "system",
        "content": "You are given part of an interview transcript between a psychiatrist and a patient, and as context the interview's summary as well as the last output for the interview part before.\
        Identify psychiatrically significant symptoms (DSM-5) for Major Depression Episode and Bipolar Disorder, and quote the exact wording (verbatim spans) that supports each symptom.\
        Start by carefully reading the transcript part and the context. Identify any parts of the conversation that directly suggest one or more of the listed symptoms. Focus only on the symptoms explicitly named below.\
        For each potential symptom, consider whether it matches any of the DSM-5 criteria listed below. Only include it if the patient's wording clearly supports one of the listed symptoms.\
        Then, extract the relevant section of the transcript and link it directly to the symptom it suggests. If a section contains multiple symptoms, list them together in one object.\
        Finally, return your answer as valid JSON list of objects: [{'symptom': '<label>', 'section': '<exact transcript quote>'}, {'symptom': '<label>', 'section': '<exact transcript quote>'}, ...].\
        If a section contains multiple syptoms, answer in the format: [{'symptom': '..., ...', 'section': '...'}, ...].\
        If there are no psychiatrically significant symptoms, respond with: [{'symptom': 'none', 'section': 'none'}].\
        Use only following symptom labels:\
        Major depression episode: Depressed mood, Loss of interest or pleasure, Decrease or increase in appetite, Weight loss or gain, Insomnia or hypersomnia, Psychomotor agitation or retardation, Fatigue or loss of energy, Worthlesness or excessive guilt, Difficulty concentrating or indecisiveness, Suicidality.\
        Manic and hypomanic episode: Expansive or elevated or irritable mood, Increased self-esteem or grandiosity, Decreased need for sleep, Increased talkativeness or pressured speech, Flight of ideas or racing thoughts, Distractibility, Increased goal-directed activity or psychomotor agitation, Risky behaviour.\
        For sections, quote verbatim spans (no summary). Use only minimum number of words necessary to document the symptom (no complete sentences unless necessary).\
        If a section supports multiple syptoms, list them together: [{'symptom': '..., ...', 'section': '...'}, ...].\
        Ignore negated symptoms unless contradicted elsewhere, and focus on information given by the patient.\
        If there are no psychiatrically significant symptoms, return: [{'symptom': 'none', 'section': 'none'}].\
        Your output should be maximum 250 words.",
    },
    {
        "role": "user",
        "content": "Here is a transcript part and context information. Extract the symptoms and supporting sections as specified. Think step by step before providing the final list.",
    },
)

cot_short_de_1 = (
    {
        "role": "system",
        "content": "Du erhältst ein Teil des Interviewtranskripts, und als Kontext die Zusammenfassung des Interviews und die vorherige Ausgabe.\
        Identifiziere psychiatrisch relevante Symptome für Major Depression Episode und Bipolare Störungen (DSM-5), und zitiere die jeweiligen Abschnitte (Wortlaute), die jedes Symptom belegen.\
        Beginne damit, das Interview und den Kontext sorgfältig zu lesen. Identifiziere alle Teile des Gesprächs, die direkt auf eines oder mehrere der aufgeführten Symptome hindeuten. Konzentriere dich nur auf die unten genannten Symptome.\
        Überlege bei jedem Symptom, ob es einem der unten aufgeführten DSM-5-Kriterien entspricht. Nimm es nur auf, wenn die Formulierungen des Patienten eindeutig auf eines der aufgelisteten Symptome hindeuten.\
        Extrahiere dann den entsprechenden Abschnitt des Transkripts und verknüpfe ihn mit dem Symptom, auf das er hindeutet. Wenn ein Abschnitt mehrere Symptome enthält, liste sie zusammen in einem Objekt auf.\
        Schließlich, gib ein gültiges JSON als Liste von Objekten zurück: [{'symptom': '<label>', 'section': '<exact transcript quote>'}, {'symptom': '<label>', 'section': '<exact transcript quote>'}, ...].\
        Verwende ausschließlich folgende Symptome:\
        Schwere depressive Episode: Depressive Stimmung, Interessen- oder Freudeverlust, Verminderter oder gesteigerter Appetit, Gewichtsverlust oder -zunahme, Insomnie oder Hypersomnie, Psychomotorische Unruhe oder Verlangsamung, Müdigkeit oder Energieverlust, Schuld- oder Wertlosigkeitsgefühle, Konzentrations- oder Entscheidungsschwierigkeiten, Suizidalität.\
        Manische und hypomanische Episode: Gereizte oder gehobene oder expansive Stimmung, Gesteigertes Selbstwertgefühl oder Größenideen, Vermindertes Schlafbedürfnis, Gesteigertes Sprechbedürfnis oder Rededruck, Ideenflucht oder Gedankenrasen, Ablenkbarkeit, Gesteigerte zielgerichtete Aktivität oder psychomotorische Unruhe, Risikoverhalten.\
        Gebe die Abschnitte wörtlich aus dem Transkript wieder (keine Zusammenfassung). Gib nur die minimal nötigen Wörter zur Belegung des Symptoms (keine ganzen Sätze, wenn nicht nötig).\
        Wenn ein Abschnitt mehrere Symptome enthält, liste sie zusammen auf: [{'symptom': '..., ...', 'section': '...'}, ...].\
        Ignoriere negierte Symptome, sofern sie nicht an anderer Stelle widerlegt werden, und konzentriere dich auf Informationen des Patienten.\
        Wenn keine psychiatrisch relevanten Symptome vorliegen, antworte mit: [{'symptom': 'none', 'section': 'none'}].\
        Dein Output darf maximal 250 Wörter enthalten.",
    },
    {
        "role": "user",
        "content": "Hier sind der Transkriptteil und Kontextinformationen. Extrahiere die Symptome und unterstützenden Abschnitte wie angegeben. Denke Schritt für Schritt, bevor du die endgültige Liste erstellst.",
    },
)
