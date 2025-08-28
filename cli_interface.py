from database import get_leaderboard

def main_menu():
    """
    Show the main menu to the player.
    Returns:
        str: The option chosen by the player (as text).
    """
    print("\n🎲 Snakes & Ladders")
    print("1. Resume Saved Game")
    print("2. Start New Game")
    print("3. Delete Saved Game")
    print("4. View Leaderboard")
    print("5. Exit")

    # Keep asking until a valid choice is given
    while True:
        choice = input("Choose an option (1-5): ").strip()
        if choice in {"1", "2", "3", "4", "5"}:
            return choice
        print("❌ Invalid choice, please try again.")

def get_player_names(num_players):
    """
    Ask for player names.
    Args:
        num_players (int): Number of players
    Returns:
        list of str: Player names
    """
    names = []
    for i in range(num_players):
        while True:
            name = input(f"Enter name for Player {i+1}: ").strip()
            if name:  # make sure name is not empty
                names.append(name)
                break
            print("❌ Name cannot be empty. Try again.")
    return names

def show_progress(players):
    """
    Show all player positions on the board.
    Args:
        players (list): List of player dictionaries (with 'name' and 'current_position')
    """
    print("\n📊 Current Positions:")
    for p in players:
        print(f"➡ {p['name']}: square {p['current_position']}")

def show_leaderboard():
    """
    Show top players sorted by number of wins.
    Uses database.get_leaderboard().
    """
    print("\n🏆 Leaderboard:")
    leaderboard = get_leaderboard()

    if not leaderboard:
        print("No games played yet.")
        return

    for i, p in enumerate(leaderboard, 1):
        print(f"{i}. {p['name']} - {p['wins']} wins")

def choose_resume_or_new():
    """
    Ask the player if they want to resume the saved game or start fresh.
    Returns:
        str: "1" for resume, "2" for delete & start new
    """
    print("\n⚡ You have an unfinished game!")
    print("1. Resume it")
    print("2. Delete it and start new")

    while True:
        choice = input("Choose an option (1 or 2): ").strip()
        if choice in {"1", "2"}:
            return choice
        print("❌ Invalid choice, please enter 1 or 2.")
