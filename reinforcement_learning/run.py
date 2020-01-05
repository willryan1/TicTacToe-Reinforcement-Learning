"""
This file trains two tic tac toe bots using reinforcement learning with 80000 episodes and allows you to play against
either as x or o
"""

import sys
from state import State
from player import Player
from human_player import HumanPlayer


if __name__ == "__main__":
    # Initializes both bot players
    p1 = Player("player_1")
    p2 = Player("player_2")

    # Creates a state with both players
    state = State(p1, p2)

    # Train 80000 times and save both players' policies
    print("Training...")
    state.train(70000)
    p1.save_policy()
    p2.save_policy()

    # Create a new player that never plays randomly
    player = Player("Computer", exp_rate=0)

    # Initialize the user
    human = HumanPlayer(input("What is your name: "))
    # Choose who to play as and play the game
    while True:
        x_or_o = input("Would you like to be x or o (x, o): ")
        if x_or_o.lower() == 'o':
            state = State(player, human)
            player.load_policy("policy_player_1")
            break
        elif x_or_o.lower() == 'x':
            state = State(human, player)
            player.load_policy("policy_player_2")
            state.print_board()
            break
        else:
            print("Please enter x or o.")

    while True:
        state.play()
        while True:
            play_again = input("Would you like to play again (y,n): ")
            if play_again.lower() == "n":
                sys.exit(0)
            elif play_again.lower() == "y":
                break
            else:
                print("Sorry I didn't understand that. Can you try again.")
        while True:
            x_or_o = input("Would you like to be x or o (x, o): ")
            if x_or_o.lower() == 'o':
                state = State(player, human)
                player.load_policy("policy_player_1")
                break
            elif x_or_o.lower() == 'x':
                state = State(human, player)
                player.load_policy("policy_player_2")
                state.print_board()
                break
            else:
                print("Please enter x or o.")

    # state.visualize_train()
