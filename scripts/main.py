
from functions import *

if __name__ == "__main__":
    
    if verify_files():
        parser_lists = parser()
        dfs = lists_to_dataframes(parser_lists[0], parser_lists[1],
                                  parser_lists[2])

        # dfs[0] = nodes_df
        # dfs[1] = nets_df
        # dfs[2] = rows_df
        # dfs[3] = design_df

        print("\n")
        number_of_non_terminal_nodes(dfs[0])
        number_of_terminal_nodes(dfs[0])
        biggest_non_terminal_node(dfs[0])
        smallest_non_terminal_node(dfs[0])

    else:
        pass
