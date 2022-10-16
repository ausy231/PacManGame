from game import Game
from controller import Controller


def get_maze_from_file(path):
    maze_array = []
    for line in open(path):
        maze_array.append([c for c in line][:-1])
    return maze_array


def main():
    maze_path = "maze.txt"
    pacman_game = Game(get_maze_from_file(maze_path))
    my_controller = Controller(pacman_game)
    my_controller.play()


if __name__ == "__main__":
    main()
    