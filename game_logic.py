import random

# Snakes move you backwards, ladders move you forwards
SNAKES_LADDERS = {
    16: 6, 47: 26, 49: 11, 56: 53,
    62: 19, 64: 60, 87: 24, 93: 73,
    95: 75, 98: 78,
    1: 38, 4: 14, 9: 31, 21: 42,
    28: 84, 36: 44, 51: 67,
    71: 91, 80: 100
}

def roll_dice():
    return random.randint(1, 6)

def move_player(position, roll):
    new_position = position + roll
    #If overshoots 100, stay in the same place
    if new_position > 100:
        return position
    if new_position in SNAKES_LADDERS:
        return SNAKES_LADDERS[new_position]

    return new_position
