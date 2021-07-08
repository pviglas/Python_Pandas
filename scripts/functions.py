# Parsing bookshelf formatted file

""""   Set the current working dir infos   """

import os
import pandas as pd

"""
folderName = "ibm01_mpl6_placed_and_nettetris_legalized"
fileName = "ibm01"

os.chdir('C:\\Users\\root\\Desktop\\Python_Pandas\\docs\\ISPD\\{}'.format(
    folderName))

"""
folderName = "design"
fileName = "design"
os.chdir(
    'C:\\Users\\root\\Desktop\\Python_Pandas\\docs\\{}'.format(folderName))



""""    Classes    """


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return " (" + str(self.x) + " , " + str(self.y) + ") "


class Node:

    def __init__(self, node_name, node_width, node_height, node_type,
                 node_x=0, node_y=0):
        self.node_name = node_name
        self.node_width = node_width
        self.node_height = node_height
        self.node_type = node_type
        self.node_x = node_x  # Lower Left Corner - x Coordinate
        self.node_y = node_y  # Lower Left Corner - y Coordinate
        self.lower_left_corner = Point(None, None)
        self.lower_right_corner = Point(None, None)
        self.upper_left_corner = Point(None, None)
        self.upper_right_corner = Point(None, None)

        self.node_nets = []  # net_names that this node are part of #todo net object if needed
        self.node_row = Row(None, None, None, None, None)

    # update the Coordinates x & y
    def set_x_y(self, node_x, node_y):
        self.node_x = node_x
        self.node_y = node_y

    def set_row(self, row):
        self.node_row = row

    def append_net(self, net_name):
        self.node_nets.append(str(net_name))

    # calculate the coordinates of the 4-corners of the node
    # Terminals are dots, they do not have corners
    def set_points(self, x_min, x_max, y_min, y_max):
        if self.node_type == "Non_Terminal":
            self.lower_left_corner = Point(x_min, y_min)
            self.lower_right_corner = Point(x_max, y_min)
            self.upper_left_corner = Point(x_min, y_max)
            self.upper_right_corner = Point(x_max, y_max)

    def display_node_corners(self):
        print("\nNode name: " + str(self.node_name)
              + "\nLower Left Corner: " + str(self.lower_left_corner)
              + "\nLower Right Corner: " + str(self.lower_right_corner)
              + "\nUpper Left Corner: " + str(self.upper_left_corner)
              + "\nUpper Right Corner: " + str(self.upper_right_corner))

    def display_node_row(self):
        print("\nNode " + str(self.node_name)
              + " is placed in row: " + str(self.node_row.row_name))

    def display_node_nets(self):
        print("\nNode " + str(self.node_name) + " belongs to the net(s):  ")
        for net in self.node_nets:
            print(net, end=" ")

    def to_dict(self):
        return {
            'Node_name': self.node_name,
            'Width': self.node_width,
            'Height': self.node_height,
            'Coordinate_x_min': self.node_x,
            'Coordinate_y_min': self.node_y,
            'Row_number': self.node_row.row_name,
            'Nets': self.node_nets,
            'Type': self.node_type,
            'list_size': self.node_width * self.node_height
        }

    def __str__(self):
        return (str(self.node_name) + " " + str(self.node_width) + " " +
                str(self.node_height) + " " + str(self.node_type) + " " +
                str(self.node_x) + " " + str(self.node_y))


