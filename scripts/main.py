
from functions import *
import datetime

if __name__ == "__main__":
    
    if verify_files():
        parser_lists = parser()
        print("\n")
        # parser_lists[0] = node_list
        # parser_lists[1] = nets_list
        # parser_lists[2] = row_list

        nodes_df = node_list_to_df(parser_lists[0])
        print("\nDisplay Nodes Dataframe: \n")
        print(nodes_df)

        nets_df = net_list_to_df(parser_lists[1])
        find_min_max_on_nets_df(nodes_df, nets_df)
        calculate_net_hpw(nets_df)
        calculate_net_size(nets_df)

        print("\nDisplay Nets Dataframe: \n")
        print(nets_df)

        rows_df = row_list_to_df(parser_lists[2])
        row_density(nodes_df, rows_df)
        print("\nDisplay Rows Dataframe: \n")
        print(rows_df)

        create_design_df(nodes_df, nets_df, rows_df)
        #number_of_non_terminal_nodes(dfs[0])
        #biggest_non_terminal_node(dfs[0])
        #smallest_non_terminal_node(dfs[0])
        #mean_size_non_terminal_nodes(dfs[0])

        #number_of_terminal_nodes(dfs[0])

        #number_of_nets(dfs[1])
        #biggest_net_based_on_nodes(dfs[1])
        #smallest_net_based_on_nodes(dfs[1])
        #mean_size_of_nets_based_on_nodes(dfs[1])

        #number_of_rows(dfs[2])
        #biggest_row(dfs[2])
        #smallest_row(dfs[2])
        #mean_num_of_nodes_on_rows(dfs[2])

        #design_half_perimeter_wirelength(dfs[1])
        #design_density(dfs[0], dfs[2])

        # biggest_net_based_on_size(dfs[1], dfs[0])

        #row_density(dfs[0], dfs[1], dfs[2])


        """
        for node in parser_lists[0]:
            print(node.display_node_corners())
        """
    else:
        pass
