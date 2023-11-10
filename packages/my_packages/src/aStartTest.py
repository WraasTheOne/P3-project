import heapq

def astar(start, goal, graph):
    # Initialize the open and closed sets
    open_set = {}
    closed_set = set()

    # Add the starting node to the open set
    open_set[start] = (0, [start])

    while open_set:
        # Get the node with the lowest f score from the open set
        current_node = min(open_set, key=lambda node: open_set[node][0])
        current_cost, path = open_set[current_node]

        # Remove the current node from the open set
        del open_set[current_node]

        # If we've reached the goal, return the path
        if current_node == goal:
            return path

        # Add the current node to the closed set
        closed_set.add(current_node)

        # Check each neighbor of the current node
        for neighbor, weight in graph[current_node].items():
            # If the neighbor is already in the closed set, skip it
            if neighbor in closed_set:
                continue

            # Calculate the tentative g score
            tentative_g_score = current_cost + weight

            # Calculate the tentative f score
            h_score = heuristic(neighbor, goal)
            tentative_f_score = tentative_g_score + h_score

            if neighbor not in open_set or tentative_f_score < open_set[neighbor][0]:
                open_set[neighbor] = (tentative_f_score, path + [neighbor])

    # If we've exhausted all possible paths and haven't found the goal, return None
    return None

# Rest of your code remains the same


def heuristic(node, goal):
    # In this example, we'll use the Manhattan distance as our heuristic
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])



graph = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (0, 2): 1, (1, 1): 1},
    (0, 2): {(0, 1): 1, (0, 3): 1, (1, 2): 1},
    (0, 3): {(0, 2): 1, (0, 4): 1, (1, 3): 1},
    (0, 4): {(0, 3): 1, (1, 4): 1},

    (1, 0): {(0, 0): 1, (1, 1): 1, (2, 0): 1},
    (1, 1): {(0, 1): 1, (1, 0): 1, (1, 2): 1, (2, 1): 1},
    (1, 2): {(0, 2): 1, (1, 1): 1, (1, 3): 1, (2, 2): 1},
    (1, 3): {(0, 3): 1, (1, 2): 1, (1, 4): 1, (2, 3): 1},
    (1, 4): {(0, 4): 1, (1, 3): 1, (2, 4): 1},

    (2, 0): {(1, 0): 1, (2, 1): 1, (3, 0): 1},
    (2, 1): {(1, 1): 1, (2, 0): 1, (2, 2): 1, (3, 1): 1},
    (2, 2): {(1, 2): 1, (2, 1): 1, (2, 3): 1, (3, 2): 1},
    (2, 3): {(1, 3): 1, (2, 2): 1, (2, 4): 1, (3, 3): 1},
    (2, 4): {(1, 4): 1, (2, 3): 1, (3, 4): 1},

    (3, 0): {(2, 0): 1, (3, 1): 1, (4, 0): 1},
    (3, 1): {(2, 1): 1, (3, 0): 1, (3, 2): 1, (4, 1): 1},
    (3, 2): {(2, 2): 1, (3, 1): 1, (3, 3): 1, (4, 2): 1},
    (3, 3): {(2, 3): 1, (3, 2): 1, (3, 4): 1, (4, 3): 1},
    (3, 4): {(2, 4): 1, (3, 3): 1, (4, 4): 1},

    (4, 0): {(3, 0): 1, (4, 1): 1},
    (4, 1): {(3, 1): 1, (4, 0): 1, (4, 2): 1},
    (4, 2): {(3, 2): 1, (4, 1): 1, (4, 3): 1},
    (4, 3): {(3, 3): 1, (4, 2): 1, (4, 4): 1},
    (4, 4): {(3, 4): 1, (4, 3): 1}
}

# Example start and goal nodes
start_node = (0, 0)
goal_node = (4, 4)

# Example usage of the A* algorithm
path = astar(start_node, goal_node, graph)
print("Path found:", path)

# Create an image to visualize the maze and the path