class Net:

    def __init__(self, net_name, net_degree):
        self.net_name = net_name
        self.net_degree = net_degree
        self.net_nodes = []  # list of nodes for the current net
        self.net_rows = []  # list of rows that this net belongs to
        self.x_min = None
        self.x_max = None
        self.y_min = None
        self.y_max = None
        self.wirelength = None
        self.net_size = None
        self.internal_nodes = []
        self.external_nodes = set()

    def append_node(self, node):
        self.net_nodes.append(node)

    def append_row(self, row):
        self.net_rows.append(row)

    def find_coordinates_of_net(self):
        start = 0
        temp_internal_node_0 = Node(None, None, None, None)
        temp_internal_node_1 = Node(None, None, None, None)
        temp_internal_node_2 = Node(None, None, None, None)
        temp_internal_node_3 = Node(None, None, None, None)

        for node in self.net_nodes:
            start += 1

            if start == 1 and node.node_type == "Non_Terminal":
                self.x_min = node.lower_left_corner.x
                self.x_max = node.lower_right_corner.x
                self.y_min = node.lower_left_corner.y
                self.y_max = node.upper_right_corner.y

                temp_internal_node_0 = node
                temp_internal_node_1 = node
                temp_internal_node_2 = node
                temp_internal_node_3 = node

            elif start == 1 and node.node_type == "Terminal":
                self.x_min = node.node_x
                self.x_max = node.node_x
                self.y_min = node.node_y
                self.y_max = node.node_y

                temp_internal_node_0 = node
                temp_internal_node_1 = node
                temp_internal_node_2 = node
                temp_internal_node_3 = node

            else:
                if node.node_type == "Non_Terminal":
                    if node.lower_left_corner.x < self.x_min:
                        self.x_min = node.lower_left_corner.x
                        temp_internal_node_0 = node
                    if node.lower_right_corner.x > self.x_max:
                        self.x_max = node.lower_right_corner.x
                        temp_internal_node_1 = node
                    if node.lower_left_corner.y < self.y_min:
                        self.y_min = node.lower_left_corner.y
                        temp_internal_node_2 = node
                    if node.upper_right_corner.y > self.y_max:
                        self.y_max = node.upper_right_corner.y
                        temp_internal_node_3 = node
                else:
                    if node.node_x < self.x_min:
                        self.x_min = node.node_x
                        temp_internal_node_0 = node
                    if node.node_x > self.x_max:
                        self.x_max = node.node_x
                        temp_internal_node_1 = node
                    if node.node_y < self.y_min:
                        self.y_min = node.node_y
                        temp_internal_node_2 = node
                    if node.node_y > self.y_max:
                        self.y_max = node.node_y
                        temp_internal_node_3 = node
        """
        for node in self.net_nodes:
            if (node != temp_internal_node_0 and node != temp_internal_node_1
                    and node != temp_internal_node_2
                    and node != temp_internal_node_3):
                self.internal_nodes.append(node)
            else:
                self.external_nodes.add(node)
        """

        for node in self.net_nodes:
            if node.node_type == "Non_Terminal":
                if(node.lower_left_corner.x == self.x_min or
                        node.lower_right_corner.x == self.x_max or
                        node.lower_left_corner.y == self.y_min or
                        node.upper_right_corner.y == self.y_max):

                    self.external_nodes.add(node)

            elif node.node_type == "Terminal":
                if(node.node_x == self.x_min or
                        node.node_x == self.x_max or
                        node.node_y == self.y_min or
                        node.node_y == self.y_max):

                    self.external_nodes.add(node)
            else:
                self.internal_nodes.append(node)

    def calculate_net_wirelength(self):
        self.wirelength = (self.x_max - self.x_min) + (self.y_max - self.y_min)

    def calculate_net_size(self):
        self.net_size = (self.x_max - self.x_min) * (self.y_max - self.y_min)

    def display_net_nodes(self):
        print("\n" + str(self.net_name)
              + " has net_degree =  " + str(self.net_degree))
        print("Node(s) of this net: ")
        for node in self.net_nodes:
            print(node.node_name, end=" ")

    def display_net_internal_nodes(self):
        print("\nInternal Node(s) of " + str(self.net_name) + ":")
        if self.internal_nodes:
            for node in self.internal_nodes:
                print(node.node_name)
        else:
            print("None")

    def display_net_external_nodes(self):
        print("\nExternal Node(s) of " + str(self.net_name) + ":")
        for node in self.external_nodes:
            print(node.node_name)

    def display_net_rows(self):
        print("\nRow(s) of " + str(self.net_name) + ":")
        for row in self.net_rows:
            print(row.row_name, end=" ")

    def display_net_size(self):
        print(str(self.net_name) + " size = " + str(self.net_size))

    def display_net_wirelength(self):
        print(str(self.net_name) + " wirelength = " + str(self.wirelength))

    def to_dict(self):
        return {
            'Net_name': self.net_name,
            'Nodes': [node.node_name for node in self.net_nodes],
            'Rows': [row.row_name for row in self.net_rows],
            'Internal_nodes': [node.node_name for node in self.internal_nodes],
            'External_nodes': [node.node_name for node in self.external_nodes],
            'Half_Perimeter_Wirelength': self.wirelength,
            'Net_size': self.net_size,
            'x_min': self.x_min,
            'x_max': self.x_max,
            'y_min': self.y_min,
            'y_max': self.y_max
        }

    # not displaying the nodes that are part of the net
    def __str__(self):
        return str(self.net_name) + " " + str(self.net_degree)


