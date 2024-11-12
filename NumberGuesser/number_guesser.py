import random
#randrange excludes the upper bound limit number
#randint includes the upper bound limit number

userInput = input("Type a number: ")

if userInput.isdigit():
    userInput = int(userInput)

    if userInput <= 0:
        print("Please type a number larger than 0 next time!")
        quit()
else:
    print("Please type a number next time!")

random_number = random.randint(0, userInput)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time!")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("Your guess is above the number!")
    else:
        print("Your guess is below the number!")

print("You got it in", guesses, "guess(es).")