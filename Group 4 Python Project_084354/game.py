# game.py
# This file has the game logic: playing rounds, deciding winners,
# and running a full match.

import random
from display import display_move, display_result, display_match_result, display_round_score
from auth import validate_menu_input, validate_positive_integer


def get_player_move():
    # Show the menu and let the player pick a move by number
    print()
    print("  Choose your move:")
    print("    [1] Rock")
    print("    [2] Paper")
    print("    [3] Scissors")

    choice = validate_menu_input("  Enter 1, 2, or 3: ", ["1", "2", "3"])

    # Convert the number to the move name
    if choice == "1":
        return "rock"
    elif choice == "2":
        return "paper"
    else:
        return "scissors"


def decide_winner(player_move, computer_move):
    # Figure out who won the round
    # Returns "win", "draw", or "lose" from the player's point of view

    if player_move == computer_move:
        return "draw"

    # Check all the ways the player can win
    if player_move == "rock" and computer_move == "scissors":
        return "win"
    elif player_move == "scissors" and computer_move == "paper":
        return "win"
    elif player_move == "paper" and computer_move == "rock":
        return "win"

    # If it's not a draw and the player didn't win, they lost
    return "lose"


def play_round():
    # Play one round: player picks, computer picks randomly, show result
    player_move = get_player_move()
    computer_move = random.choice(["rock", "paper", "scissors"])

    # Show both moves with ASCII art
    display_move(player_move, computer_move)

    # Figure out who won and show the result banner
    result = decide_winner(player_move, computer_move)
    display_result(result)

    return result


def play_match():
    # Play a full match of multiple rounds
    # Returns the number of wins, draws, and losses

    num_rounds = validate_positive_integer("\n  How many rounds do you want to play? ")
    print("\n  Starting a " + str(num_rounds) + "-round match! Good luck!\n")

    # Keep track of the score
    wins = 0
    draws = 0
    losses = 0

    # Play each round
    for i in range(1, num_rounds + 1):
        print("\n" + "-" * 40)
        print("  ROUND " + str(i) + " of " + str(num_rounds))
        print("-" * 40)

        result = play_round()

        # Update the score
        if result == "win":
            wins = wins + 1
        elif result == "draw":
            draws = draws + 1
        else:
            losses = losses + 1

        # Show running score
        display_round_score(i, wins, draws, losses)

    # Show the final match summary
    display_match_result(wins, draws, losses)

    return wins, draws, losses