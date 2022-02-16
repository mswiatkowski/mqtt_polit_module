#from src.voice_assistant_modules.va_module import VAModule
import parse_from_input as pfi
import search_engine as seng

user_query = ""

# class politModule(VAModule):
#     @classmethod
#     def get_id(cls):
#         return "politics"
#
#     def process_query(selfself, query: str) -> str:
#         user_query = query
#         return query


if __name__ == '__main__':
    # politModule.main()
    """TEST:"""
    user_query = input("usr_query>>> ").lower()
    query_decoded = pfi.query_processing(user_query)
    try:
        output_message = seng.create_output(query_decoded)
    except IndexError:
        output_message = "Nie rozumiem"
    print(output_message)