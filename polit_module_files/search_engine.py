import csv
import parse_from_input as pfi  # Zaimportowanie programu parsującego


"""
##################################################################################################

Plik search_engine.py jest zasadniczo "mózgiem" modułu. To w nim bazy polityków są przeszukiwane, 
a odpowiedzi na zapytania formułowane. Funkcje korzystają z pliku parse_from_input.py, który 
zawiera słownik słów kluczowych oraz z plików csv:
- sejm.csv - zawierającego dane na temat posłów i posłanek;
- politicians.csv - zawierającego dane na temat polityków pełniących ważniejsze lub wyróżniające 
się funkcje
- clubs.csv - zawierającego dane na temat klubów i kół w polskim sejmie (traktowane są one jednak 
dla uproszczenia jak partie)

##################################################################################################
"""



"""Poniżej znajduje się blok kodu potrzebnego do zapytań o członkostwo w partiach.
Pozwala on przeanalizować imiona i nazwiska oddzielnie"""
firstnames = []
lastnames = []
with open("sejm.csv", "r", encoding="utf-8") as sejm:
    sejm = csv.reader(sejm)
    for row in sejm:
        firstnames.append(row[1])
        lastnames.append(row[0])

lastnames = [y for x in lastnames for y in x.split(' ')]    # Rozbicie dwuczłonowych nazwisk na pojedyncze elementy listy



################################################################################

def search_politicians(keyword):
    """
    Funkcja przeszukująca polityków pod względem funkcji.
    :param keyword: pojedynczy element sparsowanego zapytania.
    :return: fraza będąca odpowiedzią na zapytanie.
    """
    with open('politicians.csv', 'r', encoding="utf-8") as polits:
        reader = csv.reader(polits)
        for row in reader:
            if keyword in row:
                return f'{keyword} Polski to {row[1]} {row[0]}'


def count_sejm(keyword="", party=""):
    """
    Funkcja licząca członków sejmu. Oba argumenty opcjonalne.
    :param keyword: pojedynczy element sparsowanego zapytania oznaczający płeć.
    :param party: pojedynczy element sparsowanego zapytania oznaczający partię.
    :return: integer wyrażający liczbę osób w sejmie.
    """
    count = 0
    with open('sejm.csv', 'r', encoding="utf-8") as sejm:
        reader = csv.reader(sejm)
        for row in reader:
            if keyword in row and party == "":
                count += 1
            elif keyword in row and party in row:
                count += 1
    # print(count)
    return count

def search_kto(keywords):
    """
    Funkcja odpowiadająca na pytanie o to, kto pełni daną funkcję.
    :param keywords: sparsowane zapytanie użytkownika.
    :return: wykonanie funkcji search_politicians().
    """
    if "kto" in keywords:
        if "prezydent" in keywords:
            return search_politicians("prezydent")
        if "rpo" in keywords:
            return search_politicians("rzecznik praw obywatelskich")


def search_ilu(keywords):
    """
    Funkcja obsługująca zapytania o liczebność polityków.
    :param keywords: sparsowane zapytanie użytkownika.
    :return: fraza będąca odpowiedzią na zapytanie.
    """
    if "ilu" in keywords:
        if "posel" in keywords:
            for word in keywords:
                if word in pfi.clubs_keys.keys():
                    if word == "niezrzeszony":  # wyszczególnienie posłów niezrzeszonych wynika z przyczyn stylistycznych
                        return f"Posłów niezrzeszonych jest w sejmie {count_sejm(word)}"
                    else:
                        return f"{pfi.clubs_keys.get(word)[1]} ma w sejmie {count_sejm(word)} posłów"
            return f"posłów w sejmie jest {count_sejm()}"
        if "prezydent" in keywords:
            return "prezydent jest tylko jeden"
        if "premier" in keywords:
            return "premier jest tylko jeden"
        if "m" in keywords: # z przyczyn gramatycznych rozróżnienie ze względu na płeć znajduje się w tej funkcji
            for word in keywords:
                if word in pfi.clubs_keys.keys() and word != "partia":
                    return f"mężczyzn w partii {word} jest {count_sejm('m', word)}"
            return f"mężczyzn jest w sejmie {count_sejm('m')}"


