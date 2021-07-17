
from functions import *
import datetime

if __name__ == "__main__":

    if verify_files():
        main_time = datetime.datetime.now()

        begin_time = datetime.datetime.now()
        parser_lists = parser()
        end_time = datetime.datetime.now() - begin_time
        print("\n")

        # parser_lists[0] = node_list
        # parser_lists[1] = nets_list
        # parser_lists[2] = row_list

        b2 = datetime.datetime.now()
        # Nodes DataFrame Functions
        nodet = datetime.datetime.now()
        nodes_df = create_nodes_df(parser_lists[0])
        nodetend = datetime.datetime.now() - nodet
        print("\nDisplay Nodes Dataframe: \n")
        print(nodes_df)
        print("\n")

        # Nets DataFrame Functions
        nett = datetime.datetime.now()
        nets_df = create_nets_df(parser_lists[1], nodes_df)
        nettend = datetime.datetime.now() - nett
        print("\nDisplay Nets Dataframe: \n")
        print(nets_df)
        print("\n")

        # Rows DataFrame Functions
        rowt = datetime.datetime.now()
        rows_df = create_rows_df(parser_lists[2], nodes_df)
        print("\nDisplay Rows Dataframe: \n")
        rowtend = datetime.datetime.now() - rowt
        print(rows_df)
        print("\n")

        # Design DataFrame Functions
        dt = datetime.datetime.now()
        design_df = create_design_df(nodes_df, nets_df, rows_df)
        dtend = datetime.datetime.now() - dt
        print("\nDisplay Designs Dataframe: \n")
        print(design_df)
        print("\n")
        e2 = datetime.datetime.now() - b2

        #nodes_df.to_csv('PythonExport.csv', sep=',')
        #nodes_df.to_excel("output.xlsx")


    #    with pd.ExcelWriter('output.xlsx') as writer:
     #       nodes_df.to_excel(writer, sheet_name='nodes_df')
      #      nets_df.to_excel(writer, sheet_name='nets_df')
       #     rows_df.to_excel(writer, sheet_name='rows_df')
        #    design_df.to_excel(writer, sheet_name='design_df')


        number_of_non_terminal_nodes(nodes_df)
        biggest_non_terminal_node(nodes_df)
        smallest_non_terminal_node(nodes_df)
        mean_size_non_terminal_nodes(nodes_df)
        number_of_terminal_nodes(nodes_df)

        print('\n')
        number_of_nets(nets_df)
        biggest_net_based_on_nodes(nets_df)
        smallest_net_based_on_nodes(nets_df)
        mean_size_of_nets_based_on_nodes(nets_df)
        print('\n')
        biggest_net_based_on_size(nets_df, nodes_df)
        smallest_net_based_on_size(nets_df, nodes_df)
        mean_net_based_on_size(nets_df, nodes_df)

        print('\n')
        number_of_rows(rows_df)
        biggest_row(rows_df)
        smallest_row(rows_df)
        mean_num_of_nodes_on_rows(rows_df)

        print('\n')
        calculate_design_half_perimeter_wirelength(nets_df)
        calculate_design_density(nodes_df, rows_df)

        print('\n')
        main_end = datetime.datetime.now() - main_time

        lists_to_df_time = nodetend + nettend + rowtend + dtend
        print("\nParser time: ", end_time)
        print("Convert Lists to DFs time: ", lists_to_df_time)
        print("Whole main runtime: ", main_end)
        print("Parser time + convertions to df: ", end_time + lists_to_df_time)
        print("create node_df: ", nodetend)
        print("create net_df: ", nettend)
        print("create row_df: ", rowtend)
        print("create design_df: ", dtend)
    else:
        pass

