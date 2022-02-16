import csv
import parse_from_input

# keywords = main.query_decoded
firstnames = []
lastnames = []
with open("sejm.csv", "r", encoding="utf-8") as sejm:
    sejm = csv.reader(sejm)
    for row in sejm:
        firstnames.append(row[1])
        lastnames.append(row[0])

################################################################################

def search_politicians(keyword):
    with open('politicians.csv', 'r', encoding="utf-8") as polits:
        reader = csv.reader(polits)
        for row in reader:
            if keyword in row:
                return f'{keyword} Polski to {row[1]} {row[0]}'


def count_sejm(keyword="", party=""):
    count = 0
    with open('sejm.csv', 'r', encoding="utf-8") as sejm:
        reader = csv.reader(sejm)
        for row in reader:
            if keyword in row and party == "":
                count += 1
            elif keyword in row and party in row:
                count += 1
    print(count)
    return count

def search_kto(keywords):
    if "kto" in keywords:
        if "prezydent" in keywords:
            return search_politicians("prezydent")
        if "rpo" in keywords:
            return search_politicians("rzecznik praw obywatelskich")


def search_ilu(keywords):
    if "ilu" in keywords:
        if "posel" in keywords:
            for word in keywords:
                if word in parse_from_input.clubs_keys.keys():
                    if word == "niezrzeszony":
                        return f"Posłów niezrzeszonych jest w sejmie {count_sejm(word)}"
                    else:
                        return f"{parse_from_input.clubs_keys.get(word)[1]} ma w sejmie {count_sejm(word)} posłów"
            return f"posłów w sejmie jest {count_sejm()}"
        if "prezydent" in keywords:
            return "prezydent jest tylko jeden"
        if "premier" in keywords:
            return "premier jest tylko jeden"
        if "m" in keywords:
            for word in keywords:
                if word in parse_from_input.clubs_keys.keys() and word != "partia":
                    return f"mężczyzn w partii {word} jest {count_sejm('m', word)}"
            return f"mężczyzn jest w sejmie {count_sejm('m')}"


def search_ile(keywords):
    if "ile" in keywords:
        if "k" in keywords:
            for word in keywords:
                if word in parse_from_input.clubs_keys.keys() and word != "partia":
                    return f"kobiet w partii {word} jest {count_sejm('k', word)}"
            return f"kobiet jest w sejmie {count_sejm('k')}"


def search_w(keywords, split_query):
    if "w" in keywords[0]:
        list_of_lastnames = []
        list_of_firstnames = []
        club = []
        print(split_query)

        for name in split_query[1:]:
            with open('sejm.csv', 'r', encoding="utf-8") as sejm:
                sejm = csv.reader(sejm)

                for row in sejm:
                    if name in row[0] and name in lastnames:
                        list_of_lastnames.append(name)
                        club.append(row[2])
                    if name in row[1] and name in firstnames:
                        club.append(row[2])
                        list_of_firstnames.append(name)


        print(list_of_firstnames)

        if len(list_of_lastnames) > 1 and len(list_of_firstnames) == 0:
            return "Więcej niż jedna osoba się tak nazywa"
        elif len(list_of_lastnames) == 0 and len(list_of_firstnames) > 1:
            return "Więcej niż jedna osoba ma tak na imię"
        elif len(list_of_lastnames) == 1 and len(list_of_firstnames) == 0:
            return f"{list_of_lastnames[0]} jest w partii {club[0]}"
        elif len(list_of_firstnames) == 1 and len(list_of_lastnames) == 0:
            return f"{list_of_firstnames[0]} jest w partii {club[0]}"
        elif len(list_of_firstnames) == 0 and len(list_of_lastnames) == 0:
            return "w żadnej partii nie ma takiej osoby"
        else:
            return f"{list_of_firstnames[0]} {list_of_lastnames[0]} jest w partii {club[0]}"


def create_output(user_query):
    split_query = parse_from_input.query_splitting(user_query)
    keywords = parse_from_input.parsing_from_input(split_query)
    if "kto" in keywords:
        return search_kto(keywords)
    if "ilu" in keywords:
        return search_ilu(keywords)
    if "ile" in keywords:
        return search_ile(keywords)
    if "w" in keywords[0] and "partia" in keywords:
        return search_w(keywords, split_query)
    return "Nie rozumiem"

    #TODO: upewnić się, że do polityka będzie dobra partia
