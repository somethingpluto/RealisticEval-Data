from typing import List, Tuple


def topological_sort_dfs(vertices: List[int], edges: List[Tuple]) -> List:
    """
    achieve topological sorting, based on depth priority search

    Args:
        vertices (List[int]): A list of vertices in the graph. Each vertex should be a unique integer.
        edges (List[Tuple[int, int]]): A list of tuples where each tuple represents a directed edge
                                       in the graph and is formed as (start_vertex, end_vertex).

    Returns:
        List[int]: A list of vertices in topological order. If the graph contains a cycle,
                   and thus cannot have a valid topological ordering, an empty list is returned.
    """
    from collections import defaultdict, deque
    graph = defaultdict(list)
    visited = set()
    result = deque()  # 使用双端队列存储结果

    # 构建图
    for u, v in edges:
        graph[u].append(v)

    # 递归的深度优先搜索函数
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        result.appendleft(node)  # 将节点添加到结果的前端

    # 遍历所有节点
    for vertex in vertices:
        if vertex not in visited:
            dfs(vertex)

    return list(result)
