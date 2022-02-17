end = None


"""
##################################################################################################

Plik parse_from_input.py zawiera funkcje pozwalające przetworzyć zapytanie użytkownika na listę słów 
kluczowych, które następnie może wykorzystać silnik wyszukiwania. Oprócz dwóch parsujących funkcji
plik zawiera również słowniki, które pozwalają zakodować użyte przez użytkownika w zapytaniu 
słowa.

##################################################################################################
"""

"""
Poniższe słowniki zawierają klucze pozwalające zakodować wypowiedź na użytek dalszego przetwarzania.
Stosowany jest tu następujący wzór:
klucz: [lista słów, które mogą pojawić się w zapytaniu]
"""

# klucze rozpoczęcia zapytania
questions_keys = {
    "kto": ["kto", "któż"],
    "ile": ["ile", "ileż"],
    "ilu": ["ilu", "iluż"],
    "w": ["w"]
}

# klucze określenia czasu
time_keys = {
    "jest": ["jest", "jestże"],
}

# klucze zapytania o funkcję
occupations_keys = {
    "prezydent": ["prezydent", "prezydentem", "prezydentów"],
    "posel": ["poseł", "posłem", "posłów"],
    "premier": ["premier", "premierem", "premierów"],
    "leader": ["przewodniczący", "przewodniczącym", "lider", "liderem", "szef", "szefem"],
    "rpo": ["rpo", "rzecznik", "rzecznikiem"]
}

# klucze zapytania o płeć
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

# klucze zapytania o przynależność partyjną
# druga pozycja w liście to nazwa użytkowa
clubs_keys = {
    "pis": ["pis",
            "prawo i sprawiedliwość",
            "pisu",
            "pisowi",
            "prawa",
            "prawo",
            "prawie",
            "prawu"],
    "ko": ["ko",
           "koalicja obywatelska",
           "koalicja",
           "koalicji"],
    "lewica": ["lewica",
               "lewica",
               "lewicy"],
    "kp": ["kp",
           "koalicja polska",
           "polska",
           "polskiej",
           "kape"],
    "konfederacja": ["konfederacja",
                     "konfederacja",
                     "konfederacji",
                     "konfa",
                     "konfie",
                     "konfy"],
    "polska2050": ["2050",
                   "pięćdziesiąt",
                   "polska 2050"],
    "porozumienie": ["porozumienie",
                     "porozumienie",
                     "porozumieniu",
                     "porozumienia"],
    "kukiz15": ["kukiz",
                "piętnaście",
                "kukiz15"],
    "ps": ["ps",
           "polskie sprawy",
           "pees",
           "sprawy",
           "spraw",
           "sprawach",
           "polskich"],
    "pps": ["pepees",
            "polska partia socjalistyczna",
            "pps"],
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
    """
    Funkcja rozbijająca zapytanie na listę wchodzących w jego skład słów.
    :param user_query: zapytanie użytkownika.
    :return: zapytanie użytkownika w formie listy poszczególnych słów.
    """
    split_user_query = user_query.split()
    return split_user_query


# lista słowników słów kluczowych
dicts = [questions_keys, time_keys, occupations_keys, gender_keys, clubs_keys]


def parse_from_input(split_query):
    """
    Funkcja kodująca rozbite zapytanie użytkownika na listę kodów odpowiadających słowom z zapytania.
    Tworzy listę, która będzie użyta w dalszym przetwarzaniu.
    :param split_query: zapytanie użytkownika w formie listy poszczególnych słów.
    :return: zakodowane zapytanie użytkownika.
    """
    list_of_keys = []
    for dictionary in dicts:                        # dla każdego słownika kluczy
        for word in split_query:                    # dla każdego słowa w zapytaniu
            for key in dictionary.keys():           # dla każdego klucza w konkretnym słowniku
                if word in dictionary.get(key):
                    list_of_keys.append(key)
                    break

    print(list_of_keys)

    """Blok odpowiadający komunikatowi zwrotnemu: <<Nie rozumiem ani słowa>>"""
    if list_of_keys == []:
        return "Nie rozumiem"

    return list_of_keys
