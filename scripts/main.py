
from functions import *

if __name__ == "__main__":
    
    if verify_files():
        parser_lists = parser()
        lists_to_dataframes(parser_lists[0], parser_lists[1], parser_lists[2])

    else:
        pass
