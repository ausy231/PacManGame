from pacman import Pacman
from dataclasses import dataclass

class Maze:
    WALL = "#"
    POINT = "."
    SPACE = " "
    PACMAN = "P"
    DEAD = "X"
    GHOST = "G"

    def __init__(self, maze):
        self.height = len(maze)
        self.width = len(maze[0])
        self.maze = maze
        self.base = []
        for row in maze:
            self.base.append([c if c == self.WALL or c == "." else self.SPACE for c in row])
        pacman_pos, self.ghosts = self.analise()
        self.pacman = Pacman(x=pacman_pos[0], y=pacman_pos[1])

    def __str__(self):
        string = ""
        for row in self.maze:
            string += "".join(row) + "\n"
        return string[:-1]

    def analise(self):
        ghosts = []
        pacman_pos = (1, 1)
        for y in range(self.height):
            for x in range(self.width):
                if self[x, y] == self.GHOST:
                    ghosts.append(Ghost(maze=self, x=x, y=y))
                elif self.is_pacman((x, y)):
                    pacman_pos = (x, y)
        return pacman_pos, ghosts

    def __getitem__(self, pos):
        return self.maze[pos[1]][pos[0]]

    def __setitem__(self, pos, value):
        self.maze[pos[1]][pos[0]] = str(value)

    def get_base(self, pos):
        return self.base[pos[1]][pos[0]]

    def is_wall(self, pos):
        return self.maze[pos[1]][pos[0]] == self.WALL

    def is_point(self, pos):
        return self.maze[pos[1]][pos[0]] == self.POINT

    def is_pacman(self, pos):
        return self.maze[pos[1]][pos[0]] == self.PACMAN

    def move_ghosts(self, target):
        for ghost in self.ghosts:
            current_pos = ghost.pos
            new_pos = ghost.search(target)
            self[current_pos] = self.get_base(current_pos)

            ghost.set_pos(new_pos)

        for ghost in self.ghosts:
            if self[ghost.pos] == self.PACMAN or self[ghost.pos] == self.DEAD:
                self[ghost.pos] = self.DEAD
            else:
                self[ghost.pos] = self.GHOST

    def get_state(self):
        for ghost in self.ghosts:
            if ghost.pos == self.pacman.pos:
                self[self.pacman.pos] = self.DEAD
                return True, "You died!"

        for y in range(self.height):
            for x in range(self.width):
                if self[x, y] == ".":
                    return False, "Keep playing!"

        return True, "You won!"

    def get_pacman_pos(self):
        return self.pacman.pos

    def move(self, x_add, y_add):
        new_pos = self.pacman.pos[0] + x_add, self.pacman.pos[1] + y_add

        if self.is_wall(new_pos) or not new_pos[0] in range(self.width) or not new_pos[1] in range(self.height):
            return False

        self[self.pacman.pos] = self.SPACE
        self.pacman.set_pos(new_pos)
        if self.is_point(new_pos):
            self[new_pos] = self.PACMAN
            self.base[new_pos[1]][new_pos[0]] = self.SPACE
            return True

        self[new_pos] = self.PACMAN
        return False


@dataclass
class Ghost:
    DIRECTIONS = ((0, -1), (-1, 0), (0, 1), (1, 0))
    x: int
    y: int
    maze: Maze

    @property
    def pos(self):
        return self.x, self.y

    def set_pos(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def search(self, pos):
        todo = [[(self.x, self.y)]]
        while todo:
            current_path = todo.pop(0)
            if current_path[-1] == pos and len(current_path) > 1:
                return current_path[1]

            x, y = current_path[-1]
            for x_add, y_add in self.DIRECTIONS:
                if not self.maze.is_wall((x + x_add, y + y_add)) and not (x + x_add, y + y_add) in current_path:
                    todo.append(current_path + [(x + x_add, y + y_add)])

        return self.pos
