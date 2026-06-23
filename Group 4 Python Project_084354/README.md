# Rock Paper Scissors - Python Final Project

## How to Run

1. Make sure you have Python 3 installed on your computer.
2. Put all the Python files (`main.py`, `auth.py`, `game.py`, `data.py`, `display.py`) in the same folder.
3. Open a terminal or command prompt, go to that folder, and type:

```
python main.py
```

4. The program will create `metadata.csv` automatically the first time you run it. You do not need to install anything extra — it only uses built-in Python libraries (`csv`, `os`, `random`, `string`).

## Program Structure

We split the project into five files to keep things organized:

- **main.py** — This is the starting point. It shows the main menu and the game menu, and connects all the other files together. It also generates the guest username once when the program starts so it stays the same the whole time.
- **auth.py** — Handles everything related to accounts: signing up with password checks, logging in, creating guest accounts, and all the input validation functions we use across the program (like checking menu choices and making sure numbers are valid).
- **game.py** — Has the actual game logic. It lets the player pick rock, paper, or scissors, randomly picks the computer's move, figures out who won, and runs a full match of multiple rounds.
- **data.py** — Reads and writes player data to `metadata.csv`. When the program starts it loads all the data, and after every match it saves the updated stats back to the file.
- **display.py** — Stores all the ASCII art (welcome banner, hand drawings for rock/paper/scissors, win/lose/draw banners) and has functions to print them.

## Design Decisions

- Usernames can only have letters, numbers, and underscores. No spaces or special characters allowed. Names starting with "guest" are reserved for guest accounts.
- Passwords are stored as plain text in the CSV because the project requires it. In a real app you would hash them.
- When we save player data, we rewrite the whole CSV file each time. This is simple and makes sure the file always matches what is in memory.
- If a player has played zero rounds, the ratio stats (wins per round, etc.) are set to 0.0 to avoid dividing by zero.

## Known Limitations

- Passwords are in plain text (required by the project spec).
- You cannot delete an account once it is created.
- The ASCII art looks best in a terminal that is at least 80 characters wide.