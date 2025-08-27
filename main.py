from database import init_db, add_player, create_game, get_active_game, delete_game
from cli_interface import main_menu, get_player_names, show_leaderboard, choose_resume_or_new
from turn_manager import game_loop

def main():
    init_db()

    while True:
        active_game = get_active_game()
        if active_game:
            choice = choose_resume_or_new()
            if choice == "1":
                print("▶ Resuming saved game...")
                # TODO: load players from DB (small change needed here)
                # players = load_players_for_game(active_game["id"])
                game_loop(players, active_game["id"]) # type: ignore
                continue
            elif choice == "2":
                delete_game(active_game["id"])
                print("🗑️ Saved game deleted. You can start a new one.")

        choice = main_menu()

        if choice == "1":  # Start New Game
            num_players = int(input("Enter number of players: "))
            names = get_player_names(num_players)
            players = [add_player(name) for name in names]
            game = create_game()
            game_loop(players, game["id"]) # type: ignore

        elif choice == "2":
            show_leaderboard()

        elif choice == "3":
            print("👋 Goodbye!")
            break
