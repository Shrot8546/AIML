def idfs(graph, start, goal, max_depth):
    def dfs_with_limit(node, depth):
        if depth == 0:
            return [node] if node == goal else []
        elif depth > 0:
            path = []
            for neighbor in graph[node]:
                if neighbor not in path:
                    result = dfs_with_limit(neighbor, depth-1)
                    if result:
                        path = [node] + result
                        break
            return path
        return []

    for depth in range(max_depth + 1):
        result = dfs_with_limit(start, depth)
        if result:
            return result
    return []

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

print(idfs(graph, 0, 3, 3))  
