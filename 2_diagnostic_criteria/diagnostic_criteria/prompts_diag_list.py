# The following file contains prompts for finding bipolarity and depression diagnostic criteria (task 2).

diag_list_de = [
    {
        "role": "system",
        "content": "Du erhältst ein Transkript eines Interviews zwischen einem Psychiater und einem Patienten, sowie eine Liste geschätzter Symptome.\
        Prüfe, ob die DSM-5-Diagnosekriterien für eine Major Depression (MDD) und/oder eine Bipolare Störung (BD) erfüllt sind\
        und liste die erfüllten Kriterien exakt im folgenden Format auf:\
        {'ausgefüllte Diagnosekriterien': <Kriterium1>, <Kriterium2>, ...}\
        Gibt nur diese Liste zurück, ohne weitere Erklärungen oder zusätzlichen Texte. \
        Deine Antwort darf max. 150 Wörter enthalten.\
        Nutze ausschließlich folgende Diagnosekriterien und fokussiere dich auf Informationen des Patienten:\
        Depressive Episode:\
        - ≥5 Symptome inkl. depressive Stimmung/Interessenverlust, ≥2 Wochen (siehe Symptome)\
        - Deutliches Leiden oder Beeinträchtigung\
        - Keine Substanz-/medizinische Ursache\
        - Keine Psychose\
        - Keine manische/hypomanische Vorgeschichte\
        Manische Episode:\
        - Stimmungs-/Aktivitätsveränderung ≥1 Woche oder Hospitalisierung (siehe Symptome)\
        - ≥3 Symptome in dieser Phase (siehe Symptome)\
        - Beeinträchtigung oder Hospitalisierung oder Psychose\
        - Keine Substanz-/medizinische Ursache\
        Hypomanische Episode:\
        - Stimmungs-/Aktivitätsveränderung ≥4 Tage (siehe Symptome)\
        - ≥3 Symptome in dieser Phase (siehe Symptome)\
        - Funktionsänderung\
        - Stimmungsveränderung für andere beobachtbar\
        - Keine Beeinträchtigung, keine Hospitalisierung, keine Psychose\
        - Keine Substanz-/medizinische Ursache.",
    },
    {
        "role": "user",
        "content": "Hier findest du Transkript und geschätzte Symptome:",
    },
]
