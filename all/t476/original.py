def topological_sort_python(
    nodes: Union[Set[int], List[int]],
    conns: Union[Set[Tuple[int, int]], List[Tuple[int, int]]],
) -> Tuple[List[int], List[List[int]]]:
    # a python version of topological_sort, use python set to store nodes and conns
    # returns the topological order of the nodes and the topological layers
    # written by gpt4 :)

    # Make a copy of the input nodes and connections
    nodes = nodes.copy()
    conns = conns.copy()

    # Initialize the in-degree of each node to 0
    in_degree = {node: 0 for node in nodes}

    # Compute the in-degree for each node
    for conn in conns:
        in_degree[conn[1]] += 1

    topo_order = []
    topo_layer = []

    # Find all nodes with in-degree 0
    zero_in_degree_nodes = [node for node in nodes if in_degree[node] == 0]

    while zero_in_degree_nodes:

        for node in zero_in_degree_nodes:
            nodes.remove(node)

        zero_in_degree_nodes = sorted(
            zero_in_degree_nodes
        )  # make sure the topo_order is from small to large

        topo_layer.append(zero_in_degree_nodes.copy())

        for node in zero_in_degree_nodes:
            topo_order.append(node)

            # Iterate over all connections and reduce the in-degree of connected nodes
            for conn in list(conns):
                if conn[0] == node:
                    in_degree[conn[1]] -= 1
                    conns.remove(conn)

        zero_in_degree_nodes = [node for node in nodes if in_degree[node] == 0]

    # Check if there are still connections left indicating a cycle
    if conns or nodes:
        raise ValueError("Graph has at least one cycle, topological sort not possible")

    return topo_order, topo_layer