# The following file contains in-context-learning prompts for finding bipolarity and depression symptoms.

# Short is the adapted version from this repository, translated from Corean to English and German.
# We use the same sentences as in zero-shot prompting in order to reduce bias and be able to compare both methods. Only sentences related to in-context-learning (input and output) have been added.
# As in zero-shot version:
# Symptoms have been changed to Major depression episode and Bipolar disorder.
# Sentences are simpler and more direct.

# We do not use the original prompt from the paper, as the repository has been actualised after publication (most recent prompt).


icl_en_1 = [
    {
        "role": "system",
        "content": "You'll have several inputs-outputs examples.\
                    The input is an interview transcript. The output is a list of pychiatric symptoms related to Depression and Bipolar disorders, and the corresponding sections from the interview.\
                    Your task is to identify any psychiatrically significant symptoms related to depression and bipolar disorder, based on DSM-5 criteria, and the sections that suggest them.\
                    Use in-context-learning from previous examples to guide your answers.\
                    Please return your answer in the format: [{'symptom': '...', 'section': '...'}, {'symptom': '...', 'section': '...'}, ...].\
                    If a section contains multiple syptoms, answer in the format: [{'symptom': '..., ...', 'section': '...'}, ...].\
                    If there are no psychiatrically significant symptoms, respond with: [{'symptom': 'none', 'section': 'none'}].\
                    Only use the following list of symptoms:\
                    Major depression episode: Depressed mood, Loss of interest or pleasure, Appetite change (decrease or increase), Weight change (loss or gain), Insomnia, Hypersomnia, Psychomotor agitation, Psychomotor retardation, Fatigue or loss of energy, Worthlesness or excessive guilt, Difficulty concentrating or indecisiveness, Thoughts of death, Suicidal ideation, Suicide plan, Suicide attempt, Significant distress, Social or occupational impairment, Duration ≥2 weeks, Not better explained by a substance or medical condition, No psychotic features (mood-congruent or incongruent), No history of manic or hypomanic episode.\
                    Manic and hypomanic symptoms: Expansive or elevated mood, Irritable mood, Increased activity or energy, Increased self-esteem or grandiosity, Decreased need for sleep, Increased talkativeness or pressured speech, Flight of ideas or racing thoughts, Distractibility, Increased goal-directed activity, Psychomotor agitation, Risky behaviour (e.g. spending, driving), Not better explained by a substance or medical condition (e.g. corticosteroids, antidepressant).\
                    Manic episode (specifiers): Duration ≥1 week or any duration if hospitalization, Social or occupational impairment, Hospitalization, Psychotic features.\
                    Hypomanic episode (specifiers): Duration ≥4 days, Change in functioning, Mood change observable by others, No social or occupational impairment, No hospitalization, No psychotic features.\
                    Be sure to use only the symptoms named above and quote the exact wording of the interview that supports each symptom.",
    },
    {
        "role": "user",
        "content": "Based on the previous input and output examples, analyse the last input transript of a psychiatric consultation. Please extract any psychiatrically significant symptoms related to Depression and Bipolar Disorder and the sections they occur in.",
    },
]

icl_de_1 = [
    {
        "role": "system",
        "content": "Du erhälst mehrere Beispiele von Inputs und Outputs.\
                    Der Input ist ein Interviewtranskript. Der Output ist eine Liste psychiatrischer Symptome einer Depression und bipolaren Störung sowie die entsprechende Abschnitte aus dem Interview.\
                    Deine Aufgabe ist es, basierend auf DSM-5 Kriterien psychiatrisch relevante Symptome von Depression und bipolaren Störungen zu identifizieren, sowie die jeweiligen Abschnitte, die darauf hindeuten.\
                    Nutze In-Context-Learning und beziehe dich auf frühere Beispiele, um deine Antwort zu optimieren.\
                    Bitte antworte im folgenden Format: [{'symptom': '...', 'section': '...'}, {'symptom': '...', 'section': '...'}, ...].\
                    Wenn eine Textstelle mehrere Symptome enthält, verwende folgendes Format: [{'symptom': '..., ...', 'section': '...'}, ...].\
                    Wenn keine psychiatrisch relevante Symptome im Interview enthalten sind, antworte mit: [{'symptom': 'none', 'section': 'none'}].\
                    Verwende ausschließlich die folgende Liste von Symptomen:\
                    Major depression episode: Depressed mood, Loss of interest or pleasure, Appetite change (decrease or increase), Weight change (loss or gain), Insomnia, Hypersomnia, Psychomotor agitation, Psychomotor retardation, Fatigue or loss of energy, Worthlesness or excessive guilt, Difficulty concentrating or indecisiveness, Thoughts of death, Suicidal ideation, Suicide plan, Suicide attempt, Significant distress, Social or occupational impairment, Duration ≥2 weeks, Not better explained by a substance or medical condition, No psychotic features (mood-congruent or incongruent), No history of manic or hypomanic episode.\
                    Manic and hypomanic symptoms: Expansive or elevated mood, Irritable mood, Increased activity or energy, Increased self-esteem or grandiosity, Decreased need for sleep, Increased talkativeness or pressured speech, Flight of ideas or racing thoughts, Distractibility, Increased goal-directed activity, Psychomotor agitation, Risky behaviour (e.g. spending, driving), Not better explained by a substance or medical condition (e.g. corticosteroids, antidepressant).\
                    Manic episode (specifiers): Duration ≥1 week or any duration if hospitalization, Social or occupational impairment, Hospitalization, Psychotic features.\
                    Hypomanic episode (specifiers): Duration ≥4 days, Change in functioning, Mood change observable by others, No social or occupational impairment, No hospitalization, No psychotic features.\
                    Verwende nur die oben genannten Symptome und zitiere den entsprechenden Text wörtlich aus dem Interview.",
    },
    {
        "role": "user",
        "content": "Analysiere den letzten Input einer psychiatrischen Konsultation basierend auf den vorherigen Inputs- und Outputs-Beispielen. Bitte nenne alle psychiatrisch relevanten Symptome einer Depression und Bipolaren Störung und die dazugehörigen Textstellen.",
    },
]
