from PIL import Image

def create_image_with_path(graph, path, cell_size=20):
    min_x, min_y, max_x, max_y = float('inf'), float('inf'), 0, 0

    for node in graph:
        min_x = min(min_x, node[0])
        min_y = min(min_y, node[1])
        max_x = max(max_x, node[0])
        max_y = max(max_y, node[1])

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    image = Image.new("RGB", (width * cell_size, height * cell_size), "white")
    pixels = image.load()

    for node in graph:
        x = node[0] - min_x
        y = node[1] - min_y

        # Check if the current node is in the path
        if node in path:
            color = (0, 255, 0)  # green for the path
        else:
            # Check if the current node is a wall
            if not graph[node]:
                color = (0, 0, 0)  # black for walls
            else:
                color = (255, 255, 255)  # white for open paths

        for dy in range(cell_size):
            for dx in range(cell_size):
                pixels[x * cell_size + dx, y * cell_size + dy] = color

    image.show()

# Your graph
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
path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

# Example usage of the create_image_with_path function
create_image_with_path(graph, path)
