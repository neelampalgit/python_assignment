import random

def guess_the_number():
    number = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != number:
        guess = int(input("Guess the number between 1 and 100: "))
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")

    print(f"Congratulations! You guessed the number in {attempts} attempts.")

guess_the_number()
