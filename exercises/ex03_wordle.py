"""EX03 - Wordle"""

__author__ = "730559806"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(searched_word: str, searched_letter: str) -> bool:
    """Searches for a letter in a word."""
    assert len(searched_letter) == 1
    i: int = 0
    while i < len(searched_word):
        if searched_word[i] == searched_letter:
            return True
        else:
            i += 1   

    return False


def emojified(guess: str, secret: str) -> str:
    """Produces an emojie telling the user which letters are present"""
    length = len(guess)
    assert len(secret) == length
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    final_boxes: str = ""
    while i < length:
        searched_letter = guess[i]
        if contains_char(secret, searched_letter):
            if secret[i] == searched_letter:
                final_boxes += GREEN_BOX
            else:
                final_boxes += YELLOW_BOX
        else:
            final_boxes += WHITE_BOX
        i += 1
  
    return final_boxes

def input_guess(expected_length: int):
    "Asks for the user to input a guess"
    guess = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        reguess: str = input(f"That wasn't {expected_length} chars! Try again: ")
        if len(reguess) == expected_length:
            guess = reguess

    return guess

  
def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    total_turns: int = 6
    win: bool = False
    current_turn: int = 1
    while current_turn <= total_turns and not win:
        print(f"=== Turn {current_turn}/{total_turns} ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            win = True
        else:
            current_turn += 1
    if win == True:
        print(f"You won in {current_turn}/{total_turns} turns!")
    else:
        print(f"X/6 - Sorry, try again tomorrow!")

    return None

main()
