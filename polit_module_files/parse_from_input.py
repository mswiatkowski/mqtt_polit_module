end = None


################################################################################


"""
W poniższych słownikach według nstępującego wzoru:
słowo klucz: lista możliwych inputów użytkownika
"""

questions_keys = {
    "kto": ["kto", "któż", "którzy"],
    "ile": ["ile", "ileż"],
    "ilu": ["ilu", "iluż"],
    "w": ["w"]
}

time_keys = {
    "jest": ["jest", "jestże"],
    "sa": ["są"],
    "byl": ["był"]
}

occupations_keys = {
    "prezydent": ["prezydent", "prezydentem", "prezydentów"],
    "posel": ["poseł", "posłem", "posłów"],
    "prezes": ["prezes", "prezesem", "prezesów"],
    "premier": ["premier", "premierem", "premierów"],
    "leader": ["przewodniczący", "przewodniczącym"],
    "rpo": ["rpo", "rzecznik", "rzecznikiem"]
}

gender_keys = {
    "k": ["k",
          "kobieta",
          "kobiet",
          "kobiety"],
    "m": ["m",
          "mężczyzna",
          "mężczyzn",
          "mężczyźni"]
}

clubs_keys = {
    "pis": ["pis",
            "prawo i sprawiedliwość",
            "pisu",
            "pisowi",
            "prawa",
            "prawo",
            "prawie",
            "prawu",
            "prawa i sprawiedliwości",
            "prawu i sprawiedliwości",
            "partia rządząca", "partii rządzącej",
            "klub parlamenterny prawo i sprawiedliwość"],
    "ko": ["ko",
           "koalicja obywatelska",
           "koalicja",
           "koalicji"],
    "lewica": ["lewica",
               "lewica",
               "lewicy",
               "klub poselski lewicy",
               "klubu poselskiego lewicy",
               "klubie poselskim lewicy",
               "koalicyjny klub poselski lewicy",
               "koalicyjnym klubie poselskim lewicy",
               "koalicyjnego klubu poselskiego lewicy"],
    "kp": ["kp",
           "koalicja polska",
           "kape",
           "koalicji polskiej",
           "klub parlamentarny koalicja polska",
           "klubie parlamentarnym koalicji polskiej",
           "klubu parlamentarnego koalicji polskiej",
           "klub parlamentarny koalicji polskiej"],
    "konfederacja": ["konfederacja",
                     "konfederacja",
                     "konfederacji",
                     "konfa",
                     "konfie",
                     "konfy",
                     "koło poselskie konfederacja",
                     "kole poselskim konfederacja",
                     "koła poselskiego konfederacja"],
    "polska2050": ["polska 2050",
                   "polska 2050",
                   "polsce 2050",
                   "2050",
                   "koło parlamentarne polska 2050"],
    "porozumienie": ["porozumienie",
                     "porozumienie",
                     "porozumieniu",
                     "porozumienia"],
    "kukiz15": ["kukiz",
                "kukiz15"],
    "ps": ["ps",
           "polskie sprawy",
           "pees",
           "sprawy",
           "spraw",
           "sprawach",
           "polskich spraw",
           "polskich sprawach",
           "koło poselskie polskie sprawy",
           "kole poselskim polskie sprawy",
           "koła poselskiego polskie sprawy"],
    "pps": ["pepees",
            "pps",
            "koło parlamentarne pps",
            "kole parlamentarym pps"],
    "niezrzeszony": ["niezrzeszony",
                     "niezrzeszeni",
                     "niezrzeszonych"],
    "partia": ["partia",
               "partii",
               "ugrupowanie",
               "ugrupowaniu",
               "klub",
               "klubie",
               "klubu"]
}


def query_splitting(user_query):
    split_user_query = user_query.split()
    return split_user_query


dicts = [questions_keys, time_keys, occupations_keys, gender_keys, clubs_keys]


def parsing_from_input(split_query):
    list_of_keys = []
    for dictionary in dicts:
        for word in split_query:
            for key in dictionary.keys():
                if word in dictionary.get(key):
                    list_of_keys.append(key)
                    break

    print(list_of_keys)

    """Blok odpowiadający komunikatowi zwrotnemu: <<Nie rozumiem ani słowa>>"""
    if list_of_keys == []:
        print("Nie rozumiem")

    return list_of_keys




