import csv
import parse_from_input

keywords = parse_from_input.input_words


################################################################################

def search_politicians(keyword):
    with open('politicians.csv', 'r') as polits:
        reader = csv.reader(polits)
        for row in reader:
            if keyword in row:
                print(f'{keyword} Polski to {row[1]} {row[0]}')


def count_sejm(keyword):
    count = 0
    with open('sejm.csv', 'r') as sejm:
        reader = csv.reader(sejm)
        for row in reader:
            if keyword in row:
                count += 1
    print(count)
    return count



def check_hierarchy():
    if "kto" in keywords:
        if "prezydent" in keywords:
            search_politicians("prezydent")
        if "rpo" in keywords:
            search_politicians("rzecznik praw obywatelskich")
    if "ilu" in keywords:
        if "posel" in keywords:
            for word in keywords:
                if word in parse_from_input.clubs_keys.keys():
                    if word == "niezrzeszony":
                        print(f"Posłów niezrzeszonych jest w sejmie {count_sejm(word)}")
                    else:
                        print(f"{word} ma w sejmie {count_sejm(word)} posłów")
    if "ile" in keywords:
        pass


check_hierarchy()



# output_message = choose_engine(keywords)