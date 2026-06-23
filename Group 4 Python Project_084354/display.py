# display.py
# This file has all the ASCII art and print functions for the game.
# We keep art here so it doesn't clutter the game logic.

# ---- Welcome Banner ----
BANNER = """
 ____  ____  ____
|  _ \\|  _ \\/ ___|
| |_) | |_) \\___ \\
|  _ <|  __/ ___) |
|_| \\_\\_|   |____/

Rock  Paper  Scissors
"""

# ---- ASCII art for each move ----
ROCK_ART = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER_ART = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

SCISSORS_ART = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# ---- Round result banners ----
WIN_BANNER = """
+========================+
|      YOU WIN!          |
+========================+
"""

DRAW_BANNER = """
+========================+
|      IT'S A DRAW!      |
+========================+
"""

LOSE_BANNER = """
+========================+
|      YOU LOSE!         |
+========================+
"""

# ---- Match result banners ----
MATCH_WIN = """
+================================+
|   CONGRATULATIONS!             |
|   YOU WON THE MATCH!           |
+================================+
"""

MATCH_LOSE = """
+================================+
|   BETTER LUCK NEXT TIME!       |
|   The computer won the match.  |
+================================+
"""

MATCH_DRAW = """
+================================+
|   IT'S A TIE!                  |
|   The match ended in a draw.   |
+================================+
"""

GOODBYE = """
+================================+
|  Thanks for playing! Bye!      |
+================================+
"""


def display_banner():
    # Print the welcome banner when the program starts
    print(BANNER)


def display_move(player_move, computer_move):
    # Show ASCII art for both the player and computer moves
    print("\n" + "=" * 40)

    print("  YOUR MOVE: " + player_move.upper())
    if player_move == "rock":
        print(ROCK_ART)
    elif player_move == "paper":
        print(PAPER_ART)
    else:
        print(SCISSORS_ART)

    print("  COMPUTER'S MOVE: " + computer_move.upper())
    if computer_move == "rock":
        print(ROCK_ART)
    elif computer_move == "paper":
        print(PAPER_ART)
    else:
        print(SCISSORS_ART)

    print("=" * 40)


def display_result(result):
    # Print the win/draw/lose banner for one round
    if result == "win":
        print(WIN_BANNER)
    elif result == "draw":
        print(DRAW_BANNER)
    else:
        print(LOSE_BANNER)


def display_round_score(round_num, wins, draws, losses):
    # Print the running score after each round
    print("-" * 35)
    print("  Score after Round " + str(round_num) + ":")
    print("    You: " + str(wins) + "  |  Draws: " + str(draws) + "  |  Computer: " + str(losses))
    print("-" * 35)


def display_match_result(wins, draws, losses):
    # Print the final match summary with the right banner
    print("\n" + "=" * 40)
    print("         MATCH SUMMARY")
    print("=" * 40)
    print("  Rounds Won   : " + str(wins))
    print("  Rounds Drawn : " + str(draws))
    print("  Rounds Lost  : " + str(losses))
    print("=" * 40)

    if wins > losses:
        print(MATCH_WIN)
    elif losses > wins:
        print(MATCH_LOSE)
    else:
        print(MATCH_DRAW)


def display_goodbye():
    # Print goodbye message when the user exits
    print(GOODBYE)