import random

# Function to roll a dice
def roll_dice():
    return random.randint(1, 6)

# Function to play a turn
def play_turn(player_name, current_position):
    input(f"{player_name}, press Enter to roll the dice...")
    dice_roll = roll_dice()
    print(f"You rolled a {dice_roll}!")
    current_position += dice_roll
    return current_position

# Function to check for snakes and ladders
def check_snakes_and_ladders(position):
    snakes_and_ladders = {
        16: 6,
        47: 26,
        49: 11,
        56: 53,
        62: 19,
        64: 60,
        87: 24,
        93: 73,
        95: 75,
        98: 78
    }
    if position in snakes_and_ladders:
        new_position = snakes_and_ladders[position]
        if new_position > position:
            print(f"Ladder! Climb up to {new_position}!")
        else:
            print(f"Snake! Slide down to {new_position}...")
        return new_position
    return position

# Main game function
def play_snakes_and_ladders():
    player1_position = 1
    player2_position = 1
    while True:
        print(f"Player 1 is at position {player1_position}")
        player1_position = play_turn("Player 1", player1_position)
        player1_position = check_snakes_and_ladders(player1_position)
        if player1_position >= 100:
            print("Player 1 wins!")
            break
        print(f"Player 2 is at position {player2_position}")
        player2_position = play_turn("Player 2", player2_position)
        player2_position = check_snakes_and_ladders(player2_position)
        if player2_position >= 100:
            print("Player 2 wins!")
            break

# Run the game
play_snakes_and_ladders()
