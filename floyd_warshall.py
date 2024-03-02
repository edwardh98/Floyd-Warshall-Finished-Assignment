def floyd_warshall_recursive(graph, n, memo={}):
    """Recursive implementation of the Floyd-Warshall algorithm.

    Args:
        graph: Adjacency matrix representation of the graph.
        n: Number of vertices in the graph.
        memo: Dictionary to store calculated distances (memoization).

    Returns:
        The distance matrix, where dist[i][j] represents the shortest
        distance between vertices i and j.
    """

    def shortest_path(i, j, k):
        key = (i, j, k)
        if key in memo:
            return memo[key]

        if k == -1:  # Base case: no intermediate vertices
            result = graph[i][j]
        else:
            result = min(shortest_path(i, j, k - 1),
                         shortest_path(i, k, k - 1) + shortest_path(k, j, k - 1))

        memo[key] = result
        return result

    distance_matrix = [[graph[i][j] for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance_matrix[i][j] = shortest_path(i, j, k)

    return distance_matrix
