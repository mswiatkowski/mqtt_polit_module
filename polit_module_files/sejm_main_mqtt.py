# coding=utf8
from src.voice_assistant_modules.va_module import VAModule
import search_engine as seng

"""
##################################################################################################

Ten plik zawiera metodę politModule() i służy do uruchomienia programu przy użyciu serwera mqtt.
Dostosowany został do podłączenia do serwera Voice Assistant napisanego przez Wojciecha Węgrzynka.

##################################################################################################
"""


def write_to_logs(query, output):
    """
    Funkjca służąca do zapisywania zapytań i odpowiedzi w pliku logs.txt.
    :param query: zapytanie, które pobierane jest z serwera mqtt (lub, w przypadku tego programy testowego,
    z inputu użytkownika.
    :param output: string, który wysyłany jest do serwera. Stanowi odpowiedź na zapytanie.
    :return: None.
    """
    from datetime import datetime, date
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    with open("logs.txt", "a") as log:
        log.write(f"{str(today)} {str(current_time)} \nZapytanie: {query} \nOdpowiedź: {output}\n \n \n")


class politModule(VAModule):
    @classmethod
    def get_id(cls):
        return "politics"

    def process_query(self, query: str) -> str:
        """
        Funkcja pozwalająca przetworzyć zapytanie.
        :return: odpowiedź na zapytanie użytkownika.
        """
        user_query = query  # Pobranie zapytania od użytkownika
        try:
            output_message = seng.create_output(user_query)  # Wysłanie zapytania do funkcji create_output
            # i stworzenie odpowiedzi
            # Poniżej, w zależności od wymagań serwera, odpowiedź może zostać zastąpiona wartością None
            if output_message is None:
                output_message = "Nie rozumiem"
        except IndexError:
            output_message = "Nie rozumiem"
        print(output_message)
        write_to_logs(user_query, output_message)  # Zapis do logów
        return output_message


if __name__ == '__main__':
    politModule.main()
