# Training exercise for practicing python hangman game

exercise which allows you to remember the different bases of python. With the use of control structures and the functionality of types. To train, we will set up a hangman game in the terminal without a graphical interface with random words with the suggestion of a letter via the input function with a life point system.

## Features

- Random selection of a secret word from a predefined list.
- Ability to enter a letter each round.
- Display of the word to be guessed in a masked form (un-guessed letters are represented by underscores).
- Life points counter that decreases with each incorrect guess.
- Messages indicating the player's progress and the final outcome (win or lose).

## Prerequisites

To run this game, you will need Python installed on your machine. This game has been tested with Python 3.9, but it should work with other versions of Python 3 as well.

## How to Play

1. Clone the repository or download the files to your machine.
2. Open a terminal or command prompt.
3. Navigate to the folder containing the game file.
4. Run the script by typing `python index.py` in your terminal.

## Game Rules

- At the start of the game, a secret word is chosen randomly and the player has 10 life points.
- The player suggests letters one at a time.
- If the suggested letter is in the word, it appears in the correct position in the masked word.
- If the letter is not in the word, the player loses a life point.
- The game continues until the player guesses the entire word or loses all their life points.
