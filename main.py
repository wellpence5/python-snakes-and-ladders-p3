# --- Imports ---
# We bring in helper functions from the other files
from database import (
    init_db,
    add_player,
    create_game,
    get_active_game,
    delete_game,
    load_players_for_game,
)
from cli_interface import main_menu, get_player_names, show_leaderboard, choose_resume_or_new
from turn_manager import game_loop


def main():
    """
    Entry point of the Snakes & Ladders game.
    Handles menu navigation and game start/resume logic.
    """

    # First, check that the database connection works
    init_db()

    # Main program loop (keeps running until user chooses Exit)
    while True:
        # Step 1: Check if there's a saved (unfinished) game
        active_game = get_active_game()

        if active_game:
            # If there’s a saved game, ask the user what to do
            choice = choose_resume_or_new()

            if choice == "1":
                # Resume old game
                print("\n▶ Resuming saved game...")
                players = load_players_for_game(active_game["id"])
                game_loop(players, active_game["id"])
                continue  # After game ends, return to main loop

            elif choice == "2":
                # Delete old game and start fresh
                delete_game(active_game["id"])
                print("\n🗑️ Saved game deleted.")

        # Step 2: Show the main menu
        choice = main_menu()

        if choice == "1":
            # --- Start a New Game ---
            num_players = int(input("\nEnter number of players: "))

            # Collect player names from user
            names = get_player_names(num_players)

            # Add each player to the database
            players = [add_player(name) for name in names]

            # Create a new game record in the database
            game = create_game()

            # Run the main gameplay loop
            game_loop(players, game["id"])

        elif choice == "2":
            # --- View Leaderboard ---
            show_leaderboard()

        elif choice == "3":
            # --- Exit the Program ---
            print("\n👋 Goodbye! Thanks for playing.")
            break


# This makes sure the game runs only if the file
# is executed directly (not when imported elsewhere)
if __name__ == "__main__":
    main()
