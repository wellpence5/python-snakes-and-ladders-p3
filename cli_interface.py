from database import get_leaderboard

def main_menu():
    """Show main menu and return choice."""
    print("\n🎲 Snakes & Ladders")
    print("1. Resume Saved Game")
    print("2. Start New Game")
    print("3. Delete Saved Game")
    print("4. View Leaderboard")
    print("5. Exit")
    return input("Choose an option: ")

def get_player_names(num_players):
    """Ask for player names."""
    names = []
    for i in range(num_players):
        name = input(f"Enter name for Player {i+1}: ")
        names.append(name.strip())
    return names

def show_progress(players):
    """Print all player positions."""
    print("\n📊 Current Positions:")
    for p in players:
        print(f"{p['name']}: {p['current_position']}")

def show_leaderboard():
    """Show top players from database."""
    print("\n🏆 Leaderboard:")
    leaderboard = get_leaderboard()
    if not leaderboard:
        print("No games played yet.")
    else:
        for i, p in enumerate(leaderboard, 1):
            print(f"{i}. {p['name']} - {p['wins']} wins")

def choose_resume_or_new():
    """Ask the user if they want to resume or start fresh."""
    print("\n⚡ You have an unfinished game!")
    print("1. Resume it")
    print("2. Delete it and start new")
    return input("Choose an option: ")

