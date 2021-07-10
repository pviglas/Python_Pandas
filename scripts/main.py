
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


        with pd.ExcelWriter('output.xlsx') as writer:
            nodes_df.to_excel(writer, sheet_name='nodes_df')
            nets_df.to_excel(writer, sheet_name='nets_df')
            rows_df.to_excel(writer, sheet_name='rows_df')
            design_df.to_excel(writer, sheet_name='design_df')


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
        print('\n')
        main_end = datetime.datetime.now() - main_time

        print("\nParser time: ", end_time)
        print("Convert Lists to DFs time: ", e2)
        print("Whole main runtime: ", main_end)
        print("Add parser time + convertions: ", end_time + e2)
        print("create node_df: ", nodetend)
        print("create net_df: ", nettend)
        print("create row_df: ", rowtend)
        print("create design_df: ", dtend)
    else:
        pass