class Row:

    def __init__(self, row_name, y_min, y_max, x_min, x_max):
        self.row_name = row_name
        self.y_min = y_min
        self.y_max = y_max
        self.x_min = x_min
        self.x_max = x_max
        self.row_nodes = []  # list of nodes that are placed in this row
        self.row_nets = set()  # set of nets that are part of this row
        self.lower_left_corner = Point(x_min, y_min)
        self.lower_right_corner = Point(x_max, y_min)
        self.upper_left_corner = Point(x_min, y_max)
        self.upper_right_corner = Point(x_max, y_max)
        self.density = None

    def append_node(self, node):
        if node.node_type == "Non_Terminal":
            self.row_nodes.append(node)

    def append_net(self, net):
        self.row_nets.add(net)

    def calculate_row_density(self):
        nodes_area = 0
        row_area = (self.x_max - self.x_min) * (self.y_max - self.y_min)
        for node in self.row_nodes:
            nodes_area += (node.node_height * node.node_width)

        self.density = int((nodes_area / row_area) * 100)

    def display_row_nets(self):
        print("\nNet(s) of " + str(self.row_name) + ":")
        for net in self.row_nets:
            print(net.net_name, end=" ")

    def display_row_nodes(self):
        print("\nNode(s) of " + str(self.row_name) + ":")
        for node in self.row_nodes:
            print(node.node_name + " " + node.node_type, end=" ")

    def display_row_density(self):
        print("\n" + str(self.row_name) + " has density = "
              + str(self.density) + "%")

    def to_dict(self):
        return {
            'Row_name': self.row_name,
            'Density': self.density,
            'Cells': [node.node_name for node in self.row_nodes],
            'Nets': [net.net_name for net in self.row_nets],
            'Coordinate_x_min': self.x_min,
            'Coordinate_x_max': self.x_max,
            'Coordinate_y_min': self.y_min,
            'Coordinate_y_max': self.y_max,
        }

    def __str__(self):
        return (str(self.row_name) + " - y_min: "
                + str(self.y_min) + " - y_max: "
                + str(self.y_max) + " - x_min: "
                + str(self.x_min) + " - x_max: " + str(self.x_max))


class Design:

    def __init__(self, num_of_cells, num_of_terminals, num_of_nets):
        self.density = None
        self.num_of_cells = num_of_cells
        self.num_of_terminals = num_of_terminals
        self.num_of_nets = num_of_nets
        self.width = None
        self.height = None
        self.total_area = None
        self.total_cell_area = None

    def calculate_design_width_height(self):
        pass

    def calculate_design_density(self):
        pass

    def calculate_design_total_area(self):
        pass

    def calculate_design_total_cell_area(self, node_list):
        total_cell_area = 0
        for node in node_list:
            pass

    def __str__(self):
        return (str(self.density) + " " + str(self.num_of_cells)
                + " " + str(self.num_of_terminals)
                + " " + str(self.num_of_nets)
                + " " + str(self.width) + " " + str(self.height)
                + " " + str(self.total_area) + " " + str(self.total_cell_area))


""""    Functions   """


def exit_message():
    import time

    time.sleep(1)
    print("Shutting down", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".", end="")


def verify_files():
    flag = True

    extensions_tuple = [".aux", ".nets", ".nodes", ".pl", ".scl", ".wts"]

    extensions_list = []
    name = None

    for f in os.listdir():
        name, extensions = os.path.splitext(f)
        extensions_list.append(extensions)

    # Sort them both, in order to compare them
    extensions_tuple.sort()
    extensions_list.sort()

    fixed_length = len(extensions_tuple)
    read_length = len(extensions_list)

    if extensions_tuple == extensions_list:

        if os.stat('{}.aux'.format(name)).st_size == 0:
            flag = False
            print(".aux file is empty")

        if os.stat('{}.nodes'.format(name)).st_size == 0:
            flag = False
            print(".nodes file is empty")

        if os.stat('{}.scl'.format(name)).st_size == 0:
            flag = False
            print(".scl file is empty")

        if os.stat('{}.pl'.format(name)).st_size == 0:
            flag = False
            print(".pl file is empty")

        if os.stat('{}.nets'.format(name)).st_size == 0:
            flag = False
            print(".scl file is empty")

        if os.stat('{}.wts'.format(name)).st_size == 0:
            flag = False
            print(".wts file is empty")

        print("\n")

        if flag is False:
            exit_message()
        else:
            print("\n- All files are verified!")

    elif fixed_length > read_length:
        flag = False
        print("- Some files are missing.\n")
        exit_message()

    else:
        flag = False
        print("- There are more files!\n")
        exit_message()

    return flag


