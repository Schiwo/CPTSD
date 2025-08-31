# The following file contains zero-shoot prompts for finding bipolarity and depression symptoms.

# Following prompts are an adaptation of prompts from this repository, translated from Corean to English and German.
# Symptoms have been changed to Major depression episode and Bipolar disorder.
# Sentences are simpler and more direct.

# We do not use the original prompt from the paper, as the repository has been actualised after publication (most recent prompt).

zeroshot_en_1 = [
    {
        "role": "system",
        "content": "You are given part of an interview transcript between a psychiatrist and a patient, and as context the interview's summary as well as the last output for the interview part before.\
                    Identify psychiatrically significant symptoms (DSM-5) for Major Depression Episode and Bipolar Disorder, and quote the exact wording (verbatim spans) that supports each symptom.\
                    Return only valid JSON as a list of objects: [{'symptom': '<label>', 'section': '<exact transcript quote>'}, {'symptom': '<label>', 'section': '<exact transcript quote>'}, ...].\
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
        "content": "Here are the transcript part and context information. Extract the symptoms and supporting sections as specified.",
    },
]

zeroshot_de_1 = [
    {
        "role": "system",
        "content": "Du erhältst ein Teil des Interviewtranskripts, und als Kontext die Zusammenfassung des Interviews und die vorherige Ausgabe.\
                    Identifiziere psychiatrisch relevante Symptome für Major Depression Episode und Bipolare Störungen (DSM-5), und zitiere die jeweiligen Abschnitte (Wortlaute), die jedes Symptom belegen.\
                    Gib nur gültiges JSON als Liste von Objekten zurück: [{'symptom': '<label>', 'section': '<exact transcript quote>'}, {'symptom': '<label>', 'section': '<exact transcript quote>'}, ...].\
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
        "content": "Hier sind der Transkriptteil und Kontextinformationen. Extrahiere die Symptome und unterstützenden Abschnitte wie angegeben.",
    },
]
