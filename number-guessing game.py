import random

secret_number = random.randint(1, 20)
attempts = 0
Total_attempt = 5

while attempts < 5:
    guess = int(input("Guess the number between 1 and 20: "))
    attempts += 1

    if guess == secret_number:
        print(f"Correct! It took you {attempts} guesses.")
        break
    elif guess > secret_number:
        print("too high")
    else:
        print("too low")

if guess != secret_number:
    print(f"Out of attempts! The correct answer was {secret_number}.")






