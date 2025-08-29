
# We bring in everyones functions from other tasks
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
    #this is the entry point of the game.
    init_db() #make sure database actually still works
    while True:#min loop to keeps showing the menu until the user chooses Exit
        # check if there’s already a saved unfinished game
        active_game = get_active_game()
        if active_game:
            #if a saved game exists, ask the player what to do with it
            choice = choose_resume_or_new()
            if choice == "1":
                # Resume the saved game
                print("Resuming saved game :D...")
                players = load_players_for_game(active_game["id"])
                game_loop(players, active_game["id"])
                continue  #after game ends, go back to menu
            elif choice == "2":
                #delete the old game and start fresh
                delete_game(active_game["id"])
                print("Old game gone to make room. Gonna add more saves next update")
        #show the main menu(only if no active game or it was deleted)
        choice = main_menu()
        if choice == "1":
            #starting a New Game
            try:
                num_players = int(input("Enter number of players: "))
            except ValueError:
                print("Try putting a number instead.")
                continue
            #getting names
            names = get_player_names(num_players)
            #put each player to the database
            players = [add_player(name) for name in names]
            #create a new game record in the database
            game = create_game()
            #start the actual gameplay loop
            game_loop(players, game["id"])
        elif choice == "2":
            #view Leaderboard
            show_leaderboard()
        elif choice == "3":
            print("Goodbye! Give us a five star rating on play store for good luck :P")
            break

        else:
            print("Oops XuX.You had 3 choices.")

if __name__ == "__main__":
    main()
