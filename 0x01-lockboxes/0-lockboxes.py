#!/usr/bin/python3

"""
Lockboxes module.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    Args:
        boxes (list): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """

    n = len(boxes)
    visited = [False] * n  # Keep track of visited boxes
    visited[0] = True  # First box is unlocked

    def dfs(box):
        """
        Perform depth-first search (DFS) to explore the boxes and their keys.

        Args:
            box (int): The box number to start the DFS from.
        """

        visited[box] = True
        keys = boxes[box]
        for key in keys:
            if not visited[key]:
                dfs(key)

    dfs(0)  # Start DFS with the first box

    return all(visited)
