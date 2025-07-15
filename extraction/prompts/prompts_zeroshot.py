# The following file contains zero-shoot prompts for finding bipolarity and depression symptoms.

# Following prompts are an adaptation of prompts from this repository, translated from Corean to English and German.
# Symptoms have been changed to Major depression episode and Bipolar disorder.
# Sentences are simpler and more direct.

# We do not use the original prompt from the paper, as the repository has been actualised after publication (most recent prompt).

zeroshot_en_1 = [
    {
        "role": "system",
        "content": "You will be given an interview transcript between a psychiatrist and a patient. Your task is to identify any psychiatrically significant symptoms related to depression and bipolar disorder, based on DSM-5 criteria, and the sections that suggest them.\
                    Please return your answer in the format: [{'symptom': '...', 'section': '...'}, {'symptom': '...', 'section': '...'}, ...].\
                    If a section contains multiple syptoms, list them together: [{'symptom': '..., ...', 'section': '...'}, ...].\
                    If there are no psychiatrically significant symptoms, respond with: [{'symptom': 'none', 'section': 'none'}].\
                    Use only the following symptoms:\
                    Major depression episode: Depressed mood, Loss of interest or pleasure, Appetite change (decrease or increase), Weight change (loss or gain), Insomnia, Hypersomnia, Psychomotor agitation, Psychomotor retardation, Fatigue or loss of energy, Worthlesness or excessive guilt, Difficulty concentrating or indecisiveness, Thoughts of death, Suicidal ideation, Suicide plan, Suicide attempt, Significant distress, Social or occupational impairment, Duration ≥2 weeks, Not better explained by a substance or medical condition, No psychotic features (mood-congruent or incongruent), No history of manic or hypomanic episode.\
                    Manic and hypomanic symptoms: Expansive or elevated mood, Irritable mood, Increased activity or energy, Increased self-esteem or grandiosity, Decreased need for sleep, Increased talkativeness or pressured speech, Flight of ideas or racing thoughts, Distractibility, Increased goal-directed activity, Psychomotor agitation, Risky behaviour (e.g. spending, driving), Not better explained by a substance or medical condition (e.g. corticosteroids, antidepressant).\
                    Manic episode (specifiers): Duration ≥1 week or any duration if hospitalization, Social or occupational impairment, Hospitalization, Psychotic features.\
                    Hypomanic episode (specifiers): Duration ≥4 days, Change in functioning, Mood change observable by others, No social or occupational impairment, No hospitalization, No psychotic features.\
                    Be sure to use only the symptoms named above and quote the exact wording of the interview that supports each symptom.",
    },
    {
        "role": "user",
        "content": "Here is a transcript of a psychiatric consultation. Please extract any psychiatrically significant symptoms related to Depression and Bipolar Disorder and the sections they occur in.",
    },
]

zeroshot_de_1 = [
    {
        "role": "system",
        "content": "Du erhälst ein Transkript eines Interviews zwischen einem Psychiater und einem Patienten. Deine Aufgabe ist es, basierend auf DSM-5 Kriterien psychiatrisch relevante Symptome von Depression und bipolaren Störungen zu identifizieren, sowie die jeweiligen Abschnitte, die darauf hindeuten.\
                    Bitte antworte im folgenden Format: [{'symptom': '...', 'section': '...'}, {'symptom': '...', 'section': '...'}, ...].\
                    Wenn eine Textstelle mehrere Symptome enthält, verwende folgendes Format: [{'symptom': '..., ...', 'section': '...'}, ...].\
                    Wenn keine psychiatrisch relevante Symptome im Interview enthalten sind, antworte mit: [{'symptom': 'none', 'section': 'none'}].\
                    Verwende ausschließlich folgende Symptome:\
                    Major depression episode: Depressed mood, Loss of interest or pleasure, Appetite change (decrease or increase), Weight change (loss or gain), Insomnia, Hypersomnia, Psychomotor agitation, Psychomotor retardation, Fatigue or loss of energy, Worthlesness or excessive guilt, Difficulty concentrating or indecisiveness, Thoughts of death, Suicidal ideation, Suicide plan, Suicide attempt, Significant distress, Social or occupational impairment, Duration ≥2 weeks, Not better explained by a substance or medical condition, No psychotic features (mood-congruent or incongruent), No history of manic or hypomanic episode.\
                    Manic and hypomanic symptoms: Expansive or elevated mood, Irritable mood, Increased activity or energy, Increased self-esteem or grandiosity, Decreased need for sleep, Increased talkativeness or pressured speech, Flight of ideas or racing thoughts, Distractibility, Increased goal-directed activity, Psychomotor agitation, Risky behaviour (e.g. spending, driving), Not better explained by a substance or medical condition (e.g. corticosteroids, antidepressant).\
                    Manic episode (specifiers): Duration ≥1 week or any duration if hospitalization, Social or occupational impairment, Hospitalization, Psychotic features.\
                    Hypomanic episode (specifiers): Duration ≥4 days, Change in functioning, Mood change observable by others, No social or occupational impairment, No hospitalization, No psychotic features.\
                    Verwende nur die oben genannten Symptome und zitiere den entsprechenden Text wörtlich aus dem Interview.\
                    ",
    },
    {
        "role": "user",
        "content": "Hier ist ein Transkript eines psychiatrischen Gesprächs. Bitte nenne alle psychiatrisch relevanten Symptome einer Depression und Bipolaren Störung und die dazugehörigen Textstellen.",
    },
]
