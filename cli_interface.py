import sqlite3
import time

def display_main_menu():
    """Display the main menu and get user choice"""
    while True:
        print("\n" + "="*40)
        print("    SNAKES & LADDERS GAME")
        print("="*40)
        print("1. Start New Game")
        print("2. View Leaderboard")
        print("3. Exit")
        print("="*40)
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            return "new_game"
        elif choice == "2":
            return "leaderboard"
        elif choice == "3":
            return "exit"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def get_number_of_players():
    """Get the number of players from user input"""
    while True:
        try:
            num_players = int(input("Enter number of players (2-4): ").strip())
            if 2 <= num_players <= 4:
                return num_players
            else:
                print("Please enter a number between 2 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_player_names(num_players):
    """Get names for all players"""
    players = []
    for i in range(num_players):
        while True:
            name = input(f"Enter name for Player {i+1}: ").strip()
            if name:
                players.append(name)
                break
            else:
                print("Name cannot be empty. Please try again.")
    return players

def prompt_for_roll(player_name):
    """Prompt player to roll the dice"""
    input(f"\n{player_name}, press Enter to roll the dice...")
    print("Rolling...")
    time.sleep(1)  # Add a small delay for effect

def display_game_board(players, positions, current_player_idx):
    """Display the current game state in a simple text format"""
    print("\n" + "-"*50)
    print("CURRENT GAME BOARD")
    print("-"*50)
    
    for i, (player, position) in enumerate(zip(players, positions)):
        marker = " ← CURRENT TURN" if i == current_player_idx else ""
        print(f"{player}: Position {position}{marker}")
    
    print("-"*50)

def display_roll_result(roll_value, old_position, new_position):
    """Display the result of a dice roll"""
    print(f"You rolled a {roll_value}!")
    print(f"Moved from position {old_position} to {new_position}")

def display_snake_bite(old_position, new_position):
    """Display message when player bitten by snake"""
    print(f"🐍 OH NO! Snake bite! Slid down from {old_position} to {new_position}")

def display_ladder_climb(old_position, new_position):
    """Display message when player climbs ladder"""
    print(f"🧊 YAY! Ladder climb! Jumped from {old_position} to {new_position}")

def display_winner(winner_name):
    """Display the winner of the game"""
    print("\n" + "🎉"*30)
    print(f"CONGRATULATIONS {winner_name.upper()}! YOU WON THE GAME!")
    print("🎉"*30)

def display_leaderboard():
    """Display the leaderboard from database"""
    try:
        # Connect to database
        conn = sqlite3.connect('snakes_ladders.db')
        cursor = conn.cursor()
        
        # Get top players by wins
        cursor.execute('''
            SELECT name, wins, total_moves 
            FROM players 
            ORDER BY wins DESC, total_moves ASC
            LIMIT 10
        ''')
        
        leaders = cursor.fetchall()
        
        print("\n" + "="*60)
        print("LEADERBOARD - TOP PLAYERS")
        print("="*60)
        
        if leaders:
            print(f"{'Rank':<5} {'Player':<15} {'Wins':<10} {'Total Moves':<12}")
            print("-"*60)
            
            for i, (name, wins, moves) in enumerate(leaders, 1):
                print(f"{i:<5} {name:<15} {wins:<10} {moves:<12}")
        else:
            print("No games played yet. Be the first to win!")
            
        print("="*60)
        
    except sqlite3.Error as e:
        print(f"Error accessing database: {e}")
    finally:
        if conn:
            conn.close()

def display_invalid_move():
    """Display message for invalid move (would exceed 100)"""
    print("Invalid move! You need an exact roll to reach position 100.")

def display_error(message):
    """Display error message"""
    print(f"Error: {message}")

# Example of how the CLI would integrate with the game
def run_cli_interface():
    """Main function to run the CLI interface"""
    while True:
        choice = display_main_menu()
        
        if choice == "new_game":
            # Start new game flow
            num_players = get_number_of_players()
            players = get_player_names(num_players)
            
            print(f"\nStarting new game with players: {', '.join(players)}")
            print("Game is starting...")
            
            # In the actual implementation, this would call the game logic
            # For now, we'll just simulate some interactions
            
            # Simulate a game round
            positions = [0] * num_players
            for i in range(num_players):
                display_game_board(players, positions, i)
                prompt_for_roll(players[i])
                
                # These would come from the game logic
                roll = 5  # Simulated dice roll
                old_pos = positions[i]
                positions[i] += roll
                
                display_roll_result(roll, old_pos, positions[i])
                display_game_board(players, positions, i)
                
            # Simulate game end
            display_winner(players[0])
            
        elif choice == "leaderboard":
            display_leaderboard()
            
        elif choice == "exit":
            print("Thank you for playing! Goodbye!")
            break

# Run the CLI interface if this file is executed directly
if __name__ == "__main__":
    run_cli_interface()