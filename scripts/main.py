
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
        biggest_non_terminal_node(dfs[0])
        smallest_non_terminal_node(dfs[0])
        mean_size_non_terminal_nodes(dfs[0])

        number_of_terminal_nodes(dfs[0])

        number_of_nets(dfs[1])
        biggest_net_based_on_nodes(dfs[1])
        smallest_net_based_on_nodes(dfs[1])
        mean_size_of_nets_based_on_nodes(dfs[1])

        number_of_rows(dfs[2])
        biggest_row(dfs[2])
        smallest_row(dfs[2])
        mean_num_of_nodes_on_rows(dfs[2])

        design_half_perimeter_wirelength(dfs[1])
        design_density(dfs[0], dfs[2])

        # biggest_net_based_on_size(dfs[1], dfs[0])

        row_density(dfs[0], dfs[1], dfs[2])
        #net_size_and_hpw(dfs[0], dfs[1])


    else:
        pass
