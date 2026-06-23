# auth.py
# This file handles sign up, login, guest accounts,
# and input validation (passwords, menus, etc.)

from data import create_player

# These are the special characters allowed in passwords
SPECIAL_CHARS = "!@#$%^&*()_+-=[]{};\':\",.< >?/"


# ============================================
#  INPUT VALIDATION HELPERS
# ============================================

def validate_menu_input(prompt, valid_options):
    # Keep asking until the user picks one of the valid options
    while True:
        choice = input(prompt).strip()
        if choice == "":
            print("  Input cannot be empty. Please try again.")
            continue
        if choice.lower() in valid_options:
            return choice.lower()
        print("  Invalid choice. Please pick from: " + ", ".join(valid_options))


def validate_positive_integer(prompt):
    # Keep asking until the user enters a whole number greater than 0
    while True:
        value = input(prompt).strip()
        if value == "":
            print("  Input cannot be empty. Please enter a positive number.")
            continue
        # Check if it's a valid integer
        try:
            num = int(value)
        except ValueError:
            print("  That is not a valid number. Please try again.")
            continue
        # Check if it's positive
        if num <= 0:
            print("  Please enter a number greater than zero.")
            continue
        return num


def validate_non_empty(prompt):
    # Keep asking until the user types something (not blank)
    while True:
        value = input(prompt).strip()
        if value == "":
            print("  Input cannot be empty. Please try again.")
            continue
        return value


# ============================================
#  PASSWORD VALIDATION
# ============================================

def validate_password(password):
    # Check the password against all the sign-up rules.
    # Returns a list of problems. If the list is empty, the password is good.
    problems = []

    # Rule: reject passwords that are only spaces
    if password.strip() == "":
        problems.append("Password cannot be blank or only spaces.")
        return problems

    # Rule 1: at least 8 characters
    if len(password) < 8:
        problems.append("Password must be at least 8 characters long.")

    # Rule 2: at least one uppercase letter
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if not has_upper:
        problems.append("Password must contain at least one uppercase letter (A-Z).")

    # Rule 3: at least one lowercase letter
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if not has_lower:
        problems.append("Password must contain at least one lowercase letter (a-z).")

    # Rule 4: at least one digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        problems.append("Password must contain at least one number (0-9).")

    # Rule 5: at least one special character
    has_special = False
    for char in password:
        if char in SPECIAL_CHARS:
            has_special = True
            break
    if not has_special:
        problems.append("Password must contain at least one special character (e.g. !@#$%).")

    return problems


def prompt_valid_password():
    # Keep asking until the user enters a password that passes all rules
    while True:
        password = input("  Enter a password: ")
        problems = validate_password(password)
        if len(problems) == 0:
            return password
        # Show what went wrong
        print("\n  Password does not meet the requirements:")
        for problem in problems:
            print("    - " + problem)
        print()


# ============================================
#  GUEST ACCOUNT
# ============================================

def generate_guest_username(players):
    # Find a guest username like guest1, guest2, etc. that isn't taken
    number = 1
    while "guest" + str(number) in players:
        number = number + 1
    return "guest" + str(number)


def get_or_create_guest(players, guest_username):
    # If the guest account doesn't exist yet, create it
    if guest_username not in players:
        create_player(players, guest_username, "Guest", "password")
    return players[guest_username]


# ============================================
#  SIGN UP
# ============================================

def signup(players):
    # Walk the user through creating a new account
    print("\n" + "=" * 40)
    print("        CREATE A NEW ACCOUNT")
    print("=" * 40)

    # Step 1: Pick a username
    while True:
        username = input("  Choose a username: ").strip()

        # Check it's not empty
        if username == "":
            print("  Username cannot be empty.")
            continue

        # Check no spaces
        if " " in username:
            print("  Username cannot contain spaces.")
            continue

        # Check only letters, numbers, and underscores
        valid_chars = True
        for char in username:
            if not (char.isalpha() or char.isdigit() or char == "_"):
                valid_chars = False
                break
        if not valid_chars:
            print("  Username can only have letters, numbers, and underscores.")
            continue

        # Don't allow usernames starting with "guest"
        if username.lower().startswith("guest"):
            print("  Usernames starting with 'guest' are reserved.")
            continue

        # Check the username isn't already taken
        if username in players:
            print("  That username is already taken. Try another one.")
            continue

        break  # username is good

    # Step 2: Pick a display name
    handle = validate_non_empty("  Choose a display name: ")

    # Step 3: Pick a valid password
    password = prompt_valid_password()

    # Step 4: Create the account
    new_player = create_player(players, username, handle, password)
    print("\n  Account created! Welcome, " + handle + "!")
    return new_player


# ============================================
#  LOGIN
# ============================================

def login(players):
    # Let the user log in with their username and password
    print("\n" + "=" * 40)
    print("             LOGIN")
    print("=" * 40)

    while True:
        username = input("  Username (or 'back' to return): ").strip()

        # Let the user go back to main menu
        if username.lower() == "back":
            return None

        if username == "":
            print("  Username cannot be empty.")
            continue

        password = input("  Password: ")

        # Check if username exists
        if username not in players:
            print("  Username not found. Try again or type 'back'.\n")
            continue

        # Check if password matches
        if players[username]["Password"] != password:
            print("  Wrong password. Try again or type 'back'.\n")
            continue

        # Login successful
        print("\n  Welcome back, " + players[username]["Handle"] + "!")
        return players[username]