import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
while True:
    userInput = input("Type Rock / Paper / Scissors or Q to quit: ").lower()
    if userInput == "q":
        break

    if userInput not in options:
        continue

    randomNumber = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[randomNumber]
    print("Computer picked: ", computer_pick )

    if userInput == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif userInput == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif userInput == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif userInput == computer_pick:
        print("Draw. You picked the same item")

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times")
print("THe computer won", computer_wins, "times")
print("Goodbye")