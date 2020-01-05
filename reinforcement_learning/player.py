"""
This file contains the player class that represents a player that will be either p1 or p2 in the state class. These
objects will be used to pick move selections and update the states_value dictionary with new q values.
"""

import numpy as np
import pickle


class Player:
    """
    This class has two main methods, the pick_action method and the reward player method. In the pick_action method,
    the exp_rate variable will determine the percentage that a random action is picked or the action that has the most
    positive q value in the states_value dictionary. In this instance the states_value dictionary will represent the
    q table in most other q learning problems. The reward player function will be called after a game is won and provide
    rewards to each value in the state_value dictionary that was used.
    """
    def __init__(self, name, exp_rate=0.3):
        self.name = name
        self.exp_rate = exp_rate
        self.states_value = {}
        self.states = []
        self.decay_gamma = 0.9
        self.learning_rate = 0.25

    def get_key(self, board):
        """
        :param board: board representation
        :return: unique key for states_value dictionary to represent the current state of the board
        """
        return str(board)

    def pick_action(self, positions, current_board, symbol):
        """
        Will choose an action for the computer. The exp_rate will determine how often the choice is random. If the
        exp_rate is at 0.3, 30% of the time the action will be random. Otherwise, the action will be decided by the
        highest value in the states_value dictionary.
        :param positions: positions available on the board
        :param current_board: current board list
        :param symbol: 1 or -1 for which player is playing
        :return: index of the move on the board (1-9)
        """
        if np.random.uniform(0, 1) <= self.exp_rate:
            index = np.random.choice(positions)
        else:
            max_q = -999999
            for position in positions:
                next_board = current_board.copy()
                next_board[position] = symbol
                next_board_key = self.get_key(next_board)
                value = 0 if self.states_value.get(next_board_key) is None else self.states_value.get(next_board_key)
                if value >= max_q:
                    max_q = value
                    index = position
        return index

    def reward_player(self, reward):
        """
        Iterates through the reversed states list to update the values in the states value dictionary with the formula:
        Qt(s,a)=Qt−1(s,a)+αTDt(a,s)
        :param reward: reward value given to this player at the end of the game (0-1)
        """
        for state in reversed(self.states):
            if self.states_value.get(state) is None:
                self.states_value[state] = 0
            self.states_value[state] += self.learning_rate * (self.decay_gamma * reward - self.states_value[state])
            reward = self.states_value[state]

    def add_state(self, state):
        """
        Adds a state ti tge state list
        :param state: state as a key
        """
        self.states.append(state)

    def reset(self):
        """
        Clears states
        """
        self.states = []

    def save_policy(self):
        """
        Saves the policy in bytes to the file policy_(name of player)
        """
        with open('policy_' + str(self.name), 'wb') as f:
            pickle.dump(self.states_value, f)

    def load_policy(self, file_name):
        """
        Read the policy from a file name and update the states value dictionary
        :param file_name: name of the policy file
        """
        with open(file_name, 'rb') as f:
            self.states_value = pickle.load(f)
