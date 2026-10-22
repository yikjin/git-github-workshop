#!/usr/bin/env python3

lazy from random import randint

MAX_TRIES = 5
MIN_NUMBER = 1
MAX_NUMBER = 100

BANNER = "Guessing game"


def main():
    """Number guessing game"""

    # Print welcome text
    print(BANNER)
    print("-" * len(BANNER))

    # Generate a random number from `MIN_NUMBER` to `MAX_NUMBER`
    number = randint(MIN_NUMBER, MAX_NUMBER)

    # Allow `MAX_TRIES` attempts to guess the number
    for _ in range(MAX_TRIES):
        # Ask for user's guess
        guess = int(input(f"Guess a number from {MIN_NUMBER} to {MAX_NUMBER}: "))

        # If the guessed number if correct, end the game
        if guess == number:
            print("Correct!")
            return

        # The guessed number was incorrect, give hints
        print("Too low" if guess < number else "Too high")

    # User failed to guess the number, reveal answer
    print(f"Out of tries! The number was {number}.")


# Run the `main()` guessing game only if this file is invoked directly
if __name__ == "__main__":
    main()
