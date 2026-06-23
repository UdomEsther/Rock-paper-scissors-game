# main.py
# This is the main file that runs the Rock Paper Scissors game.
# It shows the menus and connects everything together.

from data import load_players, save_players, update_stats
from auth import generate_guest_username, get_or_create_guest, signup, login, validate_menu_input
from game import play_match
from display import display_banner, display_goodbye


def show_stats(player):
    # Print the player's current statistics
    print("\n" + "=" * 40)
    print("  Stats for: " + player["Handle"] + " (" + player["Username"] + ")")
    print("=" * 40)
    print("  Total Rounds  : " + str(player["Total Rounds"]))
    print("  Total Wins    : " + str(player["Total Wins"]))
    print("  Total Draws   : " + str(player["Total Draws"]))
    print("  Total Losses  : " + str(player["Total Losses"]))
    print("  Wins/Round    : " + str(player["Wins per Round"]))
    print("  Draws/Round   : " + str(player["Draws per Round"]))
    print("  Losses/Round  : " + str(player["Losses per Round"]))
    print("=" * 40)


def game_menu(player, players):
    # This is the menu shown after a player is logged in.
    # They can play, view stats, or log out.

    while True:
        print("\n  Logged in as: " + player["Handle"] + " (" + player["Username"] + ")")
        print()
        print("  +============================+")
        print("  |       GAME MENU            |")
        print("  +============================+")
        print("  |  [1] Play                  |")
        print("  |  [2] View My Stats         |")
        print("  |  [3] Logout                |")
        print("  +============================+")

        choice = validate_menu_input("  Pick an option (1-3): ", ["1", "2", "3"])

        if choice == "1":
            # Play a match
            wins, draws, losses = play_match()

            # Save the results to the player's stats
            update_stats(player, wins, draws, losses)
            save_players(players)
            print("  Your stats have been saved!")

        elif choice == "2":
            # Show the player's stats
            show_stats(player)

        elif choice == "3":
            # Log out and go back to main menu
            print("\n  Goodbye, " + player["Handle"] + "! Logging out...\n")
            break


def main():
    # This is where the program starts

    # Show the welcome banner
    display_banner()

    # Load player data from the CSV file (creates it if it doesn't exist)
    players = load_players()

    # Generate a guest username for this session
    # This stays the same for the whole time the program is running
    guest_username = generate_guest_username(players)

    # Main menu loop - keeps running until the user chooses to exit
    while True:
        print()
        print("  +============================+")
        print("  |       MAIN MENU            |")
        print("  +============================+")
        print("  |  [1] Play as Guest         |")
        print("  |  [2] Login                 |")
        print("  |  [3] Sign Up               |")
        print("  |  [4] Exit                  |")
        print("  +============================+")

        choice = validate_menu_input("  Pick an option (1-4): ", ["1", "2", "3", "4"])

        if choice == "1":
            # Guest mode - reuse the same guest account for this run
            player = get_or_create_guest(players, guest_username)
            print("\n  Playing as " + player["Username"] + ". Have fun!")
            game_menu(player, players)

        elif choice == "2":
            # Login with existing account
            player = login(players)
            if player is not None:
                game_menu(player, players)

        elif choice == "3":
            # Create a new account (auto-login after)
            player = signup(players)
            game_menu(player, players)

        elif choice == "4":
            # Exit the program
            display_goodbye()
            break


# This makes sure main() only runs when we run this file directly
if __name__ == "__main__":
    main()