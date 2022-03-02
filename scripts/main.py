# Viglas Panagiotis

from functions import *

if __name__ == "__main__":

    if verify_files():

        parser_lists = parser()

        # parser_lists[0] -> node_list
        # parser_lists[1] -> nets_list
        # parser_lists[2] -> row_list

        # Nodes DataFrame
        nodes_df = create_nodes_df(parser_lists[0])

        print("\nDisplay Nodes Dataframe: \n")
        print(nodes_df)
        print("\n")

        # Nets DataFrame
        nets_df = create_nets_df(parser_lists[1])

        print("\nDisplay Nets Dataframe: \n")
        print(nets_df)
        print("\n")

        # Rows DataFrame
        rows_df = create_rows_df(parser_lists[2], nodes_df)

        print("\nDisplay Rows Dataframe: \n")
        print(rows_df)
        print("\n")

        # Design DataFrame Functions
        design_df = create_design_df(nodes_df, nets_df, rows_df)

        print("\nDisplay Designs Dataframe: \n")
        print(design_df)
        print("\n")

        # Nodes Functions
        number_of_non_terminal_nodes(nodes_df)
        biggest_non_terminal_node(nodes_df)
        smallest_non_terminal_node(nodes_df)
        mean_size_non_terminal_nodes(nodes_df)
        number_of_terminal_nodes(nodes_df)
        print('\n')

        # Nets Functions
        number_of_nets(nets_df)
        biggest_net_based_on_nodes(nets_df)
        smallest_net_based_on_nodes(nets_df)
        mean_size_of_nets_based_on_nodes(nets_df)
        print('\n')

        biggest_net_based_on_size(nets_df)
        smallest_net_based_on_size(nets_df)
        mean_net_based_on_size(nets_df)
        print('\n')

        # Rows Functions
        number_of_rows(rows_df)
        biggest_row(rows_df)
        smallest_row(rows_df)
        mean_num_of_nodes_on_rows(rows_df)
        print('\n')

        # Design Functions
        # design_df_half_perimeter_wirelength(nets_df)
        # design_df_density(nodes_df, rows_df)
        print('\n')

        allocation_of_non_terminal_node_sizes(nodes_df)
        allocation_of_net_sizes(nets_df)
        allocation_of_net_sizes_based_on_nodes(nets_df)
        allocation_of_cells_on_each_row(rows_df)
        allocation_of_row_densities(rows_df)
        allocation_of_row_spaces(rows_df)

        # Save to excel file
        # with pd.ExcelWriter('output.xlsx') as writer:
        #     nodes_df.to_excel(writer, sheet_name='nodes_df')
        #     nets_df.to_excel(writer, sheet_name='nets_df')
        #     rows_df.to_excel(writer, sheet_name='rows_df')
        #     design_df.to_excel(writer, sheet_name='design_df')

    else:
        pass

