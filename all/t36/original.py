def floyd_warshall_shortest_paths(adjacency_matrix: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:

    num_vertices = len(adjacency_matrix)

    def _recursive_floyd_warshall(k: int) -> List[List[Union[int, float]]]:
        """
        Recursive helper function for Floyd-Warshall algorithm.

        Args:
            k (int): The current intermediate vertex being considered.

        Returns:
            List[List[Union[int, float]]]: The updated adjacency matrix after considering the current intermediate vertex.
        """
        if k == num_vertices:
            return adjacency_matrix
        for i in range(num_vertices):
            for j in range(num_vertices):
                # Update the distance to the minimum of the current or via vertex k
                adjacency_matrix[i][j] = min(adjacency_matrix[i][j],
                                             adjacency_matrix[i][k] + adjacency_matrix[k][j])
        return _recursive_floyd_warshall(k + 1)

    return _recursive_floyd_warshall(0)
