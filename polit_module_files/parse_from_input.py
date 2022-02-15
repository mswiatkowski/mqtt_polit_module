
user_input = input("usr_input>>> ")
split_usr_input = user_input.split()
print(split_usr_input)


################################################################################


"""
W poniższych słownikach według nstępującego wzoru:
słowo klucz: lista inputów użytkownika
"""

questions_keys = {
    "kto": ["kto", "któż", "którzy"],
    "ile": ["ile", "ileż"],
    "ilu": ["ilu", "iluż"]
}

time_keys = {
    "jest": ["jest", "jestże"],
    "sa": ["są"],
    "byl": ["był"]
}

occupations_keys = {
    "prezydent": ["prezydent", "prezydentem"],
    "posel": ["poseł", "posłem"],
    "prezes": ["prezes", "prezesem"],
    "premier": ["premier", "premierem"],
    "leader": ["przewodniczący", "przewodniczącym"]
}

clubs_keys = {
    "pis": ["pis",
            "pisu",
            "pisowi",
            "prawo i sprawiedliwość",
            "prawa i sprawiedliwości",
            "prawu i sprawiedliwości",
            "partia rządząca", "partii rządzącej",
            "klub parlamenterny prawo i sprawiedliwość"],
    "ko": ["ko",
           "koalicja obywatelska"],
    "lewica": ["lewica",
               "lewicy",
               "klub poselski lewicy",
               "klubu poselskiego lewicy",
               "klubie poselskim lewicy",
               "koalicyjny klub poselski lewicy",
               "koalicyjnym klubie poselskim lewicy",
               "koalicyjnego klubu poselskiego lewicy"],
    "kp": ["kp",
           "koalicja polska",
           "koalicji polskiej",
           "klub parlamentarny koalicja polska",
           "klubie parlamentarnym koalicji polskiej",
           "klubu parlamentarnego koalicji polskiej",
           "klub parlamentarny koalicji polskiej"],
    "konfederacja": ["konfederacja",
                     "konfederacji",
                     "konfa",
                     "konfie",
                     "konfy",
                     "koło poselskie konfederacja",
                     "kole poselskim konfederacja",
                     "koła poselskiego konfederacja"],
    "polska2050": ["polska 2050",
                   "polsce 2050",
                   "koło parlamentarne polska 2050"],
    "porozumienie": ["porozumienie",
                     "porozumieniu",
                     "porozumienia"],
    "kukiz15": ["kukiz15"],
    "ps": ["ps",
           "p s"
           "pe es",
           "polskie sprawy",
           "polskich spraw",
           "polskich sprawach",
           "koło poselskie polskie sprawy",
           "kole poselskim polskie sprawy",
           "koła poselskiego polskie sprawy"],
    "pps": ["pps",
            "koło parlamentarne pps",
            "kole parlamentarym pps"],
    "niezrzeszony": ["niezrzeszony",
                     "niezrzeszeni",
                     "niezrzeszonych"]
}

questions = {
    "kto": 'kto',
    "któż": 'kto',
    "ile": 'ile',
    "ilu": 'ile'
}

time = {
    "jest": 'jest',
    "jestże": 'jest',
    "był": 'był'
}

occupations = {
    "prezydent": 'prezydent',
    "prezydentem": 'prezydent',
    "poseł": 'poseł',
    "posłem": 'poseł',
    "posłów": 'posłowie',
    "premier": 'premier',
    "premierem": 'premier',
    "prezes": 'prezes',
    "prezesem": 'prezes'
}

parties = {
    "pis": 'pis',
    "pisu": 'pis',
    "peo": 'po',
    "razem": 'razem',
    "konfederacja": 'konfederacja',
    "konfederacji": 'konfederacja'
}


################################################################################


translated_usr_input = []

"""Słowa niebędące kluczem zostają pominięte"""
for word in split_usr_input:
    if word in questions.keys():
        translated_usr_input.append(questions.get(word))
    elif word in time.keys():
        translated_usr_input.append(time.get(word))
    elif word in occupations.keys():
        translated_usr_input.append(occupations.get(word))
    elif word in parties.keys():
        translated_usr_input.append(parties.get(word))

"""Blok odpowiadający komunikatowi zwrotnemu: <<Nie rozumiem ani słowa>>"""
if translated_usr_input == []:
    translated_usr_input = "Nie rozumiem"


################################################################################


input_words = translated_usr_input