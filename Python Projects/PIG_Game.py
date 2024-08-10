import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

print("Rules for the game :")
print("1. Roll the dice during your turn until you get a one to get the maximum score which is 50.")
print("2. Your scores will be added according to the upturned value on dice.")
print("3. If you get a 1, you score will be halved in your next turn.")
print("4. Player who gets the score 50 first wins.\n")


while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 1 < players <= 4:
            break
    else:
        print("Invalid, enter a valid choice")

max_score = 50

scores = [0 for _ in range(players)]

while max(scores) < max_score:
    for i in range(players):
        print("\nThis is player",i+1 , "turn.\n")
        playing = input("Do you want to play the game (y/n): ").lower()
        value = roll()
            
        while True:
            if value == 1:
                scores[i] = int(scores[i] / 2)
                print("\nTurn's over! You got a 1\n\n")
                break
            else:
                print("You got a", value)
                scores[i] += value
                print("Current score of player", i+1 , "is", scores[i])
                if scores[i] > max_score:
                    break
            value = roll()
            playing = input("Do you want to play the game (y/n): ").lower()
        
winner = scores.index(max(scores))
print("Winner is player ",winner +1)