def parser():  # parsing the whole circuit

    """               Start of Parse .nodes               """

    file = open("{}.nodes".format(fileName))
    lines = file.readlines()

    saved = 0
    node_list = []  # List of all nodes for the current circuit
    number_of_nodes = None
    number_of_terminals = None
    number_of_nets = None

    # Locate NumNodes + NumTerminals
    for i in range(len(lines)):
        # .upper everything cause of insensitive chars
        temp_parsing = lines[i].strip(" ,.\n#:").upper()

        # Locate NumNodes
        if temp_parsing.find("NUMNODES") != -1:
            point = temp_parsing.find("NUMNODES")
            length = len("NUMNODES")

            number_of_nodes = temp_parsing[point + length:]
            number_of_nodes = number_of_nodes.strip(": ")

            number_of_nodes = int(number_of_nodes)

        # Locate NumTerminals
        if temp_parsing.find("NUMTERMINALS") != -1:
            point = temp_parsing.find("NUMTERMINALS")
            length = len("NUMTERMINALS")

            number_of_terminals = temp_parsing[point + length:]
            number_of_terminals = number_of_terminals.strip(": ")

            number_of_terminals = int(number_of_terminals)

            # Starting point for the 2nd for, +1 for the next line.
            saved = i + 1
            break

    # Parsing the Nodes
    for j in range(saved, len(lines)):

        temp = lines[j].strip("\t,.\n#: ")
        temp = temp.split()

        node_name = temp[0]
        node_width = int(temp[1])
        node_height = int(temp[2])

        if len(temp) == 3:  # len == 3 -> Non_Terminal
            node_type = "Non_Terminal"
        elif len(temp) == 4:  # len == 4 -> Terminal
            node_type = "Terminal"
        else:
            # Length is not 3 or 4 - Modified file
            print("Error. File is modified!")
            node_type = "Error. File is modified!"

        new_node = Node(node_name, node_width, node_height, node_type)
        node_list.append(new_node)  # node_x,node_y not found yet

    file.close()  # Close .nodes file

    """               End of Parse .nodes               """

    """               Start of Parse .pl               """

    file = open("{}.pl".format(fileName))
    lines = file.readlines()

    # Skip first 4 lines - comments
    for i in range(4, len(lines)):
        temp_parsing = lines[i].strip()
        temp_parsing = temp_parsing.split()  # temp_parsing type = list

        node_name = temp_parsing[0]
        node_x = int(temp_parsing[1])  # Lower Left Corner x Coordinate
        node_y = int(temp_parsing[2])  # Lower Left Corner y Coordinate

        # match the node_names and
        # update the node_x,node_y according to their coordinates
        for node in node_list:
            if node.node_name == node_name:
                node.set_x_y(node_x, node_y)
                if node.node_type == "Non_Terminal":
                    node.set_points(node_x, node_x + node.node_width,
                                    node_y, node_y + node.node_height)

    file.close()  # Close .pl file
    """               End of Parse .pl               """

    """               Start of Parse .nets               """

    file = open("{}.nets".format(fileName))
    lines = file.readlines()

    saved = 0  # saving pointers that are used for parsing
    net_list = []  # List of all nets for the current circuit

    # Locate NumNets
    for i in range(len(lines)):

        temp_parsing = lines[i].strip(" ,.\n#:").upper()

        # Parse NumNets
        if temp_parsing.find("NUMNETS") != -1:
            point = temp_parsing.find("NUMNETS")
            length = len("NUMNETS")

            number_of_nets = temp_parsing[point + length:]
            number_of_nets = number_of_nets.strip(": ")

            number_of_nets = int(number_of_nets)

            saved = i
            break

    # Locating all NetDegree's
    name_counter = -1  # counter for names of the Nets
    for i in range(saved, len(lines)):

        temp_parsing = lines[i].strip(" ,.\n#:").upper()

        # Locate NetDegree
        if temp_parsing.find("NETDEGREE") != -1:

            name_counter += 1  # +1 for the next Net Name

            temp_parsing = temp_parsing.replace(":", " ")
            temp_parsing = temp_parsing.split()

            net_degree = int(temp_parsing[1])
            net_name = "net{}".format(name_counter)

            # Read the "netDegree" number of lines of each Net
            # netDegree+1 because "range" stops at (max - 1)
            # Starting from 1, to skip the " NetDegree : x " line

            new_net = Net(net_name, net_degree)

            for j in range(1, net_degree + 1):
                next_line = lines[i + j].split()  # contains node name & more
                current_node = str(next_line[0])  # parse only the node name

                # match the node name, to the node object
                for node in node_list:
                    if node.node_name == current_node:
                        new_net.append_node(node)

                # new_net.append_node(current_node)   #it appends node name

                # find on which nets, the current_node belongs to
                # and then updating the net_list of the current_node
                # according to the matches
                for node in node_list:
                    if node.node_name == current_node:
                        node.append_net(new_net.net_name)

            new_net.find_coordinates_of_net()
            new_net.calculate_net_wirelength()
            new_net.calculate_net_size()
            net_list.append(new_net)  # add every net on the list of nets

    file.close()  # Close .nets file
    """               End of Parse .nets               """

    """               Start of Parse .scl               """

    file = open("{}.scl".format(fileName))
    lines = file.readlines()

    row_name = None
    row_coordinate = None
    row_sub = None
    row_numsites = None
    row_height = None

    row_list = []  # List of all rows for the current circuit

    name_counter = -1  # counter for name of the Rows
    for i in range(len(lines)):
        # .upper everything cause of insensitive chars
        temp_parsing = lines[i].strip(" ,.\n#:").upper()

        if temp_parsing.find("COREROW HORIZONTAL") != -1:
            name_counter += 1  # +1 for the next Row Name

            row_name = "row{}".format(name_counter)

            # Parse Row's Coordinate and check if Coordinate is at (i+1)
            # position
            # (i+1) = Coordinate
            # .upper everything cause of insensitive chars
            temp = lines[i + 1].strip(" ,.\n#:").upper()

            if temp.find("COORDINATE") != -1:

                point = temp.find("COORDINATE")
                length = len("COORDINATE")

                row_coordinate = temp[point + length:]
                row_coordinate = row_coordinate.strip(": ")

                # Lower Left Corner y coordinate of the row
                row_coordinate = int(row_coordinate)

            else:
                print("Error: File is modified.")

            # Parse Row's Height and check if Height is at (i+2) position
            # (i+2) = Height
            # .upper everything cause of insensitive chars
            temp = lines[i + 2].strip(" ,.\n#:").upper()

            if temp.find("HEIGHT") != -1:

                point = temp.find("HEIGHT")
                length = len("HEIGHT")

                row_height = temp[point + length:]
                row_height = row_height.strip(": ")
                row_height = int(row_height)

            else:
                print("Error: File is modified.")

            # Parse SubrowOrigin & Numsites & check if their position is
            # at (i+7)
            # (i+7) = SubrowOrigin + Numsites
            # .upper everything cause of insensitive chars
            temp = lines[i + 7].strip(" ,.\n#:").upper()

            if temp.find("SUBROWORIGIN") != -1:

                point = temp.find("SUBROWORIGIN")
                length = len("SUBROWORIGIN")

                row_sub = temp[point + length:]
                row_sub = row_sub.strip(": ")
                row_sub = row_sub.strip(" ,.\n#:").upper()

                if row_sub.find("NUMSITES") != -1:
                    point2 = row_sub.find("NUMSITES")

                    # filter and locate Numsites
                    row_numsites = row_sub[point2 + length:]
                    row_numsites = row_numsites.strip(": ")

                    # Lower Right Corner x Coordinate
                    row_numsites = int(row_numsites)

                    # filter and locate SubrowOrigin
                    row_sub = row_sub[:point2]
                    row_sub = int(row_sub)  # Lower Left Corner x Coordinate

            else:
                print("Error: File is modified.")

            # row_height + row_coordinate = y_max of each row
            new_row = Row(row_name, row_coordinate,
                          (row_height + row_coordinate), row_sub, row_numsites)

            row_list.append(new_row)  # add every row on the list of rows

    file.close()  # Close .scl file
    """               End of Parse .scl              """
    # Find the row, each node is placed in
    for row in row_list:
        for node in node_list:
            # check for both lower_y and upper_y to avoid Terminal nodes
            if (node.lower_left_corner.y == row.lower_left_corner.y and
                    node.upper_left_corner.y == row.upper_left_corner.y):
                node.set_row(row)
                row.append_node(node)

    # Find the row(s), each Net belongs to and the opposite
    for net in net_list:
        for node in net.net_nodes:
            if node.node_type == "Non_Terminal":
                net.append_row(node.node_row)
                node.node_row.append_net(net)
        net.net_rows = list(dict.fromkeys(net.net_rows))  # remove duplicates

    # Update each row, with its density
    for row in row_list:
        row.calculate_row_density()

    return node_list, net_list, row_list


