import random

def play_round(player_move):
    # Computer randomly selects Rock, Paper, or Scissors
    computer_move = random.choice(['Rock', 'Paper', 'Scissors'])
    result = ""
    
    if player_move == computer_move:
        result = "Draw"
    elif (player_move == 'Rock' and computer_move == 'Scissors') or \
         (player_move == 'Scissors' and computer_move == 'Paper') or \
         (player_move == 'Paper' and computer_move == 'Rock'):
        result = "Win"
    else:
        result = "Loss"
    
    return computer_move, result

def play_match(player):
    rounds = int(input("How many rounds do you want to play? "))
    player_stats = {
        "Total Wins": 0,
        "Total Draws": 0,
        "Total Losses": 0
    }
    
    for _ in range(rounds):
        player_move = input("Choose: Rock, Paper, Scissors: ").strip().capitalize()
        computer_move, result = play_round(player_move)
        
        print(f"Computer chose {computer_move}. You {result.lower()}!")
        
        if result == "Win":
            player_stats["Total Wins"] += 1
        elif result == "Draw":
            player_stats["Total Draws"] += 1
        else:
            player_stats["Total Losses"] += 1
            
    return player_stats
