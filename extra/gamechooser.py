import random
num_games = int(input("how many games are you choosing from? "))
games = []
for i in range(num_games):
    game = input(f"enter the name of game {i + 1}: ")
    games.append(game)
chosen_game = random.choice(games)
print(f"the chosen game is: {chosen_game}")