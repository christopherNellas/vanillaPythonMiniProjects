import random as r
print("Welcome to the Number Guessing Game!")
gameRange = input("Input a number: ")
if gameRange.isdigit():
    gameRange = int(gameRange)
    random_number = r.randint(0,gameRange)
else:
    print("Pls enter a number")
    quit()
incorrect_guesses = 0
while True:
    user_guess = input("Guess the random number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == random_number:
            print(f"Correct! {user_guess} is the random number.")
            break
        elif user_guess > random_number:
            print(f"The random number is less than this {user_guess}")
            incorrect_guesses += 1
            continue
        elif user_guess < random_number:
            print(f"The random number is greater than this {user_guess}")
            incorrect_guesses += 1
            continue
    else:
        print("Pls enter a numbers")
        incorrect_guesses += 1
        continue
print(f"incorrect guesses {incorrect_guesses}")