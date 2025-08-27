from game_logic import roll_dice, move_player
from database import update_player_position, log_move, record_game_result

def play_turn(player, game_id):
    """Handle one player's turn."""
    roll = roll_dice()
    old_pos = player["current_position"]
    new_pos = move_player(old_pos, roll)

    # Update DB
    update_player_position(player["id"], new_pos)
    log_move(game_id, player["id"], roll, old_pos, new_pos)

    # Update local data
    player["current_position"] = new_pos

    print(f"🎲 {player['name']} rolled {roll} → moved from {old_pos} to {new_pos}")
    return new_pos == 100  # True if win

def game_loop(players, game_id):
    """Run turns until someone wins."""
    while True:
        for player in players:
            input(f"\n{player['name']}, press Enter to roll...")
            won = play_turn(player, game_id)
            if won:
                print(f"\n🏆 {player['name']} WINS the game! 🏆")
                record_game_result(game_id, player["id"])
                return
