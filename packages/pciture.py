from PIL import Image

def create_image_with_path(maze_grid, path, cell_size=20):
    height = len(maze_grid)
    width = len(maze_grid[0])

    image = Image.new("RGB", (width * cell_size, height * cell_size), "white")
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            if maze_grid[y][x] == 0:
                color = (255, 255, 255)  # white for open paths
            elif maze_grid[y][x] == 30:
                color = (0, 0, 0)  # black for walls
            else:
                color = (maze_grid[y][x], maze_grid[y][x], maze_grid[y][x])  # adjust as needed

            if (y, x) in path:
                color = (0, 255, 0)  # green for the path

            for dy in range(cell_size):
                for dx in range(cell_size):
                    pixels[x * cell_size + dx, y * cell_size + dy] = color

    image.show()

# Your 15x15 maze grid
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 30, 30, 30, 30, 0, 30, 30, 30, 30, 30, 30, 30, 30, 0],
    [0, 0, 0, 0, 30, 0, 30, 0, 0, 0, 0, 0, 30, 30, 0],
    [0, 30, 30, 30, 30, 0, 30, 0, 30, 30, 30, 0, 30, 0, 0],
    [0, 30, 0, 0, 0, 0, 30, 0, 30, 0, 30, 0, 30, 30, 0],
    [0, 30, 30, 30, 30, 0, 30, 0, 30, 0, 30, 0, 0, 0, 0],
    [0, 0, 0, 0, 30, 0, 30, 0, 30, 30, 30, 30, 30, 30, 0],
    [30, 30, 30, 0, 30, 0, 30, 0, 0, 0, 0, 0, 0, 30, 0],
    [0, 0, 30, 0, 30, 0, 30, 30, 30, 30, 30, 30, 0, 30, 0],
    [0, 30, 30, 0, 30, 0, 0, 0, 0, 0, 0, 30, 0, 30, 0],
    [0, 30, 0, 0, 30, 0, 30, 30, 30, 30, 0, 30, 0, 30, 30],
    [0, 30, 30, 30, 30, 0, 30, 0, 0, 30, 0, 30, 0, 30, 0],
    [0, 0, 0, 0, 0, 0, 30, 0, 30, 30, 0, 30, 0, 30, 0],
    [0, 30, 30, 30, 30, 30, 30, 0, 0, 0, 0, 30, 0, 30, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# The path you provided
path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (10, 10), (11, 10), (12, 10), (13, 10), (14, 10), (14, 11), (14, 12), (14, 13), (14, 14)]

create_image_with_path(grid, path)
