
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

        # Nodes DataFrame Functions
        nodet = datetime.datetime.now()
        nodes_df = create_nodes_df(parser_lists[0])
        nodetend = datetime.datetime.now() - nodet

        print("\nDisplay Nodes Dataframe: \n")
        print(nodes_df)
        print("\n")


        nodes_df_lines = nodes_df_lines(parser_lists[0])
        print("\nDisplay Nodes Dataframe (with duplicates): \n")
        print(nodes_df_lines)
        print("\n")


        # Nets DataFrame Functions
        nett = datetime.datetime.now()
        nets_df = create_nets_df(parser_lists[1], nodes_df)
        # nets_df = create_nets_df(parser_lists[1], nodes_df_lines)
        nettend = datetime.datetime.now() - nett

        print("\nDisplay Nets Dataframe: \n")
        print(nets_df)
        print("\n")

        # Rows DataFrame Functions
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
        biggest_net_based_on_size(nets_df, nodes_df)
        smallest_net_based_on_size(nets_df, nodes_df)
        mean_net_based_on_size(nets_df, nodes_df)
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

        main_end = datetime.datetime.now() - main_time

        print("Times: ")
        lists_to_df_time = nodetend + nettend + rowtend + dtend
        print("Parser time: ", end_time)
        print("Convert Lists to DFs time: ", lists_to_df_time)
        print("Parser time + conversions to df: ", end_time + lists_to_df_time)
        print("create node_df: ", nodetend)
        print("create net_df: ", nettend)
        print("create row_df: ", rowtend)
        print("create design_df: ", dtend)
        print("Whole main runtime: ", main_end)


        """
        aa1 = datetime.datetime.now()
        find_min_max_on_nets_df2(nodes_df, nets_df)
        aa1end = datetime.datetime.now() - aa1

        aa2 = datetime.datetime.now()
        find_min_max_on_nets_df(nodes_df, nets_df)
        aa2end = datetime.datetime.now() - aa2
    
        print("\nFind min/max of nets with DFs: ", aa2end)
        print("\nFind min/max of nets with DFs(new way): ", aa1end)
        """

        # allocation_of_non_terminal_node_sizes(nodes_df)

        # allocation_of_net_sizes(nets_df)
        # allocation_of_net_sizes_based_on_nodes(nets_df)

        # allocation_of_cells_on_each_row(rows_df)
        # allocation_of_row_densities(rows_df)
        # allocation_of_row_spaces(rows_df)

        # Export to excel/csv
        # nodes_df.to_csv('PythonExport.csv', sep=',')
        # nodes_df.to_excel("output.xlsx")

        # with pd.ExcelWriter('output.xlsx') as writer:
          #  nodes_df_lines.to_excel(writer, sheet_name='nodes_df')
            # nets_df.to_excel(writer, sheet_name='nets_df')
        #     rows_df.to_excel(writer, sheet_name='rows_df')
        #    design_df.to_excel(writer, sheet_name='design_df')

    else:
        pass

