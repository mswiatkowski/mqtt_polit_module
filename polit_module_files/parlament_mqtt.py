# coding=utf8
from src.voice_assistant_modules.va_module import VAModule


"""
##################################################################################################

Ten plik zawiera metodę politModule() i służy do uruchomienia programu przy użyciu serwera mqtt.
Dostosowany został do podłączenia do serwera Voice Assistant napisanego przez Wojciech Węgrzynka.

##################################################################################################
"""

class politModule(VAModule):
    @classmethod
    def get_id(cls):
        return "politics"

    def process_query(selfself, query: str) -> str:
        user_query = query
        return query


if __name__ == '__main__':
    politModule.main()