def search_ile(keywords):
    """
    Rozszerzenie gramatyczne funkcji liczącej polityków. Ta funkcja liczy tylko kobiety.
    :param keywords: sparsowane zapytanie użytkownika.
    :return: fraza będąca odpowiedzią na zapytanie.
    """
    if "ile" in keywords:
        if "k" in keywords:
            for word in keywords:
                if word in pfi.clubs_keys.keys() and word != "partia":
                    return f"kobiet w partii {word} jest {count_sejm('k', word)}"
            return f"kobiet jest w sejmie {count_sejm('k')}"


def search_w(keywords, split_query):
    """
    Funkcja obsługująca zapytania zaczynające się na "w". Głównie dotyczące przynależności kogoś do partii.
    :param keywords: sparsowane zapytanie użytkownika.
    :param split_query: niesparsowane, ale podzielone na odrębne słowa zapytanie użytkownika.
    :return: fraza będąca odpowiedzią na zapytanie.
    """
    if "w" in keywords[0]:
        """Obie listy poniżej różnią się od tych z początku kody tym, 
        że te zawierają tylko elementy wyszukane w bazie polityków"""
        list_of_lastnames = []
        list_of_firstnames = []
        club = []
        # print(split_query)

        for name in split_query[1:]:
            with open('sejm.csv', 'r', encoding="utf-8") as sejm:
                sejm = csv.reader(sejm)

                for row in sejm:
                    """Oddzielnie przetwarzane są imiona i nazwiska"""
                    if name in row[0] and name in lastnames:
                        list_of_lastnames.append(name)
                        club.append(row[2])
                    if name in row[1] and name in firstnames:
                        club.append(row[2])
                        list_of_firstnames.append(name)


        # print(list_of_firstnames)

        """W poniższym bloku kodu sprawdzane są przypadki powtórzeń imion i nazwisk, a także sytuacja,
        w której jakiejś osoby nie ma w bazie danych"""
        if len(list_of_lastnames) > 1 and len(list_of_firstnames) == 0:     # powtórzenie nazwiska
            return "Więcej niż jedna osoba się tak nazywa"
        elif len(list_of_lastnames) == 0 and len(list_of_firstnames) > 1:   # powtórzenie imienia
            return "Więcej niż jedna osoba ma tak na imię"
        elif len(list_of_lastnames) == 1 and len(list_of_firstnames) == 0:  # podanie w zapytaniu samego nazwiska
            return f"{list_of_lastnames[0]} jest w partii {club[0]}"
        elif len(list_of_firstnames) == 1 and len(list_of_lastnames) == 0:  # podanie w zapytaniu samego imienia
            return f"{list_of_firstnames[0]} jest w partii {club[0]}"
        elif len(list_of_firstnames) == 0 and len(list_of_lastnames) == 0:  # podanie w zapytaniu osoby spoza listy
            return "w żadnej partii nie ma takiej osoby"
        else:                                                               # podanie imienia i nazwiska
            return f"{list_of_firstnames[0]} {list_of_lastnames[0]} jest w partii {pfi.clubs_keys.get(club[0])[1]}"


def create_output(user_query):
    """
    Funkcja, która wywołuje wszystkie powyższe funkcje w zależności od zapytania. Jest wywoływana w metodzie main.
    :param user_query: Niesparsowane i niepodzielone zapytanie użytkownika.
    :return: fraza będąca odpowiedzią na zapytanie.
    """
    split_query = pfi.query_splitting(user_query)       # podzielenie zapytania na listę słów
    keywords = pfi.parsing_from_input(split_query)      # zakodowanie listy słów według słownika słów kluczowych
    if "kto" in keywords:
        return search_kto(keywords)
    if "ilu" in keywords:
        return search_ilu(keywords)
    if "ile" in keywords:
        return search_ile(keywords)
    if "w" in keywords[0] and "partia" in keywords:
        return search_w(keywords, split_query)
    return "Nie rozumiem"
