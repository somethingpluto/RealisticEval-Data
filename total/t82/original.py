def cycles_by_size(self, filter_repeat_nodes=True) -> dict[int: list[int]]:
    """
    Code partially written by ChatGPT
    Construct a list of unique cycles in the graph,
    where each second-level list is composed of cycles of the same size,
    and each cycle visits each node at most once.

    Returns:
    dict: dictionary where keys are cycle sizes and values are lists of unique cycles
    """

    # Use simple_cycles to get all cycles in the graph
    all_cycles = list(nx.simple_cycles(self.graph))

    # Filter out cycles with fewer than 3 nodes
    # (since the graph is undirected, any edge is also a "cycle" so filter those out)
    cycles = [cycle for cycle in all_cycles if len(cycle) > 2]
    if filter_repeat_nodes:
        # filter and cycles that visit any node more than once
        cycles = [cycle for cycle in cycles if len(cycle) == len(set(cycle))]

    # Remove duplicates from the cycles (ignoring the order of nodes)
    unique_cycles = list(set(frozenset(cycle) for cycle in cycles))

    # Initialize a default dictionary to store cycles by size
    unique_cycles_by_size = defaultdict(list)

    # Iterate over the cycles
    for cycle in unique_cycles:
        # The size of the cycle is its length
        size = len(cycle)

        # Append the cycle to the list of cycles of the same size
        unique_cycles_by_size[size].append(self.graph.subgraph(list(cycle)))

    return unique_cycles_by_size