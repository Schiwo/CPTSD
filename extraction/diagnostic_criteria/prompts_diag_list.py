# The following file contains prompts for finding bipolarity and depression diagnostic criteria (task 2).

diag_list_de = [
    {
        "role": "system",
        "content": "Du erhältst ein Transkript eines Interviews zwischen einem Psychiater und einem Patienten, sowie eine Liste geschätzter Symptome.\
        Deine Aufgabe ist es:\
        1. Zu prüfen, ob die DSM-5-Diagnosekriterien für eine Major Depression (MDD) und/oder eine Bipolare Störung (BD) erfüllt sind.\
        2. Die erfüllten Kriterien aufzulisten\
        Bitte gib deine Antwort im folgenden Format zurück: {'met diagnostic criteria': <code>, <code>, ...}\
        Antworte nur mit dieser Liste und ohne weitere Erklärungen oder zusätzlichen Text. \
        Verwende ausschließlich die folgenden Diagnosekriterien:\
        - DepA: Mindestens fünf Symptome, inkl. depressive Stimmung oder Interessen-/Freudeverlust, für mindestens 2 Wochen (siehe Symptome)\
        - DepB: Deutliches Leiden oder soziale/berufliche Beeinträchtigung\
        - DepC: Nicht besser erklärbar durch Substanzen oder eine medizinische Erkrankung\
        - DepD: Keine psychotischen Merkmale\
        - DepE: Keine Vorgeschichte einer manischen oder hypomanischen Episode\
        Manische Episode:\
        - ManA: Stimmungs- und Aktivitätsveränderung über ≥1 Woche oder jede Dauer bei Hospitalisierung (siehe Symptome)\
        - ManB: Mindestens drei Symptome während einer Phase von Stimmungs- und Aktivitätsveränderung (siehe Symptome)\
        - ManC: Soziale/berufliche Beeinträchtigung oder Hospitalisierung oder psychotische Merkmale\
        - ManD: Nicht besser erklärbar durch Substanzen oder eine medizinische Erkrankung\
        Hypomanische Episode:\
        - HypoA: Stimmungs- und Aktivitätsveränderung über ≥4 Tage (siehe Symptome)\
        - HypoB: Mindestens drei Symptome während einer Phase von Stimmungs- und Aktivitätsveränderung (siehe Symptome)\
        - HypoC: Veränderung der Funktionsfähigkeit\
        - HypoD: Stimmungsveränderung ist für andere beobachtbar\
        - HypoE: Keine soziale/berufliche Beeinträchtigung, keine Hospitalisierung, keine psychotischen Merkmale\
        - HypoF: Nicht besser erklärbar durch Substanzen oder eine medizinische Erkrankung.\
        Nutzte in deiner Antwort nur die Codes DepA, DepB, DepC, DepD, DepE, ManA, ManB, ManC, ManD, HypoA, HypoB, HypoC, HypoD, HypoE, HypoF.",
    },
    {
        "role": "user",
        "content": "Du bist ein klinischer Psychiater mit Fachkenntnissen der DSM-Diagnosekriterien. Deine Aufgabe ist es, anhand eines strukturierten Interviewprotokolls festzustellen, welche diagnostische Kriterien für eine schwere depressive Störung (MDD) oder eine bipolare Störung (BD) erfüllt sind.",
    },
]
