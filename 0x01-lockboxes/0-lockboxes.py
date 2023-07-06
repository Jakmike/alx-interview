def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n  # Keep track of visited boxes
    visited[0] = True  # First box is unlocked

    def dfs(box):
        visited[box] = True
        keys = boxes[box]
        for key in keys:
            if not visited[key]:
                dfs(key)

    dfs(0)  # Start DFS with the first box

    return all(visited)
