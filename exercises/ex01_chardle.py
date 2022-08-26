"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730559806"

guess: str = input("Enter a 5-character word: ")
instance: int = 0
if len(guess) == 5:
    char: str = input("Enter a single character: ")
    if len(char) == 1:
        print("Searching for " + char + " in " + guess)
        if guess[0] == char:
            print(char + " found at index 0")
            if guess[0] == char:
                instance += 1
        if guess[1] == char:
            print(char + " found at index 1")
            if guess[1] == char:
                instance += 1
        if guess[2] == char:
            print(char + " found at index 2")
            if guess[2] == char:
                instance += 1
        if guess[3] == char:
            print(char + " found at index 3")
            if guess[3] == char:
                instance += 1
        if guess[4] == char:
            print(char + " found at index 4")
            if guess[4] == char:
                instance += 1

        if instance == 0:
            print("No instances of " + char + " found in " + guess)
        if instance == 1:
            print(str(instance) + " instance of " + char + " found in " + guess)
        if instance > 1:
            print(str(instance) + " instances of " + char + " found in " + guess)
    else:
        print("Error: Character must be a single character")
else:
    print("Error: Word must contain 5 letters")
