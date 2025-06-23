# The following file contains zero-shoot prompts for finding bipolarity and depression symptoms.

# Short is the original version from this repository, translated from corean to english and german.

zeroshot_short_en_1 = [
    {
        "role": "system",
        "content": "You will be given the following interview between a psychiatrist and a patient. If you think there are any psychiatrically significant symptoms in the following interview, please tell what they are and the sections that suggest them.\
                    Please answer in the form [{'symptom': '...', 'section': '...'}, {'symptom': '...', 'section': '...'}, ...].\
                    If you think there are multiple symptoms in a particular section, answer in the form [{'symptom': '..., ...', 'section': '...'}, ...].\
                    If there are no psychiatrically significant symptoms and sections in a given interview, please answer [{'symptom': 'none', 'section': 'none'}].\
                    I will give you the following 40 symptoms associated with Depression and Bipolarity:\
                    For Major depression episode: Depressed mood Decreased interest,  Decreased appetite, Increased appetite, Insomnia, Hypersomnia, Psychomotor agitation, Psychomotor retardation, Fatigue, Worthlesness, Excessive guilt, Decreased concentration, Decreased decision, Suicide ideation, Suicide plan, Suicide attempt, Signficant distress, Social-occupational impairment, No medication, No pychotic disorder, No manic or hypomanic episode.\
                    For Bipolar disorder: Expansive mood, Increased energy, Increased self-esteem, Decreased need for sleep, Increased talk, Increased ideas, Decreased concentration, Increase in goal-directed activity, Psychomotor agitation, Increased activities with high potential for painful consequences, No medication \
                    Manic: Social-occupational impairment, Hospitalization, Psychotic features \
                    Hypomanic: Change in functioning, Mood disturbance and change in functioning observable by others, No social-occupational impairment, No hospitalization, No psychotic features.\
                    Be sure to answer with the symptoms named above and with the exact wording of the interview.",
    },
    {
        "role": "user",
        "content": "If you think the following consultation has psychiatrically significant symptoms, please tell what they are and the sections in the text where you find these symptoms.",
    },
]

zeroshot_short_de_1 = [
    {
        "role": "system",
        "content": "Ihnen wird das folgende Gespräch zwischen einem Psychiater und einem Patienten vorgelegt. Wenn Sie der Meinung sind, dass in dem folgenden Gespräch psychiatrisch bedeutsame Symptome vorkommen, geben Sie bitte an, um welche Symptome es sich handelt und welche Abschnitte darauf hindeuten.\
                    Bitte beantworten Sie Symptome in der Form '- Symptoms : ...' und Abschnitte in der Form '- Sections : ...'.\
                    Wenn es in einem bestimmten Interview keine psychiatrisch bedeutsamen Symptome gibt, antworten Sie bitte mit 'N/A'.\
                    Ich gebe Ihnen 40 mögliche Symptome, die mit Depression und Bipolarität assoziiert sind:\
                    Für eine schwere depressive Episode: Depressive Stimmung, Vermindertes Interesse, Verminderter Appetit, Gesteigerter Appetit, Schlaflosigkeit, Hypersomnie, Psychomotorische Unruhe, Psychomotorische Retardierung, Müdigkeit, Wertlosigkeit, Übermäßiges Schuldgefühl, Verminderte Konzentration, Verminderte Entscheidungsfähigkeit, Selbstmordgedanken, Selbstmordpläne, Selbstmordversuch, Signifikante Notlage, Sozial-berufliche Beeinträchtigung, Keine Medikamente, Keine pychotische Störung, Keine manische oder hypomanische Episode\
                    Bei bipolarer Störung: Expansive Stimmung, Gesteigerte Energie, Gesteigertes Selbstwertgefühl, Vermindertes Schlafbedürfnis, Gesteigertes Reden, Gesteigerte Ideen, Verminderte Konzentration, Gesteigerte zielgerichtete Aktivität, Psychomotorische Unruhe, Gesteigerte Aktivitäten mit hohem Potenzial für schmerzhafte Konsequenzen, Keine Medikation \
                    Manisch: Sozial-berufliche Beeinträchtigung, Krankenhausaufenthalt, Psychotische Merkmale \
                    Hypomanisch: Veränderung der Funktionsweise, Von anderen beobachteter Veränderung der Funktionsweise, Keine sozial-berufliche Beeinträchtigung, Kein Krankenhausaufenthalt, Keine psychotischen Merkmale\
                    Antworten Sie mit den oben bennanten Symptomen und mit dem genauen Wortlaut des Interviews.\
                    ",
    },
    {
        "role": "user",
        "content": "Wenn Sie der Meinung sind, dass die folgende Befragung psychiatrisch bedeutsame Symptome aufweist, geben Sie bitte an, um welche Symptome es sich handelt und in welchen Abschnitten des Textes Sie diese Symptome finden.",
    },
]

