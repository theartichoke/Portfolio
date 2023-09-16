import random
from Words import words
import string

def get_valid_word(words):

    word = random.choice(words)

    while '-' in word or ' ' in word:

        word = random.choice(words)

    return word.upper()
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left, and you have used these letters: ", " ".join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))
        user_letter = input("Guess a letter!: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print(f"{user_letter} was not in the word.")

        elif user_letter in used_letters:
            print("Letter has already been used, please pick another.")

        else:
            print("Invalid character, please try again.")
    if lives == 0:
        print(f"You died, the word was {word}")
    else:
        print(f"Congrats! You guess the word, it was {word}")
hangman()