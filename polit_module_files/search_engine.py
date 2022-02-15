import csv
import parse_from_input

keywords = parse_from_input.input_words


################################################################################


def choose_engine(keyword):
    if keyword[0] == 'kto':
        search_politicians(keyword[2])


################################################################################


def search_politicians(keyword):
    with open('politicians.csv', 'r') as polits:
        reader = csv.reader(polits)
        for row in reader:
            if keyword in row:
                print(f'{keyword} to {row[0]} {row[1]}')


################################################################################


def search_parties(keyword):
    pass


################################################################################


output_message = choose_engine(keywords)