def node_list_to_df(node_list):
    pd.set_option('display.width', 800)
    pd.set_option('display.max_columns', 20)

    nodes_df = pd.DataFrame.from_records([node.to_dict() for node in node_list])
    nodes_df['Size'] = nodes_df["Width"] * nodes_df["Height"]


    print("\nDisplay Nodes Dataframe: \n")
    print(nodes_df)

def lists_to_dataframes(node_list, net_list, row_list):

    print("\nDisplay Nets Dataframe: \n")
    nets_df = pd.DataFrame.from_records([net.to_dict() for net in net_list])
    print(nets_df)

    print("\nDisplay Rows Dataframe: \n")
    rows_df = pd.DataFrame.from_records([row.to_dict() for row in row_list])
    print(rows_df)

    # calculations for DF Design
    design_cells = nodes_df.shape[0]
    print("\nDesign num of cells: ", design_cells)

    design_nets = nets_df.shape[0]
    print("Design num of nets: ", design_nets)

    design_height = (rows_df['Coordinate_y_max'].max()
                     - rows_df['Coordinate_y_min'].min())
    print("Design Height: ", design_height)

    design_width = (rows_df['Coordinate_x_max'].max()
                    - rows_df['Coordinate_x_min'].min())
    print("Design Width: ", design_width)

    design_terminals = len(nodes_df[nodes_df['Type'].str.match('Terminal')])
    print("Design Terminals: ", design_terminals)

    design_total_area = design_height * design_width
    print("Design Total Area: ", design_total_area)

    design_total_cell_area = nodes_df['Size'].sum()
    print("Design Total Cell Area: ", design_total_cell_area)

    design_density = (design_total_cell_area / design_total_area) * 100
    print("Design Density: " + str(design_density) + "%")

    design_dict = {
        'Density (%)': design_density,
        'Number_of_cells': design_cells,
        'Number_of_terminals': design_terminals,
        'Number_of_nets': design_nets,
        'Width': design_width,
        'Height': design_height,
        'Total_Area': design_total_area,
        'Total_Cell_Area': design_total_cell_area
    }

    # 1st way to create DF Design
    # design_df = pd.DataFrame(design_dict, index=[0])

    # 2nd way to create DF design
    print("\nDisplay Designs Dataframe: \n")
    design_df = pd.DataFrame.from_records([design_dict])
    print(design_df)

    return nodes_df, nets_df, rows_df, design_df


