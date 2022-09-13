"""EX02 - One_Shot_Wordle."""

__author__ = "730559806"

secret: str = "python"
guess: str = input("What is your 6-letter guess? ")
i: int = 0
final_boxes: str = " "
letter_exists: bool = False
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

if len(guess) != len(secret):
    while len(guess) != len(secret):
        new_guess: str = input("That was not 6 letters! Try again: ")
        if len(new_guess) == len(secret):
            guess = new_guess

while i < len(secret):
    if guess[i] == secret[i]:
        final_boxes += GREEN_BOX
        i += 1    
    else:
        exists: bool = False
        alternate: int = 0
        while exists is False and alternate < len(secret):
            if guess[i] == secret[alternate]:
                exists = True
            alternate += 1
        if exists is True:
            final_boxes += YELLOW_BOX
        else:
            final_boxes += WHITE_BOX
        i += 1
print(final_boxes)

if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
