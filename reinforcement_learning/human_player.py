"""
A class that represents a human player
"""


class HumanPlayer:
    """
    Represents the user, only needs the pick_action method therefore all other methods are unimplemented
    """
    def __init__(self, name):
        self.name = name

    def pick_action(self, positions, board, turn):
        """
        Picks the move based on user input
        :param positions: the available positions
        :param board: so a human player and bot can use the same method
        :param turn: so a human player and bot can use the same method
        """
        print([position + 1 for position in positions])
        while True:
            try:
                pos = int(input("Where do you want to play: ")) - 1
            except ValueError:
                print("Please enter an integer.")
                continue
            if pos in positions:
                return pos
            else:
                print("Position {} is not a valid position".format(pos + 1))

    def add_state(self, state):
        pass

    def feed_reward(self, reward):
        pass

    def reset(self):
        pass
