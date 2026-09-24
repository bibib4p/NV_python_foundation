# Guess the Number

import random

correct_number = random.randint(1, 10)
attempts = 5
count = 1

print("Choose a secret number between 1 and 10. You have 5 attempts to guess it!")
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
    print("Wrong. You have 0 attempt left\n")
