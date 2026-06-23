# Rock-paper-scissors-game
A terminal-based Rock Paper Scissors game built with Python featuring user authentication, guest access, persistent CSV-based player statistics, and a full ASCII-art-driven interface.


# Rock, Paper, Scissors — Terminal Game with Authentication & Persistent Stats

A fully-featured, text-based Rock Paper Scissors game built in Python. Unlike a typical beginner version of this game, this project includes user authentication, guest access, persistent player statistics stored in CSV, robust input validation, and an ASCII-art-driven terminal interface.

## Overview

This program simulates a multi-round Rock Paper Scissors match between a human player and a computer opponent. Players can sign up for an account, log in to an existing one, or play as a guest — with all statistics (wins, draws, losses, and win/draw/loss ratios) tracked and saved across sessions in a `metadata.csv` file.

The project was built to demonstrate core software engineering concepts beyond simple game logic, including file I/O, session management, authentication flows, data validation, and modular program design.

## Features

- **Three access modes:** Play as Guest, Login, or Sign Up
- **Persistent player statistics** stored in `metadata.csv`, including total rounds, wins, draws, losses, and calculated ratios
- **Guest account system** with auto-generated, collision-free usernames (e.g., `guest7`) that persist for the duration of a session
- **Secure sign-up flow** with strict password validation (minimum length, uppercase, lowercase, digit, and special character requirements)
- **Robust input validation** across every user-facing prompt — the program never crashes on invalid or unexpected input
- **ASCII art interface** for the welcome banner, move reveals (Rock/Paper/Scissors), round results (Win/Draw/Loss), and final match summary
- **Modular code structure** separating authentication, game logic, data handling, and display rendering

## How It Works

1. On launch, the player chooses to **play as a guest**, **log in**, or **sign up**
2. Once authenticated, the player selects the number of rounds to play
3. Each round, the player picks Rock, Paper, or Scissors (by number, full word, or initial letter) while the computer makes a random choice
4. Results are displayed using ASCII art, with a running score shown after every round
5. At the end of the match, the overall winner is declared and the player's statistics are updated and saved to `metadata.csv`

## Technologies Used

- **Python 3**
- **CSV module** for data persistence
- **Modular file structure** (`main.py`, `auth.py`, `game.py`, `data.py`, `display.py`)

## Project Structure

```
project/
│
├── main.py        # Entry point — main menu loop and session state
├── auth.py        # Sign up, login, and guest account generation
├── game.py        # Round logic, match loop, and result calculation
├── data.py        # CSV read/write operations and player record management
├── display.py     # ASCII art constants and display functions
└── metadata.csv   # Auto-generated at runtime if not already present
```

## Data Model

Each player record (guest or registered) is stored in `metadata.csv` with the following fields:

```
Username, Handle, Password, Total Rounds, Total Wins, Total Draws, Total Losses,
Wins per Round, Draws per Round, Losses per Round
```

The three "per round" fields are derived statistics, recalculated as decimals (e.g., `0.6667`) every time a match is completed.

## Key Design Decisions

- **Guest persistence:** A guest's auto-generated username remains fixed for the entire program run — even across logout/login cycles — and only regenerates when the program is restarted.
- **Password validation as a standalone function:** Implemented independently of the sign-up flow so it can be tested in isolation.
- **ASCII art stored as constants:** All visual elements live in `display.py` rather than being scattered inline through the game logic, keeping the codebase clean and maintainable.

## Edge Cases Handled

- Missing or empty `metadata.csv` on first run
- Guest username collisions across multiple program runs
- Division-by-zero protection when calculating ratios for a player with zero rounds played
- Re-authentication mid-session (logout/login replacing in-memory state correctly)
- Passwords consisting only of whitespace
- Non-numeric or out-of-range input on every menu and prompt

## How to Run

```bash
git clone <repository-url>
cd rock-paper-scissors
python main.py
```

No external dependencies are required beyond the Python standard library.

## Known Limitations

- Usernames are currently validated for uniqueness but not for character restrictions (spaces/special characters are permitted)
- No encryption is applied to stored passwords — they are saved as plain text in `metadata.csv`, which is acceptable for this learning exercise but would need to be addressed before any real-world use

## What I Learned

Building this project reinforced practical skills in file-based data persistence, session and state management, defensive input validation, and structuring a Python program into clean, modular components rather than a single monolithic script.
