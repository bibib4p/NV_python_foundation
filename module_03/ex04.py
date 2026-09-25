# Guess the Number

import random

attempts = 5
count = 1

difficulty = input("Choose a difficulty:\n1. Easy\n2. Hard\nDifficulty: ").strip().replace(".", "").title()

while difficulty != "1" and difficulty != "2":
    print("\nPlease Enter a Valid Level!")
    difficulty = input("Choose a difficulty:\n1. Easy\n2. Hard\nDifficulty: ").strip().replace(".", "").title()

if difficulty == "1":
    correct_number = random.randint(1, 10)
    print("\nChoose a secret number between 1 and 10. You have 5 attempts to guess it!")
else:
    correct_number = random.randint(1, 30)
    print("\nChoose a secret number between 1 and 30. You have 5 attempts to guess it!")

guess = int(input("Type your guess: "))

while guess != correct_number and attempts > 1:
    attempts -= 1
    if guess > correct_number:
        print(f"Too High. Attempts left: {attempts}")
    else:
        print(f"Too Low. Attempts left: {attempts}")
    count += 1
    guess = int(input("\nType your guess: "))

if guess == correct_number:
    print(f"Correct! You found it in {count} attempts!\n")
else:
    print(f"Nice Try! You are out of attempts.\nThe number was {correct_number}.")
