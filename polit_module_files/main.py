# coding=utf8
#from src.voice_assistant_modules.va_module import VAModule
import parse_from_input as pfi
import search_engine as seng

# user_query = ""
# class politModule(VAModule):
#     @classmethod
#     def get_id(cls):
#         return "politics"
#
#     def process_query(selfself, query: str) -> str:
#         user_query = query
#         return query

def write_to_logs(query, output):
    from datetime import datetime, date
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    with open("logs.txt", "a") as log:
        log.write(f"{str(today)} {str(current_time)} \nZapytanie: {query} \nOdpowiedź: {output}\n \n \n")


if __name__ == '__main__':
    # politModule.main()
    """TEST:"""
    user_query = input("usr_query>>> ").lower()
    try:
        output_message = seng.create_output(user_query)
    except IndexError:
        output_message = "Nie rozumiem"
    print(output_message)
    write_to_logs(user_query, output_message)