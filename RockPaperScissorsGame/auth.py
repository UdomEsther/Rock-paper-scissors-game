import csv
import os

metadata_file = 'metadata.csv'

def load_players():
    players = {}
    if not os.path.exists(metadata_file):
        # Create a new CSV with the header if it does not exist
        with open(metadata_file, 'w', newline='') as f:
            f.write("Username,Handle,Password,Total Rounds,Total Wins,Total Draws,Total Losses\n")
    else:
        with open(metadata_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                players[row['Username']] = row
    return players

def save_players(players):
    with open(metadata_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=players[next(iter(players))].keys())
        writer.writeheader()
        for player in players.values():
            writer.writerow(player)

def signup(players):
    username = input("Enter desired username: ")
    while username in players:
        username = input("Username already exists. Enter a new one: ")
    
    handle = input("Enter desired handle (display name): ")
    password = input("Enter password: ")
    players[username] = {
        "Username": username,
        "Handle": handle,
        "Password": password,
        "Total Rounds": "0",
        "Total Wins": "0",
        "Total Draws": "0",
        "Total Losses": "0"
    }
    save_players(players)

def login(players):
    username = input("Enter username: ")
    if username in players:
        password = input("Enter password: ")
        if players[username]["Password"] == password:
            return players[username]
    print("Login failed.")
    return None
