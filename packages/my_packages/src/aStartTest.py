
import heapq

def astar(start, goal, graph):
  
    # Initialize the open and closed sets
    open_set = []
    closed_set = set()

    # Add the starting node to the open set
    heapq.heappush(open_set, (0, start, [start]))

    while open_set:
        # Get the node with the lowest f score
        current_cost, current_node, path = heapq.heappop(open_set)

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

            # If the neighbor is not in the open set, add it
            if not any(neighbor in item for item in open_set):
                heapq.heappush(open_set, (tentative_f_score, neighbor, path + [neighbor]))
            else:
                # If the neighbor is already in the open set, update its f score if the new score is lower
                for item in open_set:
                    if neighbor in item:
                        if tentative_f_score < item[0]:
                            item[0] = tentative_f_score
                            item[2] = path + [neighbor]

    # If we've exhausted all possible paths and haven't found the goal, return None
    return None

def heuristic(node, goal):
   
    # In this example, we'll use the Manhattan distance as our heuristic
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


graph = {
    (0, 0): {(0, 1): 0, (1, 0): 1},
    (0, 1): {(0, 0): 0, (0, 2): 1, (1, 1): 1},
    (0, 2): {(0, 1): 0, (0, 3): 1, (1, 2): 1},
    (0, 3): {(0, 2): 0, (0, 4): 1, (1, 3): 1},
    (0, 4): {(0, 3): 0, (1, 4): 1},

    (1, 0): {(0, 0): 1, (1, 1): 1, (2, 0): 1},
    (1, 1): {(0, 1): 1, (1, 0): 1, (1, 2): 1, (2, 1): 1},
    (1, 2): {(0, 2): 1, (1, 1): 1, (1, 3): 1, (2, 2): 1},
    (1, 3): {(0, 3): 1, (1, 2): 1, (1, 4): 1, (2, 3): 1},
    (1, 4): {(0, 4): 1, (1, 3): 1, (2, 4): 1},

    (2, 0): {(1, 0): 0, (2, 1): 1, (3, 0): 0},
    (2, 1): {(1, 1): 0, (2, 0): 1, (2, 2): 0, (3, 1): 1},
    (2, 2): {(1, 2): 0, (2, 1): 1, (2, 3): 0, (3, 2): 1},
    (2, 3): {(1, 3): 0, (2, 2): 1, (2, 4): 0, (3, 3): 1},
    (2, 4): {(1, 4): 0, (2, 3): 1, (3, 4): 0},

    (3, 0): {(2, 0): 1, (3, 1): 1, (4, 0): 0},
    (3, 1): {(2, 1): 1, (3, 0): 1, (3, 2): 0, (4, 1): 1},
    (3, 2): {(2, 2): 1, (3, 1): 1, (3, 3): 0, (4, 2): 1},
    (3, 3): {(2, 3): 1, (3, 2): 1, (3, 4): 0, (4, 3): 1},
    (3, 4): {(2, 4): 1, (3, 3): 1, (4, 4): 0},

    (4, 0): {(3, 0): 0, (4, 1): 1},
    (4, 1): {(3, 1): 0, (4, 0): 1, (4, 2): 1},
    (4, 2): {(3, 2): 0, (4, 1): 1, (4, 3): 1},
    (4, 3): {(3, 3): 0, (4, 2): 1, (4, 4): 1},
    (4, 4): {(3, 4): 0, (4, 3): 1}
}

# Example start and goal nodes
start_node = (0, 0)
goal_node = (4, 4)

# Example usage of the A* algorithm
path = astar(start_node, goal_node, graph)
print("Path found:", path)

# Create an image to visualize the maze and the path