# 2 - 5
def number_of_non_terminal_nodes(nodes_df):

    non_terminal_nodes = len(nodes_df[nodes_df['Type'].str.match('Non_Terminal')])
    print("Non Terminals nodes: ", non_terminal_nodes)


def biggest_non_terminal_node(nodes_df):

    max_df = nodes_df[nodes_df['Type'].str.match('Non_Terminal')]
    max_node_size = int(max_df['Size'].max())

    max_df = max_df[max_df.Size == max_node_size]
    max_nodes_list = list(max_df.Node_name)

    # print(max_df.get(["Node_name", "Size"]).to_string(index=False))
    print("Maximum Non Terminal Node size = ", max_node_size)
    print("Non Terminal Node(s) with max size: ", max_nodes_list)
    print("\n")


def smallest_non_terminal_node(nodes_df):

    min_df = nodes_df[nodes_df['Type'].str.match('Non_Terminal')]
    min_node_size = int(min_df['Size'].min())

    min_df = min_df[min_df.Size == min_node_size]
    min_nodes_list = list(min_df.Node_name)

    # print(min_df.get(["Node_name", "Size"]).to_string(index=False))
    print("Minimum Non Terminal Node size = ", min_node_size)
    print("Non Terminal Node(s) with min size: ", min_nodes_list)
    print("\n")


def mean_size_non_terminal_nodes(nodes_df):

    mean_df = nodes_df[nodes_df['Type'].str.match('Non_Terminal')]
    mean = float(mean_df['Size'].mean())
    mean = round(mean, 2)

    print("Mean size of Non Terminal Node(s): ", mean)


