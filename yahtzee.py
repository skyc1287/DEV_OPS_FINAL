# Yahtzee is a dice game

# Function to roll the dice
def roll_dice():
    return [random.randint(1, 6) for _ in range(5)]

# Function to calculate the score for a given dice combination
def calculate_score(dice):
    score = 0
    for i in range(1, 7):
        count = dice.count(i)
        score += count * i
    return score

# Function to play the game
def play_yahtzee(num_players):
    players = []
    for i in range(num_players):
        players.append({
            'name': f'Player {i+1}',
            'score': 0
        })

    for turn in range(13):
        print(f'Round {turn+1}:')
        for player in players:
            print(f"{player['name']}, it's your turn.")
            input("Press Enter to roll the dice...")
            dice = roll_dice()
            print(f"You rolled: {dice}")
            score = calculate_score(dice)
            print(f"Your score for this round: {score}")
            player['score'] += score
            print(f"Your total score: {player['score']}")
            print()

    print("Game over!")
    print("Final scores:")
    for player in players:
        print(f"{player['name']}: {player['score']}")

# Main program
if __name__ == "__main__":
    num_of_players = int(input("Enter the number of players (1-4): "))
    play_yahtzee(num_of_players)
