"""
Author: Eric Ayanru
Course: CSE110
Project: Word Guessing Game

Description:
This program is a word guessing game similar to Wordle.
The player must guess a secret word. After each guess, a hint is shown:
- UPPERCASE letter: correct letter, correct position
- lowercase letter: correct letter, wrong position
- _ : letter not in the word

The game continues until the player guesses correctly.
"""

def main():
    secret_word = "puzzle"
    guess_count = 0
    word_length = len(secret_word)

    print("Welcome to the Word Guessing Game!")
    print(f"Hint: {'_ ' * word_length}\n")

    while True:
        guess = input("What is your guess? ").lower()
        guess_count += 1

        # Validate input length
        if len(guess) != word_length:
            print(f"Your guess must be {word_length} letters long.\n")
            continue

        # Check for a correct guess
        if guess == secret_word:
            print("Congratulations! You guessed it!\n")
            break

        # Generate hint
        hint = []
        for i in range(word_length):
            if guess[i] == secret_word[i]:
                hint.append(guess[i].upper())
            elif guess[i] in secret_word:
                hint.append(guess[i].lower())
            else:
                hint.append("_")

        print("Hint: ", " ".join(hint))
        print("Your guess was not correct.\n")

    print(f"Total guesses: {guess_count}")

if __name__ == "__main__":
    main()