# 7 - 10 --- terminal are dots --> they have no size
def number_of_terminal_nodes(nodes_df):

    terminal_nodes = len(nodes_df[nodes_df['Type'].str.match('Terminal')])
    print("Terminals nodes: ", terminal_nodes)


# 12 - 15
def number_of_nets(nets_df):

    num_of_nets = nets_df.shape[0]
    print("Number of nets: ", num_of_nets)
    print("\n")


def biggest_net_based_on_nodes(nets_df):

    max_num_of_cells = int(nets_df["Nodes"].str.len().max())
    max_nets_df = nets_df[nets_df.Nodes.str.len() == max_num_of_cells]
    max_nets_list = list(max_nets_df.Net_name)

    print("Maximum number of cells in a net: ", max_num_of_cells)
    print("Biggest net(s): ", max_nets_list)
    print("\n")


def smallest_net_based_on_nodes(nets_df):

    min_num_of_cells = int(nets_df["Nodes"].str.len().min())
    min_nets_df = nets_df[nets_df.Nodes.str.len() == min_num_of_cells]
    min_nets_list = list(min_nets_df.Net_name)

    print("Minimum number of cells in a net: ", min_num_of_cells)
    print("Smallest net(s): ", min_nets_list)
    print("\n")


def mean_size_of_nets_based_on_nodes(nets_df):

    mean_num_of_cells = float(nets_df["Nodes"].str.len().mean())
    mean_num_of_cells = round(mean_num_of_cells, 2)

    print("Mean number of cell(s) on each net: ", mean_num_of_cells)
    print("\n")


def biggest_net_based_on_size(nets_df, nodes_df):
    """
    df = nets_df.get(["External_nodes"])
    print(df, type(df))

    serie = nets_df["External_nodes"]
    print(serie, type(serie))
    """

    # todo


def smallest_net_based_on_size(nets_df, nodes_df):
    # todo
    pass


def mean_net_based_on_size(nets_df, nodes_df):
    # todo
    pass


# 17 - 20
def number_of_rows(rows_df):
    num_of_rows = rows_df.shape[0]
    print("Number of rows: ", num_of_rows)
    print("\n")


def biggest_row(rows_df):

    max_num_of_cells = int(rows_df["Cells"].str.len().max())
    max_rows_df = rows_df[rows_df.Cells.str.len() == max_num_of_cells]
    max_rows_list = list(max_rows_df.Row_name)

    # print(max_rows_df.get(["Row_name", "Cells"]).to_string(index=False))
    print("Maximum number of cells in a row: ", max_num_of_cells)
    print("Biggest row(s): ", max_rows_list)
    print("\n")


def smallest_row(rows_df):

    min_num_of_cells = int(rows_df["Cells"].str.len().min())
    min_rows_df = rows_df[rows_df.Cells.str.len() == min_num_of_cells]
    min_rows_list = list(min_rows_df.Row_name)

    # print(min_rows_df.get(["Row_name", "Cells"]).to_string(index=False))
    print("Minimum number of cells in a row: ", min_num_of_cells)
    print("Smallest row(s): ", min_rows_list)
    print("\n")


def mean_num_of_nodes_on_rows(rows_df):

    mean_num_of_cells = float(rows_df["Cells"].str.len().mean())
    mean_num_of_cells = round(mean_num_of_cells, 2)

    print("Mean number of cells on each row: ", mean_num_of_cells)
    print("\n")


# 24 - 25
def design_half_perimeter_wirelength(nets_df):

    design_hpw = nets_df['Half_Perimeter_Wirelength'].sum()

    print("Design Half Perimeter Wirelength: ", design_hpw)
    print("\n")


def design_density(nodes_df, rows_df):

    design_height = (rows_df['Coordinate_y_max'].max()
                     - rows_df['Coordinate_y_min'].min())

    design_width = (rows_df['Coordinate_x_max'].max()
                    - rows_df['Coordinate_x_min'].min())

    design_total_area = design_height * design_width
    design_total_cell_area = nodes_df['Size'].sum()
    design_density = (design_total_cell_area / design_total_area) * 100

    print("Design Density: " + str(design_density) + "%")
    print("\n")


""" Testing DataFrames """


