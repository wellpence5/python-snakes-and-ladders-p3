from database import get_leaderboard

def main_menu():
    print("-----------------------------------------------------------")
    print("Snakes & Ladders :D")
    print("1. Start New Game")
    print("2. View Leaderboard")
    print("3. Exit")
    print("-----------------------------------------------------------")
    choice = input("Choose an option (1-3): ").strip()
    #validation
    while choice not in {"1", "2", "3"}:
        print("-----------------------------------------------------------")
        print("Oopss!. Please enter 1, 2, or 3.")
        print("-----------------------------------------------------------")
        choice = input("Choose an option (1-3): ").strip()
    return choice

def get_player_names(num_players):
    #Ask for player names and return them as a list.
    #Prevents empty names.
    names = []
    for i in range(num_players):
        while True:
            name = input(f"Enter name for Player {i+1}: ").strip()
            if name:
                names.append(name)
                break
            else:
                print("Name cannot be empty. Try again.")
    return names

def show_progress(players):
    #print all playre positions insa way
    print("Current Positions:")
    for p in players:
        print(f"{p['name']}: {p['current_position']}")

def show_leaderboard():
    print("Leaderboard:")
    leaderboard = get_leaderboard()
    if not leaderboard:
        print("  No games played yet.")
    else:
        for i, p in enumerate(leaderboard, 1):
            print(f"  {i}. {p['name']} —> {p['wins']} wins")

def choose_resume_or_new():
    #Special menu shown when an unfinished game exists.
    print("-----------------------------------------------------------")
    print("You have an unfinished game!")
    print("1. Resume it")
    print("2. Delete it and start afresh")
    print("-----------------------------------------------------------")
    choice = input("Choose an option (1-2): ").strip()
    while choice not in {"1", "2"}:
        print("Invalid choice. Please enter 1 or 2.")
        choice = input("Choose an option (1-2): ").strip()
    return choice
