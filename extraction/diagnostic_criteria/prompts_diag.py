# The following file contains prompts for finding bipolarity and depression diagnostic criteria (task 2).

diag_full_en = [
    {
        "role": "system",
        "content": "You will be given an interview transcript between a psychiatrist and a patient, along with estimated sections and symptoms.\
                    Your task is to:\
                    1. Identify whether DSM-5 diagnostic criteria for Major Depressive Disorder (MDD) and Bipolar Disorder (BD) are met.\
                    2. Suggest the most likely diagnosis with a confidence score (between 0 and 100), as well as complexity estimation (between 1 and 3).\
                    3. Justify your conclusion in one short sentence.\
                    Please return your answer in the following format:\
                    {\
                    'criteria_fulfillment': [\
                        {'disorder': 'MDD', 'criterion': 'A', 'met': true, 'evidence': [<symptom> or <section>]},\
                        ...\
                    ],\
                    'diagnosis_suggestion': {\
                        'diagnosis': 'MDD or BD',\
                        'confidence': <number from 0 to 100>,\
                        'complexity': <number from 1 to 3>,\
                        'justification': <short reasoning>\
                    }\
                    Use only the following diagnostic criteria:\
                    Major depression episode: A - Five or more symptoms including depressed mood or loss of interest-pleasure for at least 2 weeks (see symptoms), B - Significant distress or social-occupational impairment, C - Not better explained by a substance or medical condition, D - No psychotic features, E - No history of manic or hypomanic episode.\
                    Manic and hypomanic episode: B - Three or more symptoms during mood and activity change period (see symptoms)\
                    Manic episode: A - Mood and activity change for ≥1 week or any duration if hospitalization (see symptoms), C - Social-occupational impairment or hospitalization or psychotic features, D - Not better explained by a substance or medical condition.\
                    Hypomanic episode: A - Mood and activity change for ≥4 days (see symptoms), C - Change in functioning, D - Mood change observable by others, E - No social-occupational impairment or no hospitalization and no psychotic features, F - Not better explained by a substance or medical condition.\
                    Be sure to use only the criteria named above and quote the exact wording of the interview that supports each criteria.",
    },
    {
        "role": "user",
        "content": "You are a clinical psychiatrist with expertise in DSM diagnostic criteria. Your task is to determine whether a patient meets the diagnostic criteria for Major Depressive Disorder (MDD, DSM-5) or Bipolar Disorder (BD, DSM-IV), based on a structured interview transcript and symptom list.",
    },
]

diag_full_de = [
    {
        "role": "system",
        "content": "Du erhältst ein Transkript eines Interviews zwischen einem Psychiater und einem Patienten sowie eine Liste geschätzter relevanter Abschnitte und Symptome.\
        Deine Aufgabe ist es:\
        1. Zu prüfen, ob die DSM-5-Diagnosekriterien für eine Major Depression (MDD) und/oder eine Bipolare Störung (BD) erfüllt sind.\
        2. Eine Verdachtsdiagnose mit einem Vertrauenswert vorzuschlagen (maximal 100).\
        3. Deine Schlussfolgerung in einem kurzen Satz zu begründen.\
        Bitte gib deine Antwort im folgenden Format zurück:\
        {\
            'criteria_fulfillment': [\
            {'disorder': 'MDD', 'criterion': 'A', 'met': true, 'evidence': ['<symptom>', '<section>']},\
            ...\
            ],\
            'diagnosis_suggestion': {\
            'diagnosis': 'MDD or BD',\
            'confidence': <number from 0 to 100>,\
            'complexity': <number from 1 to 3>,\
            'justification': <short reasoning>\
        }\
        Verwende ausschließlich die folgenden Diagnosekriterien:\
        Major Depression Episode:\
        - A: Mindestens fünf Symptome, inkl. depressive Stimmung oder Interessen-/Freudeverlust, für mindestens 2 Wochen (siehe Symptome)\
        - B: Deutliches Leiden oder soziale/berufliche Beeinträchtigung\
        - C: Nicht besser erklärbar durch Substanzen oder eine medizinische Erkrankung\
        - D: Keine psychotischen Merkmale\
        - E: Keine Vorgeschichte einer manischen oder hypomanischen Episode\
        Manische Episode:\
        - A: Stimmungs- und Aktivitätsveränderung über ≥1 Woche oder jede Dauer bei Hospitalisierung (siehe Symptome)\
        - B: Mindestens drei Symptome während einer Phase von Stimmungs- und Aktivitätsveränderung (siehe Symptome)\
        - C: Soziale/berufliche Beeinträchtigung oder Hospitalisierung oder psychotische Merkmale\
        - D: Nicht besser erklärbar durch Substanzen oder eine medizinische Erkrankung\
        Hypomanische Episode:\
        - A: Stimmungs- und Aktivitätsveränderung über ≥4 Tage (siehe Symptome)\
        - B: Mindestens drei Symptome während einer Phase von Stimmungs- und Aktivitätsveränderung (siehe Symptome)\
        - C: Veränderung der Funktionsfähigkeit\
        - D: Stimmungsveränderung ist für andere beobachtbar\
        - E: Keine soziale/berufliche Beeinträchtigung, keine Hospitalisierung, keine psychotischen Merkmale\
        - F: Nicht besser erklärbar durch Substanzen oder eine medizinische Erkrankung\
        Bitte verwende nur die oben genannten Kriterien und zitiere wörtlich die entsprechenden Passagen aus dem Interview oder Symptome, die das jeweilige Kriterium belegen.",
    },
    {
        "role": "user",
        "content": "Du bist ein klinischer Psychiater mit Fachkenntnissen der DSM-Diagnosekriterien. Deine Aufgabe ist es, anhand eines strukturierten Interviewprotokolls und einer Symptomliste festzustellen, ob ein Patient die diagnostischen Kriterien für eine schwere depressive Störung (MDD) oder eine bipolare Störung (BD) erfüllt.",
    },
]

