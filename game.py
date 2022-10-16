from maze import Maze


class Game:
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"

    def __init__(self, maze):
        self.maze = Maze(maze)
        self.done = False
        self.state = ""
        self.points = 0

    def turn(self, game_input):
        self.done, self.state = self.maze.get_state()
        if self.done:
            return

        old_position = (self.maze.get_pacman_pos())
        new_pos = ()
        if game_input == self.UP:
            new_pos = (0, -1)
        if game_input == self.DOWN:
            new_pos = (0, 1)
        if game_input == self.LEFT:
            new_pos = (-1, 0)
        if game_input == self.RIGHT:
            new_pos = (1, 0)

        self.points += int(self.maze.move(new_pos[0], new_pos[1]))

        self.done, self.state = self.maze.get_state()
        if self.done:
            return

        self.maze.move_ghosts(old_position)

        self.done, self.state = self.maze.get_state()
        if self.done:
            return

    def get_state(self):
        return self.state

    def finished(self):
        return self.done

    def get_score(self):
        return self.points

    def __str__(self):
        return str(self.maze)
