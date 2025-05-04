import random

snakes = {27: 1, 21: 9, 17: 4, 19: 7}
ladders = {3: 22, 5: 8, 11: 26, 20: 29}
player_pos = {"Player 1": 0, "Player 2": 0}

def roll_dice():
    return random.randint(1, 6)

def move_player(player, pos):
    dice = roll_dice()
    print(f"{player} rolled a {dice}")
    if pos + dice > 100:
        print(f"{player} needs exact roll to reach 100.")
        return pos
    pos += dice
    if pos in snakes:
        print(f"{player} bitten by a snake at {pos}")
        pos = snakes[pos]
    elif pos in ladders:
        print(f"{player} climbed a ladder at {pos}")
        pos = ladders[pos]
    print(f"{player} is now at {pos}\n")
    return pos

def check_winner(player, pos):
    if pos == 100:
        print(f"{player} wins the game!")
        return True
    return False

def play_game():
    print("Welcome to Snake and Ladder Game")
    while True:
        for player in player_pos:
            input(f"{player}'s turn. Press Enter to roll...")
            player_pos[player] = move_player(player, player_pos[player])
            if check_winner(player, player_pos[player]):
                return

if __name__ == "__main__":
    play_game()