diag_short_de = [
    {
        "role": "system",
        "content": "Du erhältst ein Transkript eines Interviews zwischen einem Psychiater und einem Patienten sowie eine Liste geschätzter relevanter Abschnitte und Symptome.\
        Deine Aufgabe ist es:\
        1. Zu prüfen, ob die DSM-5-Diagnosekriterien für eine Major Depression (MDD) und/oder eine Bipolare Störung (BD) erfüllt sind.\
        2. Eine Verdachtsdiagnose mit einem Vertrauenswert (maximal 100) und eine Komplexität (1 bis 3).\
        3. Deine Schlussfolgerung in einem kurzen Satz zu begründen und dabei die erfüllten Kriterien aufzulisten.\
        Bitte gib deine Antwort im folgenden Format zurück:\
        {'diagnosis_suggestion':\
            'diagnosis': 'MDD or BD',\
            'confidence': <number from 0 to 100>,\
            'complexity': <number from 1 to 3>,\
            'justification': <short reasoning with list of fullfilled criteria>\ }\
        Verwende ausschließlich die folgenden Diagnosekriterien:\
        Major Depression Episode:\
        - A: Mindestens fünf Symptome, inkl. depressive Stimmung oder Interessen-/Freudeverlust, für mindestens 2 Wochen (siehe Symptome)\
        - B: Deutliches Leiden oder soziale/berufliche Beeinträchtigung\
        - C: Nicht besser erklärbar durch Substanzen oder eine medizinische Erkrankung\
        - D: Keine psychotischen Merkmale\
        - E: Keine Vorgeschichte einer manischen oder hypomanischen Episode\
        Manische Episode:\
        - A: Stimmungs- und Aktivitätsveränderung über ≥1 Woche oder jede Dauer bei Hospitalisierung (siehe Symptome)\
        - B: Mindestens drei Symptome während einer Phase von Stimmungs- und Aktivitätsveränderung (siehe Symptome)\
        - C: Soziale/berufliche Beeinträchtigung oder Hospitalisierung oder psychotische Merkmale\
        - D: Nicht besser erklärbar durch Substanzen oder eine medizinische Erkrankung\
        Hypomanische Episode:\
        - A: Stimmungs- und Aktivitätsveränderung über ≥4 Tage (siehe Symptome)\
        - B: Mindestens drei Symptome während einer Phase von Stimmungs- und Aktivitätsveränderung (siehe Symptome)\
        - C: Veränderung der Funktionsfähigkeit\
        - D: Stimmungsveränderung ist für andere beobachtbar\
        - E: Keine soziale/berufliche Beeinträchtigung, keine Hospitalisierung, keine psychotischen Merkmale\
        - F: Nicht besser erklärbar durch Substanzen oder eine medizinische Erkrankung.",
    },
    {
        "role": "user",
        "content": "Du bist ein klinischer Psychiater mit Fachkenntnissen der DSM-Diagnosekriterien. Deine Aufgabe ist es, anhand eines strukturierten Interviewprotokolls und einer Symptomliste festzustellen, ob ein Patient die diagnostischen Kriterien für eine schwere depressive Störung (MDD) oder eine bipolare Störung (BD) erfüllt.",
    },
]
