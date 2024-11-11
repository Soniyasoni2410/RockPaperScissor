# Rock, Paper, Scissors Game

A simple Python-based implementation of the classic Rock, Paper, Scissors game. In this game, the user plays against the computer, with the choices being compared to determine the winner based on the classic rules. The program also includes input validation and engaging ASCII art.

## How It Works

1. The computer randomly selects its choice from Rock, Paper, or Scissors using Python's `random.randint()` function.
2. The user is prompted to input their choice:
   - 🪨 Rock = 0
   - 📄 Paper = 1
   - ✂ Scissors = 2
3. The program compares both choices and declares the winner:
   - Rock beats Scissors
   - Paper beats Rock
   - Scissors beats Paper
4. If the user enters an invalid input, the program will ask for a valid choice.
5. Fun ASCII art is used to visually represent each choice.

## Key Features

- **Randomization**: Computer's choice is generated using `random.randint()`.
- **Conditional Logic**: Determines the winner using `if-elif-else` statements.
- **Input Handling**: Handles user input and ensures valid choices.
- **ASCII Art**: Displays visually engaging representations of choices.
- **Error Handling**: Provides feedback for invalid inputs.

## Requirements

- Python 3.x

## How to Run

1. Clone this repository.
2. Navigate to the project directory.
3. Run the game using the command:
   ```bash
   python RockPaperScissors.py

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
