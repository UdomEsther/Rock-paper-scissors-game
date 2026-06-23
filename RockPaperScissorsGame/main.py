import auth
import game
import display

def main():
    players = auth.load_players()
    display.display_banner()
    
    while True:
        choice = input("1. Play as Guest\n2. Login\n3. Sign Up\n4. Exit\nChoose an option: ")
        if choice == '1':
            print("Playing as Guest")
            guest_username = "Guest"  # You can create a random guest username here if you want.
            player = {"Username": guest_username}
            game.play_match(player)

        elif choice == '2':
            player = auth.login(players)
            if player:
                game.play_match(player)
        
        elif choice == '3':
            auth.signup(players)
        
        elif choice == '4':
            break

if __name__ == "__main__":
    main()
