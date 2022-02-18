
from functions import *
import datetime

if __name__ == "__main__":

    if verify_files():
        main_time = datetime.datetime.now()

        begin_time = datetime.datetime.now()
        parser_lists = parser()
        end_time = datetime.datetime.now() - begin_time

        # parser_lists[0] -> node_list
        # parser_lists[1] -> nets_list
        # parser_lists[2] -> row_list

        # Nodes DataFrame
        nodet = datetime.datetime.now()
        nodes_df = create_nodes_df(parser_lists[0])
        nodetend = datetime.datetime.now() - nodet

        print("\nDisplay Nodes Dataframe: \n")
        print(nodes_df)
        print("\n")

        # Nets DataFrame
        nett = datetime.datetime.now()
        nets_df = create_nets_df(parser_lists[1], nodes_df)
        nettend = datetime.datetime.now() - nett

        print("\nDisplay Nets Dataframe: \n")
        print(nets_df)
        print("\n")

        # Rows DataFrame
        rowt = datetime.datetime.now()
        rows_df = create_rows_df(parser_lists[2], nodes_df)
        rowtend = datetime.datetime.now() - rowt

        print("\nDisplay Rows Dataframe: \n")
        print(rows_df)
        print("\n")

        # Design DataFrame Functions
        dt = datetime.datetime.now()
        design_df = create_design_df(nodes_df, nets_df, rows_df)
        dtend = datetime.datetime.now() - dt

        print("\nDisplay Designs Dataframe: \n")
        print(design_df)
        print("\n")

        # Nodes Functions
        number_of_non_terminal_nodes_time = datetime.datetime.now()
        number_of_non_terminal_nodes(nodes_df)
        number_of_non_terminal_nodes_time = datetime.datetime.now() - number_of_non_terminal_nodes_time

        biggest_non_terminal_node_time = datetime.datetime.now()
        biggest_non_terminal_node(nodes_df)
        biggest_non_terminal_node_time = datetime.datetime.now() - biggest_non_terminal_node_time

        smallest_non_terminal_node_time = datetime.datetime.now()
        smallest_non_terminal_node(nodes_df)
        smallest_non_terminal_node_time = datetime.datetime.now() - smallest_non_terminal_node_time

        mean_size_non_terminal_nodes_time = datetime.datetime.now()
        mean_size_non_terminal_nodes(nodes_df)
        mean_size_non_terminal_nodes_time = datetime.datetime.now() - mean_size_non_terminal_nodes_time

        number_of_terminal_nodes_time = datetime.datetime.now()
        number_of_terminal_nodes(nodes_df)
        number_of_terminal_nodes_time = datetime.datetime.now() - number_of_terminal_nodes_time

        print('\n')

        # Nets Functions
        number_of_nets_time = datetime.datetime.now()
        number_of_nets(nets_df)
        number_of_nets_time = datetime.datetime.now() - number_of_nets_time

        biggest_net_based_on_nodes_time = datetime.datetime.now()
        biggest_net_based_on_nodes(nets_df)
        biggest_net_based_on_nodes_time = datetime.datetime.now() - biggest_net_based_on_nodes_time

        smallest_net_based_on_nodes_time = datetime.datetime.now()
        smallest_net_based_on_nodes(nets_df)
        smallest_net_based_on_nodes_time = datetime.datetime.now() - smallest_net_based_on_nodes_time

        mean_size_of_nets_based_on_nodes_time = datetime.datetime.now()
        mean_size_of_nets_based_on_nodes(nets_df)
        mean_size_of_nets_based_on_nodes_time = datetime.datetime.now() - mean_size_of_nets_based_on_nodes_time

        print('\n')

        biggest_net_based_on_size_time = datetime.datetime.now()
        biggest_net_based_on_size(nets_df, nodes_df)
        biggest_net_based_on_size_time = datetime.datetime.now() - biggest_net_based_on_size_time

        smallest_net_based_on_size_time = datetime.datetime.now()
        smallest_net_based_on_size(nets_df, nodes_df)
        smallest_net_based_on_size_time = datetime.datetime.now() - smallest_net_based_on_size_time

        mean_net_based_on_size_time = datetime.datetime.now()
        mean_net_based_on_size(nets_df, nodes_df)
        mean_net_based_on_size_time = datetime.datetime.now() - mean_net_based_on_size_time

        print('\n')

        # Rows Functions

        number_of_rows_time = datetime.datetime.now()
        number_of_rows(rows_df)
        number_of_rows_time = datetime.datetime.now() - number_of_rows_time

        biggest_row_time = datetime.datetime.now()
        biggest_row(rows_df)
        biggest_row_time = datetime.datetime.now() - biggest_row_time

        smallest_row_time = datetime.datetime.now()
        smallest_row(rows_df)
        smallest_row_time = datetime.datetime.now() - smallest_row_time

        mean_num_of_nodes_on_rows_time = datetime.datetime.now()
        mean_num_of_nodes_on_rows(rows_df)
        mean_num_of_nodes_on_rows_time = datetime.datetime.now() - mean_num_of_nodes_on_rows_time

        print('\n')

        # Design Functions
        # design_df_half_perimeter_wirelength(nets_df)
        # design_df_density(nodes_df, rows_df)
        print('\n')

        main_end = datetime.datetime.now() - main_time

        allocation_of_non_terminal_node_sizes_time = datetime.datetime.now()
        allocation_of_non_terminal_node_sizes(nodes_df)
        allocation_of_non_terminal_node_sizes_time = datetime.datetime.now() - allocation_of_non_terminal_node_sizes_time

        allocation_of_net_sizes_time = datetime.datetime.now()
        allocation_of_net_sizes(nets_df)
        allocation_of_net_sizes_time = datetime.datetime.now()  - allocation_of_net_sizes_time

        allocation_of_net_sizes_based_on_nodes_time = datetime.datetime.now()
        allocation_of_net_sizes_based_on_nodes(nets_df)
        allocation_of_net_sizes_based_on_nodes_time = datetime.datetime.now() - allocation_of_net_sizes_based_on_nodes_time

        allocation_of_cells_on_each_row_time = datetime.datetime.now()
        allocation_of_cells_on_each_row(rows_df)
        allocation_of_cells_on_each_row_time = datetime.datetime.now() - allocation_of_cells_on_each_row_time

        allocation_of_row_densities_time = datetime.datetime.now()
        allocation_of_row_densities(rows_df)
        allocation_of_row_densities_time = datetime.datetime.now() - allocation_of_row_densities_time

        # allocation_of_row_spaces(rows_df)


        # parser_lists[0] -> node_list
        # parser_lists[1] -> nets_list
        # parser_lists[2] -> row_list

        print("\n******************************\n")
        print("Times: ")
        calculate_times(parser_lists[0], parser_lists[1], parser_lists[2])

        print("\n")
        lists_to_df_time = nodetend + nettend + rowtend + dtend
        print("Parser time: ", end_time)
        print("Convert Lists to DFs time: ", lists_to_df_time)
        print("Parser time + conversions to df: ", end_time + lists_to_df_time)
        print("create node_df: ", nodetend)
        print("create net_df: ", nettend)
        print("create row_df: ", rowtend)
        print("create design_df: ", dtend)
        print("Whole main runtime: ", main_end)

        # Printing times
        print("\nnumber_of_non_terminal_nodes_time: ", number_of_non_terminal_nodes_time)
        print("biggest_non_terminal_node_time: ", biggest_non_terminal_node_time)
        print("smallest_non_terminal_node_time: ", smallest_non_terminal_node_time)
        print("mean_size_non_terminal_nodes_time: ", mean_size_non_terminal_nodes_time)
        print("number_of_terminal_nodes_time: ", number_of_terminal_nodes_time)

        print("\nnumber_of_nets_time: ", number_of_nets_time)
        print("biggest_net_based_on_nodes_time: ", biggest_net_based_on_nodes_time)
        print("smallest_net_based_on_nodes_time: ", smallest_net_based_on_nodes_time)
        print("mean_size_of_nets_based_on_nodes_time: ", mean_size_of_nets_based_on_nodes_time)

        print("biggest_net_based_on_size_time: ", biggest_net_based_on_size_time)
        print("smallest_net_based_on_size_time: ", smallest_net_based_on_size_time)
        print("mean_net_based_on_size_time: ", mean_net_based_on_size_time)

        print("\nnumber_of_rows_time: ", number_of_rows_time)
        print("biggest_row_time: ", biggest_row_time)
        print("smallest_row_time: ", smallest_row_time)
        print("mean_num_of_nodes_on_rows_time: ", mean_num_of_nodes_on_rows_time)

        print("\nGRAPH TIMES: \n")
        print("allocation_of_non_terminal_node_sizes_time: ", allocation_of_non_terminal_node_sizes_time)
        print("allocation_of_net_sizes_time: ", allocation_of_net_sizes_time)
        print("allocation_of_net_sizes_based_on_nodes_time: ", allocation_of_net_sizes_based_on_nodes_time)
        print("allocation_of_cells_on_each_row_time: ", allocation_of_cells_on_each_row_time)
        print("allocation_of_row_densities_time: ", allocation_of_row_densities_time)

        # with pd.ExcelWriter('output.xlsx') as writer:
        #     nodes_df.to_excel(writer, sheet_name='nodes_df')
        #     nets_df.to_excel(writer, sheet_name='nets_df')
        #     rows_df.to_excel(writer, sheet_name='rows_df')
        #     design_df.to_excel(writer, sheet_name='design_df')

    else:
        pass

