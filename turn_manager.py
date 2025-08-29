from game_logic import roll_dice, move_player
from database import update_player_position, log_move, record_game_result

def play_turn(player, game_id):
    #handle one player's turn:
    roll = roll_dice()
    old_pos = player["current_position"]
    #displace the player
    new_pos = move_player(old_pos, roll)
    update_player_position(player["id"], new_pos)
    log_move(game_id, player["id"], roll, old_pos, new_pos)
    #update the local data in memory
    player["current_position"] = new_pos
    print(f"{player['name']} rolled {roll} → moved from {old_pos} to {new_pos}")
    #return True if this player has reached exactly 100 to initiate win
    return new_pos == 100


def game_loop(players, game_id): #main game loop:
    while True:
        for player in players:
            #turn
            input(f"{player['name']}, press Enter to roll...")
            won = play_turn(player, game_id)
            if won:
                print(f" {player['name']} WINS the game!")
                record_game_result(game_id, player["id"])#save winner to database
                return  # End the game
