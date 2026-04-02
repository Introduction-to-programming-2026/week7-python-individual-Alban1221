# Project 2 — Number Guessing Game
# Author: your name here

import random

# ⭐ Bonus — difficulty selection
print("Choose difficulty:")
print("(1) Easy 1-10  (2) Medium 1-50  (3) Hard 1-100")
choice = input("Enter 1, 2, or 3: ")

if choice == "1":
    max_num = 10
elif choice == "2":
    max_num = 50
elif choice == "3":
    max_num = 100
else:
    print("Invalid choice, defaulting to Easy.")
    max_num = 10

# Step 1 — Pick a random number
secret = random.randint(1, max_num)

# Step 2 — Counter
guesses = 0

# Step 3 — First guess
guess = int(input(f"Guess a number between 1 and {max_num}: "))

# Step 4 — Loop until correct
while guess != secret:
    guesses += 1

    if guess < secret:
        print("Too low!")
    else:
        print("Too high!")

    guess = int(input("Try again: "))

# count the final correct guess
guesses += 1

print(f"Correct! You got it in {guesses} guesses.")