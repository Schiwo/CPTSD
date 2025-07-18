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
        "content": "You will be given an interview transcript between a psychiatrist and a patient. Your task is to identify any psychiatrically significant symptoms related to depression and bipolar disorder, based on DSM-5 criteria, and the sections that suggest them.\
        Start by carefully reading the transcript. Identify any parts of the conversation that directly suggest one or more of the listed symptoms. Focus only on the symptoms explicitly named below.\
        For each potential symptom, consider whether it matches any of the DSM-5 criteria listed below. Only include it if the patient's wording clearly supports one of the listed symptoms.\
        Then, extract the relevant section of the transcript and link it directly to the symptom it suggests. If a section contains multiple symptoms, list them together in one object.\
        Finally, return your answer in the format: [{'symptom': '...', 'section': '...'}, {'symptom': '...', 'section': '...'}, ...].\
        If a section contains multiple syptoms, answer in the format: [{'symptom': '..., ...', 'section': '...'}, ...].\
        If there are no psychiatrically significant symptoms, respond with: [{'symptom': 'none', 'section': 'none'}].\
        Only use the following list of symptoms:\
        Major depression episode: Depressed mood, Loss of interest or pleasure, Decrease or increase in appetite, Weight loss or gain, Insomnia or hypersomnia, Psychomotor agitation or retardation, Fatigue or loss of energy, Worthlesness or excessive guilt, Difficulty concentrating or indecisiveness, Suicidality.\
        Manic and hypomanic episode: Expansive or elevated or irritable mood, Increased self-esteem or grandiosity, Decreased need for sleep, Increased talkativeness or pressured speech, Flight of ideas or racing thoughts, Distractibility, Increased goal-directed activity or psychomotor agitation, Risky behaviour.\
        Be sure to use only the symptoms named above and quote the exact wording of the interview that supports each symptom.",
    },
    {
        "role": "user",
        "content": "Here is a transcript of a psychiatric consultation. Please extract any psychiatrically significant symptoms related to Depression and Bipolar Disorder and the sections they occur in. Think step by step before providing the final list.",
    },
)

cot_short_de_1 = (
    {
        "role": "system",
        "content": "Du erhälts ein Transkript eines Interviews zwischen einem Psychiater und einem Patienten. Deine Aufgabe ist es, basierend auf DSM-5 Kriterien psychiatrisch relevante Symptome von Depression und bipolaren Störungen zu identifizieren, sowie die jeweiligen Abschnitte, die darauf hindeuten.\
        Beginne damit, das Interview sorgfältig zu lesen. Identifiziere alle Teile des Gesprächs, die direkt auf eines oder mehrere der aufgeführten Symptome hindeuten. Konzentriere dich nur auf die unten genannten Symptome.\
        Überlege bei jedem Symptom, ob es einem der unten aufgeführten DSM-5-Kriterien entspricht. Nimm es nur auf, wenn die Formulierungen des Patienten eindeutig auf eines der aufgelisteten Symptome hindeuten.\
        Extrahiere dann den entsprechenden Abschnitt des Transkripts und verknüpfe ihn mit dem Symptom, auf das er hindeutet. Wenn ein Abschnitt mehrere Symptome enthält, liste sie zusammen in einem Objekt auf.\
        Schließlich, antworte im folgenden Format: [{'symptom': '...', 'section': '...'}, {'symptom': '...', 'section': '...'}, ...].\
        Wenn eine Textstelle mehrere Symptome enthält, verwende folgendes Format: [{'symptom': '..., ...', 'section': '...'}, ...].\
        Wenn keine psychiatrisch relevante Symptome im Interview enthalten sind, antworte mit: [{'symptom': 'none', 'section': 'none'}].\
        Verwende ausschließlich die folgende Liste von Symptomen:\
        Schwere depressive Episode: Depressive Stimmung, Interessen- oder Freudeverlust, Verminderter oder gesteigerter Appetit, Gewichtsverlust oder -zunahme, Insomnie oder Hypersomnie, Psychomotorische Unruhe oder Verlangsamung, Müdigkeit oder Energieverlust, Schuld- oder Wertlosigkeitsgefühle, Konzentrations- oder Entscheidungsschwierigkeiten, Suizidalität.\
        Manische und hypomanische Episode: Gereizte oder gehobene oder expansive Stimmung, Gesteigertes Selbstwertgefühl oder Größenideen, Vermindertes Schlafbedürfnis, Gesteigertes Sprechbedürfnis oder Rededruck, Ideenflucht oder Gedankenrasen, Ablenkbarkeit, Gesteigerte zielgerichtete Aktivität oder psychomotorische Unruhe, Risikoverhalten.\
        Verwende nur die oben genannten Symptome und zitiere den entsprechenden Text wörtlich aus dem Interview.",
    },
    {
        "role": "user",
        "content": "Hier ist ein Transkript eines psychiatrischen Gesprächs. Bitte nenne alle psychiatrisch relevanten Symptome einer Depression und Bipolaren Störung und die dazugehörigen Textstellen. Denke Schritt für Schritt, bevor du die endgültige Liste erstellst.",
    },
)
