from dataclasses import dataclass


@dataclass
class Pacman:
    x: int
    y: int

    @property
    def pos(self):
        return self.x, self.y

    def set_pos(self, pos):
        self.x = pos[0]
        self.y = pos[1]
