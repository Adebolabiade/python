import random

def guess_number():
    number = random.randint(1, 10)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

guess_number()