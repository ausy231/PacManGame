class Controller:
    def __init__(self, game):
        self.game = game

    def play(self):
        while not self.game.done:
            print(self.game.maze)
            controller_input = input("Input (U,D,L,R): ")
            if controller_input == "U":
                self.game.turn(game_input=self.game.UP)
            elif controller_input == "D":
                self.game.turn(game_input=self.game.DOWN)
            elif controller_input == "L":
                self.game.turn(game_input=self.game.LEFT)
            elif controller_input == "R":
                self.game.turn(game_input=self.game.RIGHT)
            else:
                print("incorrect input!")

        print(self.game.get_state())
        print(self.game)
        print(f"Points: {self.game.get_score()}")
        print("Thanks for playing!")
