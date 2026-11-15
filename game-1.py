 import random

print("🎲 Welcome to the Multiplayer Dice Roll Game! ")

# Step 1: Get player names
while True:
    try:
        number_of_players = int(input("enter the number of players(2-5): "))
        if 2 <= number_of_players <= 5:
            print(f"success? {number_of_players} players joined the game")
            break
        elif number_of_players < 2:
         print(
             F"At list 2 players are requied to play the game, ({number_of_players} players is not allowed)."
         )
        else:
            print(
                f"Maximium 5 players are allowed to play the game, ({number_of_players} players are too many)."
            )
    except ValueError:
        print("input must be number")

player_names = []
for i in range(number_of_players):
    name = input(f"enter the name of the player {i+1}: ")
    player_names.append(name)

# Step 2: Initialize scores and rounds
scores = {player: 0 for player in player_names}
total_rounds = 3

# Step 3: Run the game for 5 rounds 
for round_number in range(1, total_rounds + 1):
    print(f'\n--- Round {round_number} of {total_rounds} ---')

    for player in player_names:
        input(f"{player}, press enter to roll the dice 🎲...")
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        roll_total =dice1 + dice2

        scores[player] +=roll_total
        print(f"👉 {player} rolled ({dice1}, {dice2}) -> Round Points: {roll_total} | Total Score: {scores[player]}")

# Step 4: Determine the winner after 3 rounds
print("\n-" + "="*50)
print("🏆 Game Over! Final Scores")
print("="*50)

for player, score in scores.items():
    print(f"{player}: {score} points")

# Determine the winner(s)
highest_score =max(scores.values())
winners = [player for player, score in scores.items() if score == highest_score]

print("\n" + "="*50)

#

if len(winners) == 1:
    print(f"🎉 The winner is {winners[0]} with a total score of {highest_score} points!")
else:
    print(f"🤝 It's a tie between {', '.join(winners)} with {highest_score} points!")
    print("🎉 Congratulations to all the winners!")
print("="*50)
