import pandas as pd
import numpy as np

# Function to simulate the dice roll
def roll_dice():
    return np.random.randint(1, 7)

# Function to play the game
def play_game(players):
    num_players = len(players)
    max_position = 100

    # Initialize the players' positions
    player_positions = {f"Player {i+1}": 0 for i in range(num_players)}

    # Initialize the DataFrame to track game progress
    columns = ["Round"] + list(player_positions.keys())
    game_data = pd.DataFrame(columns=columns)

    # Game Loop
    winner = None
    round_num = 1
    while winner is None:
        round_data = [round_num]

        for player, position in player_positions.items():
            dice_roll = roll_dice()
            position += dice_roll

            # Check if the new position exceeds the maximum position
            if position > max_position:
                position = max_position - (position - max_position)

            # Define snake and ladder positions
            snake_ladder = {
                3: 39, 11: 14, 19: 5, 27: 33, 37: 3, 47: 34, 50: 6, 53: 74, 61: 18, 66: 49, 73: 12, 83: 57, 88: 24, 91: 73, 94: 68, 98: 79
            }

            # Check if the player has encountered a snake or ladder
            if position in snake_ladder:
                position = snake_ladder[position]

            player_positions[player] = position
            round_data.append(position)

            # Check if the player has reached the winning position
            if position == max_position:
                winner = player
                break

        # Ensure all rounds have equal length data
        while len(round_data) < len(columns):
            round_data.append(None)

        game_data.loc[len(game_data)] = round_data
        round_num += 1

    return game_data, winner

# Set up players
players = ["Player 1", "Player 2", "Player 3", "Player 4"]

# Play the game
game_results, winner = play_game(players)

# Display game results
print("Game Results:")
print(game_results)
print(f"\nWinner: {winner}")
