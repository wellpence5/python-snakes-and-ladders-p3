# --- Imports ---
# We bring in helper functions from other files
from database import (
    init_db,
    add_player,
    create_game,
    get_active_game,
    delete_game,
    load_players_for_game,
)
from cli_interface import (
    main_menu,
    get_player_names,
    show_leaderboard,
    choose_resume_or_new,
)
from turn_manager import game_loop


def main():
    """
    Entry point of the Snakes & Ladders game.
    - Checks the database
    - Shows the menu
    - Starts, resumes, or deletes games
    - Keeps looping until user exits
    """

    # Step 0: Make sure the database connection is ready
    init_db()

    # Main loop: keeps showing the menu until the user chooses Exit
    while True:
        # Step 1: Check if there’s already a saved unfinished game
        active_game = get_active_game()

        if active_game:
            # If a saved game exists, ask the player what to do with it
            choice = choose_resume_or_new()

            if choice == "1":
                # Resume the saved game
                print("\n▶ Resuming saved game...")
                players = load_players_for_game(active_game["id"])
                game_loop(players, active_game["id"])
                continue  # After game ends, go back to menu

            elif choice == "2":
                # Delete the old game and start fresh
                delete_game(active_game["id"])
                print("\n🗑️ Saved game deleted.")

        # Step 2: Show the main menu (only if no active game or it was deleted)
        choice = main_menu()

        if choice == "1":
            # --- Start a New Game ---
            try:
                num_players = int(input("\n👥 Enter number of players: "))
            except ValueError:
                print("❌ Please enter a valid number.")
                continue

            # Ask for each player's name
            names = get_player_names(num_players)

            # Add each player to the database
            players = [add_player(name) for name in names]

            # Create a new game record in the database
            game = create_game()

            # Start the actual gameplay loop
            game_loop(players, game["id"])

        elif choice == "2":
            # --- View Leaderboard ---
            show_leaderboard()

        elif choice == "3":
            # --- Exit the Program ---
            print("\n👋 Goodbye! Thanks for playing Snakes & Ladders!")
            break

        else:
            print("❌ Invalid choice. Please pick a menu option (1-3).")


# Run the game only if this file is executed directly
if __name__ == "__main__":
    main()