def row_density(nodes_df, nets_df, rows_df):

    # add 1 new column on the rows_df
    rows_df['testing_density'] = 0

    rows_width = int(rows_df['Coordinate_x_max'].max()
                     - int(rows_df['Coordinate_x_min'].max()))

    rows_height = int(rows_df['Coordinate_y_max'].max()
                      - rows_df['Coordinate_y_min'].max())

    row_area = rows_width * rows_height

    print(row_area)

    temp_nodes_df = pd.DataFrame()
    row_names_list = list(rows_df['Row_name'])

    for row_name in row_names_list:

        # temporary DF with nodes that belong to this list
        temp_nodes_df = nodes_df[nodes_df.Row_number == row_name]

        # sum of all node_sizes that belong to the current row
        row_all_nodes_area = temp_nodes_df.Size.sum()
        print(row_all_nodes_area)

        index = rows_df.index[rows_df.Row_name == row_name]  # type int64Index
        index = int(index[0])

        rows_df.at[index, 'testing_density'] = float((row_all_nodes_area / row_area) * 100)

    print(rows_df)
    print("\n")


# Net's min/max & net_size & HPW
def net_size_and_hpw(nodes_df, nets_df):

    # add 2 new columns on the nets_df
    nets_df['testing_Net_size'] = 0
    nets_df['testing_HPW'] = 0

    net_names_list = list(nets_df['Net_name'])
    net_externals_list = list(nets_df['External_nodes'])
    # print(net_names_list, len(net_names_list))
    # print(net_externals_list, len(net_externals_list))

    for net_name, node_names in zip(net_names_list, net_externals_list):
        # print("\n")
        # print(net_name)
        # print(node_names)

        test_node_df = pd.DataFrame()
        one_line_df = pd.DataFrame()
        test_node_df['x_max'] = 0
        test_node_df['y_max'] = 0

        for name in node_names:
           # test_node_df = test_node_df.append(nodes_df[nodes_df.Node_name == name], sort=True)

            one_line_df = nodes_df[nodes_df.Node_name == name]
            current_node_type = len(one_line_df['Type'].str.match('Terminal'))

            print(one_line_df)
            # Terminals have no Width and Height
            if current_node_type == 0:
                one_line_df['x_max'] = (one_line_df['Coordinate_x']
                                         + one_line_df['Width'])

                one_line_df['y_max'] = (one_line_df['Coordinate_y']
                                         + one_line_df['Height'])

            else:
                one_line_df['x_max'] = one_line_df['Coordinate_x']
                one_line_df['y_max'] = one_line_df['Coordinate_y']

            #test_node_df = test_node_df.append(one_line_df)

        print("\n")
        #print(test_node_df)

        net_x_min = int(test_node_df['Coordinate_x'].min())
        net_x_max = int(test_node_df['x_max'].max())
        net_y_min = int(test_node_df['Coordinate_y'].min())
        net_y_max = int(test_node_df['y_max'].max())

        index = nets_df.index[nets_df.Net_name == net_name]  # type int64Index
        index = int(index[0])

        nets_df.at[index, 'test_x_min'] = net_x_min
        nets_df.at[index, 'test_x_max'] = net_x_max
        nets_df.at[index, 'test_y_min'] = net_y_min
        nets_df.at[index, 'test_y_max'] = net_y_max

        nets_df.at[index, 'testing_Net_size'] = ((net_x_max - net_x_min)
                                                 * (net_y_max - net_y_min))

        nets_df.at[index, 'testing_HPW'] = ((net_x_max - net_x_min)
                                            + (net_y_max - net_y_min))




    print(nets_df)


    """
    # dictionary me ta nodes internal+external tou kathe net
    # nets_dict = nets_df.set_index('Net_name').T.to_dict('records')
    # print(nets_dict)
    """



# TESTING PRINTS:
"""

    for net in net_list:
        net.display_net_rows()
        net.display_net_external_nodes()
        net.display_net_internal_nodes()
    print("\n\n**")


    for row in row_list:
        print("\n\n**")
        row.display_row_nets()
        row.display_row_nodes()


    for net in net_list:
        for row in net.net_rows:
            print(type(row.net_rows))


    for net in net_list:
        for node in node_list:
            if node.node_name == net.net


    for node in node_list:
        node.display_node_row()


    for row in row_list:
        row.display_row()


    for i in row_list:
        print(i)


    a = 0
    for i in node_list:
        a = a + 1
        i.display_node_corners()

        if a == 20:
            break


    a = 0
    for i in net_list:
        a += 1
        i.display_net()
        i.find_coordinates_of_net()
        i.calculate_net_wirelength()
        i.calculate_net_size()

        print("\n")

        i.display_net_size()
        i.display_net_wirelength()
        if a == 15:
            break
"""


