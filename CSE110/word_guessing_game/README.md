# Word Guessing Game

**Author:** Eric Ayanru  
**Course:** CSE110 – Introduction to Programming  
**Project Type:** Game / Loop Practice  
**Language:** Python

## Description

This program is a fun and interactive **word guessing game** inspired by Wordle.  
Players guess a secret word, and after each guess, the program provides a hint.

**Hint Logic:**
- Uppercase letter = correct letter and position
- Lowercase letter = correct letter, wrong position
- Underscore (_) = letter not in the word

The game continues until the player guesses the correct word.

## How to Run

```bash
python word_guessing_game.py

Sample Output

Welcome to the Word Guessing Game!
Hint: _ _ _ _ _ _

What is your guess? people
Hint: p _ _ _ _ E
Your guess was not correct.

What is your guess? puzzle
Congratulations! You guessed it!

Total guesses: 2