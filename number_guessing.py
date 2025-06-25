import random

# 1: Generate a Random Number
secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100.")

# 2: Loop Until user guesses the number
while True:
    guess = int(input("Take a guess: "))
    attempts += 1   

    if guess < secret_number:
        print("Your guess is too low. Try again!")
    elif guess > secret_number:
        print("Your guess is too high. Try again!")
    else:
        print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
        break