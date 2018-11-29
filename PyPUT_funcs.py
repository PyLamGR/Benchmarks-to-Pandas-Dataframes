def get_terminal_nodes_list_number2(nodes_file_name):
    """
    @gk
    This function takes as input a file of nodes type and
    returns a dictionary with the coordinates of each non-terminal node
    dict = {'name': [x, y, width, height]}
    :param nodes_file_name:
    :return:
    """
    widht = height = x = y = 0
    nodes = {}
    data = []

    pl_file_name = nodes_file_name.replace('.nodes', '.pl')
    with open(pl_file_name) as p:
        for num, line in enumerate(p):
            if num == 0 or '#' in line or line == '\n':
                continue
            else:
                data = line.split()
                x = float(data[1])
                y = float(data[2])
                nodes[data[0]] = [x]
                nodes[data[0]].append(y)

    with open(nodes_file_name) as nf:
        for num, line in enumerate(nf):
            if num == 0 or '#' in line or line == '\n' or "NumNodes" in line or "NumTerminals" in line:
                continue
            elif "terminal" in line or "terminal_NI" in line:
                data = line.split()
                nodes[data[0]].append(float(data[1]))
                nodes[data[0]].append(float(data[2]))
            else:
                data = line.split()
                del nodes[data[0]]

    return nodes


def get_non_terminal_nodes_list_number2(nodes_file_name):
    """
    @gk
    This function takes as input a file of nodes type and
    returns a dictionary with the coordinates of each non-terminal node
    dict = {'name': [x, y, width, height]}
    :param nodes_file_name:
    :return:
    """
    widht = height = x = y = 0
    nodes = {}
    data = []

    pl_file_name = nodes_file_name.replace('.nodes', '.pl')
    with open(pl_file_name) as p:
        for num, line in enumerate(p):
            if num == 0 or '#' in line or line == '\n':
                continue
            else:
                data = line.split()
                x = int(data[1])
                y = int(data[2])
                nodes[data[0]] = [x]
                nodes[data[0]].append(y)

    with open(nodes_file_name) as nf:
        for num, line in enumerate(nf):
            if num == 0 or '#' in line or line == '\n' or "NumNodes" in line or "NumTerminals" in line:
                continue
            elif "terminal" in line or "terminal_NI" in line:
                data = line.split()
                del nodes[data[0]]
            else:
                data = line.split()
                nodes[data[0]].append(int(data[1]))
                nodes[data[0]].append(int(data[2]))

    return nodes