# Long is the original prompt of the paper in english. It has also been translated into german.
zeroshot_long_en_1 = [
    {
        "role": "system",
        "content": "You will be given an interview. When answering the psychiatric symptoms associated with Bipolarity or Depression and the section that represents them, please be sure to answer in the form [{‘Symptom’: ‘...’, ‘Section’: ‘...’}, {‘Symptom’: ‘...’, ‘Section’: ‘...’}, ...].\
                   If you think there are multiple symptoms in a particular section, you can answer in the form [{‘Symptom’: ‘..., ...’, ‘Section’: ‘...’}, ...].\
                   If there are no psychiatric symptoms associated with Bipolarity and Depression in a given interview, please answer [{‘Symptom’: ‘none’, ‘Section’: ‘none’}].\
                   I will give you following 40 symptoms associated with Depression and Bipolarity:\
                   For Major depression episode: Depressed mood Decreased interest,  Decreased appetite, Increased appetite, Insomnia, Hypersomnia, Psychomotor agitation, Psychomotor retardation, Fatigue, Worthlesness, Excessive guilt, Decreased concentration, Decreased decision, Suicide ideation, Suicide plan, Suicide attempt, Signficant distress, Social-occupational impairment, No medication, No pychotic disorder, No manic or hypomanic episode.\
                   For Bipolar disorder: Expansive mood, Increased energy, Increased self-esteem, Decreased need for sleep, Increased talk, Increased ideas, Decreased concentration, Increase in goal-directed activity, Psychomotor agitation, Increased activities with high potential for painful consequences, No medication \
                   Manic: Social-occupational impairment, Hospitalization, Psychotic features \
                   Hypomanic: Change in functioning, Mood disturbance and change in functioning observable by others, No social-occupational impairment, No hospitalization, No psychotic features.\
                   Be sure to answer with the symptoms named above and with the exact wording of the interview.",
    },
    {
        "role": "user",
        "content": "Look at the following interview and if you think that there are psychiatric symptoms associated with Bipolarity and Depression in the interview, please tell me the symptom and the section that represents it",
    },
]

zeroshot_long_de_1 = [
    {
        "role": "system",
        "content": "Sie werden ein Interview erhalten. Achten Sie bei der Beantwortung der psychiatrischen Symptome im Zusammenhang mit Bipolarität oder Depression und dem entsprechenden Abschnitt darauf, in der Form [{'Symptom': '...', 'Section': '...'}, {'Symptom': '...', 'Section': '...'}, ...] zu antworten.\
                   Wenn Sie der Meinung sind, dass es in einem bestimmten Abschnitt mehrere Symptome gibt, können Sie in der Form [{'Symptom': '..., ...', 'Section': '...'}, ...] antworten.\
                   Wenn in einem bestimmten Interview keine psychiatrischen Symptome im Zusammenhang mit Bipolarität und Depression auftreten, antworten Sie bitte in der Form [{'Symptom': 'none', 'Section': 'none'}].\
                   Ich gebe Ihnen 40 mögliche Symptome, die mit Depression und Bipolarität assoziiert sind:\
                   Für eine schwere depressive Episode: Depressive Stimmung, Vermindertes Interesse, Verminderter Appetit, Gesteigerter Appetit, Schlaflosigkeit, Hypersomnie, Psychomotorische Unruhe, Psychomotorische Retardierung, Müdigkeit, Wertlosigkeit, Übermäßiges Schuldgefühl, Verminderte Konzentration, Verminderte Entscheidungsfähigkeit, Selbstmordgedanken, Selbstmordpläne, Selbstmordversuch, Signifikante Notlage, Sozial-berufliche Beeinträchtigung, Keine Medikamente, Keine pychotische Störung, Keine manische oder hypomanische Episode\
                   Bei bipolarer Störung: Expansive Stimmung, Gesteigerte Energie, Gesteigertes Selbstwertgefühl, Vermindertes Schlafbedürfnis, Gesteigertes Reden, Gesteigerte Ideen, Verminderte Konzentration, Gesteigerte zielgerichtete Aktivität, Psychomotorische Unruhe, Gesteigerte Aktivitäten mit hohem Potenzial für schmerzhafte Konsequenzen, Keine Medikation \
                   Manisch: Sozial-berufliche Beeinträchtigung, Krankenhausaufenthalt, Psychotische Merkmale \
                   Hypomanisch: Veränderung der Funktionsweise, Von anderen beobachteter Veränderung der Funktionsweise, Keine sozial-berufliche Beeinträchtigung, Kein Krankenhausaufenthalt, Keine psychotischen Merkmale\
                   Antworten Sie mit den oben bennanten Symptomen und mit dem genauen Wortlaut des Interviews.",
    },
    {
        "role": "user",
        "content": "Schauen Sie sich das folgende Interview an, und wenn Sie der Meinung sind, dass es psychiatrische Symptome gibt, die mit Bipolarität und Depression in Verbindung stehen, nennen Sie mir bitte das Symptom und den Abschnitt, der es darstellt",
    },
]
