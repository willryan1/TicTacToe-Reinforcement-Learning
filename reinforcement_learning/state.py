"""
This file holds the state class which will represent a game between two tic tac toe players. Can train the two players
with the train method using reinforcement learning.
"""

BOARD_ROWS = 3
BOARD_COLUMNS = 3


def check_same(elements):
    """
    Checks if a list of three elements add to 3 or -e signaling a win
    :param elements: list of three elements
    :return: 1 for player 1 win, -1 for player 2 win, and zero for no win
    """
    if sum(elements) == 3:
        return 1
    elif sum(elements) == -3:
        return -1
    else:
        return 0


class State:
    """
    This class represents a tic tac toe game between two players.
    """
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.board = [0] * 9
        self.end = False
        self.current_turn = 1

    def get_key(self):
        """
        Key that can be added to states value dictionary
        :return: key
        """
        return str(self.board)

    def availible_moves(self):
        """
        :return: moves that can be played
        """
        moves = []
        for i, move in enumerate(self.board):
            if move == 0:
                moves.append(i)
        return moves

    def move(self, position):
        """
        Updates board and turn during a move
        :param position: positions available
        """
        self.board[position] = self.current_turn
        self.current_turn = -1 if self.current_turn == 1 else 1

    def check_win(self):
        """
        Checks for a win by making a list of all possible wins
        :return: 1 for player 1 win, -1 for player 2 win, 0 for a tie, and None for no wins
        """
        checks = [check_same(self.board[:3]), check_same(self.board[3:6]), check_same(self.board[6:]),
                  check_same([self.board[0], self.board[3], self.board[6]]),
                  check_same([self.board[1], self.board[4], self.board[7]]),
                  check_same([self.board[2], self.board[5], self.board[8]]),
                  check_same([self.board[0], self.board[4], self.board[8]]),
                  check_same([self.board[2], self.board[4], self.board[6]])]
        for i in checks:
            if i == 1:
                self.end = True
                return 1
            if i == -1:
                self.end = True
                return -1
        if len(self.availible_moves()) == 0:
            self.end = True
            return 0
        self.end = False
        return None

    def reward(self):
        """
        Gives rewards according to the success in the game
        """
        result = self.check_win()
        if result == 1:
            self.p1.reward_player(1)
            self.p2.reward_player(0)
        elif result == -1:
            self.p1.reward_player(0)
            self.p2.reward_player(1)
        else:
            self.p1.reward_player(0.1)
            self.p2.reward_player(0.5)

    def reset(self):
        """
        Reset game
        """
        self.board = [0] * 9
        self.end = False
        self.current_turn = 1

    def print_board(self):
        """
        Prints current board with x being 1 and o being -1
        """
        sep = " | "
        print("---------")
        values = [0, 1, 3, 4, 6, 7]
        for i, v in enumerate(self.board):
            if v == 1:
                c = 'x'
            elif v == -1:
                c = 'o'
            else:
                c = '0'
            if i in values:
                print(c + sep, end="")
            else:
                print(c)
                print("---------")

    def train(self, episodes=10000):
        """
        Trains the bots by playing and updating policy after every win
        :param episodes: amount of times to play
        """
        for i in range(episodes):
            if i % 1000 == 0:
                print("Episode {}".format(i))
            while not self.end:
                positions = self.availible_moves()
                p1_move = self.p1.pick_action(positions, self.board, self.current_turn)
                self.move(p1_move)
                board_key = self.get_key()
                self.p1.add_state(board_key)

                is_win = self.check_win()
                if is_win is not None:
                    self.reward()
                    self.p1.reset()
                    self.p2.reset()
                    self.reset()
                    break
                else:
                    positions = self.availible_moves()
                    p2_move = self.p2.pick_action(positions, self.board, self.current_turn)
                    self.move(p2_move)
                    board_key = self.get_key()
                    self.p2.add_state(board_key)

                    is_win = self.check_win()
                    if is_win is not None:
                        self.reward()
                        self.p1.reset()
                        self.p2.reset()
                        self.reset()
                        break

    def visualize_train(self):
        """
        Trains for one round allowing the user to see how the training process works depending on the game
        """
        while not self.end:
            positions = self.availible_moves()
            p1_move = self.p1.pick_action(positions, self.board, self.current_turn)
            self.move(p1_move)
            self.print_board()
            board_key = self.get_key()
            self.p1.add_state(board_key)

            is_win = self.check_win()
            if is_win is not None:
                self.reward()
                print(self.p1.states_value)
                print(self.p2.states_value)
                self.p1.reset()
                self.p2.reset()
                self.reset()
                break
            else:
                positions = self.availible_moves()
                p2_move = self.p2.pick_action(positions, self.board, self.current_turn)
                self.move(p2_move)
                self.print_board()
                board_key = self.get_key()
                self.p2.add_state(board_key)

                is_win = self.check_win()
                if is_win is not None:
                    self.reward()
                    print(self.p1.states_value)
                    print(self.p2.states_value)
                    self.p1.reset()
                    self.p2.reset()
                    self.reset()
                    break

    def play(self):
        """
        Allows other users other than bots to play against other players or bots
        """
        while not self.end:
            positions = self.availible_moves()
            p1_move = self.p1.pick_action(positions, self.board, self.current_turn)
            self.move(p1_move)
            self.print_board()
            is_win = self.check_win()
            if is_win is not None:
                if is_win == 1:
                    print(self.p1.name, "wins!")
                else:
                    print("Tie!")
                self.reset()
                break
            else:
                positions = self.availible_moves()
                p2_action = self.p2.pick_action(positions, self.board, self.current_turn)

                self.move(p2_action)
                self.print_board()
                win = self.check_win()
                if win is not None:
                    if win == -1:
                        print(self.p2.name, "wins!")
                    else:
                        print("Tie!")
                    self.reset()
                    break
