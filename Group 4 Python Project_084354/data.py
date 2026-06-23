# data.py
# This file handles reading and writing player data to metadata.csv.
# All player records are stored in a dictionary in memory while the program runs.

import csv
import os

# The headers for our CSV file, in the exact order required
HEADERS = [
    "Username", "Handle", "Password",
    "Total Rounds", "Total Wins", "Total Draws", "Total Losses",
    "Wins per Round", "Draws per Round", "Losses per Round"
]

# Build the path to metadata.csv in the same folder as this script
CSV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "metadata.csv")


def load_players():
    # Read all player records from the CSV into a dictionary.
    # If the file doesn't exist or is empty, create it with headers.
    players = {}

    # If file doesn't exist, make a new one with just the header row
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)
        return players

    # Try to read the file
    try:
        with open(CSV_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)

            # If the file is empty or has no headers, recreate it
            if reader.fieldnames is None:
                with open(CSV_FILE, "w", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow(HEADERS)
                return players

            # Read each row and add it to our dictionary
            for row in reader:
                try:
                    username = row["Username"]
                    players[username] = {
                        "Username": username,
                        "Handle": row["Handle"],
                        "Password": row["Password"],
                        "Total Rounds": int(row["Total Rounds"]),
                        "Total Wins": int(row["Total Wins"]),
                        "Total Draws": int(row["Total Draws"]),
                        "Total Losses": int(row["Total Losses"]),
                        "Wins per Round": float(row["Wins per Round"]),
                        "Draws per Round": float(row["Draws per Round"]),
                        "Losses per Round": float(row["Losses per Round"]),
                    }
                except (KeyError, ValueError):
                    # If a row is corrupted, just skip it
                    continue
    except Exception:
        # If something goes wrong, start fresh
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)
        return {}

    return players


def save_players(players):
    # Write ALL players back to the CSV file.
    # We overwrite the whole file each time to keep it in sync.
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        writer.writeheader()
        for player in players.values():
            writer.writerow(player)


def create_player(players, username, handle, password):
    # Make a new player record with all stats set to 0, save to CSV
    new_player = {
        "Username": username,
        "Handle": handle,
        "Password": password,
        "Total Rounds": 0,
        "Total Wins": 0,
        "Total Draws": 0,
        "Total Losses": 0,
        "Wins per Round": 0.0,
        "Draws per Round": 0.0,
        "Losses per Round": 0.0,
    }
    players[username] = new_player
    save_players(players)
    return new_player


def update_stats(player, match_wins, match_draws, match_losses):
    # Update a player's stats after a match and recalculate the ratios
    rounds_played = match_wins + match_draws + match_losses

    player["Total Rounds"] = player["Total Rounds"] + rounds_played
    player["Total Wins"] = player["Total Wins"] + match_wins
    player["Total Draws"] = player["Total Draws"] + match_draws
    player["Total Losses"] = player["Total Losses"] + match_losses

    # Recalculate ratios (avoid dividing by zero)
    total = player["Total Rounds"]
    if total > 0:
        player["Wins per Round"] = round(player["Total Wins"] / total, 4)
        player["Draws per Round"] = round(player["Total Draws"] / total, 4)
        player["Losses per Round"] = round(player["Total Losses"] / total, 4)
    else:
        player["Wins per Round"] = 0.0
        player["Draws per Round"] = 0.0
        player["Losses per Round"] = 0.0