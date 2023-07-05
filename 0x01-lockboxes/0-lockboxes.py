# method that determines if all the boxes can be opened.
def canUnlockAll(boxes):

    n = len(boxes)
    visited = [False] * n  # Keep track of visited boxes
    visited[0] = True  # First box is unlocked
    queue = [0]  # Start BFS with the first box

    while queue:
        current_box = queue.pop(0)
        keys = boxes[current_box]

        for key in keys:
            if not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
