# 8 Puzzle Game

This Python application implements a simple 8 Puzzle game using the Pygame library. The goal of the game is to rearrange the numbered tiles from their initial configuration to reach a specific goal configuration. The game provides a graphical interface where users can interact with the puzzle by using keyboard inputs to move the tiles.

## How to Play

1. **Initial State**: 
    - You will be prompted to input the initial state of the puzzle. The initial state represents the starting configuration of the puzzle in a 3x3 grid format.
    - The empty space in the puzzle is represented by the number 0.

2. **Game Interface**: 
    - After providing the initial state, the game window will display the puzzle grid along with the numbered tiles.
    - Use the arrow keys (Up, Down, Left, Right) to move the tiles in the desired direction.
    - Press 'Y' to restart the game if you have solved the puzzle.
    - Press 'N' to quit the game if you have solved the puzzle.

3. **Gameplay**: 
    - Your objective is to rearrange the tiles by sliding them into the empty space to achieve the goal configuration.
    - The goal configuration is predefined within the program.

4. **Winning Condition**: 
    - Once you have successfully arranged the tiles to match the goal configuration, a winning message will be displayed.
    - You will be given the option to restart the game or quit.

## Algorithm Overview

1. **Input Initial State**: 
    - The user inputs the initial configuration of the puzzle, which is represented as a 3x3 array.

2. **Designing Puzzle Interface**: 
    - The program designs the graphical interface to display the puzzle grid and the numbered tiles.

3. **Reading Keyboard Input**: 
    - The program reads keyboard inputs from the user to move the tiles within the puzzle grid.

4. **Updating Data Array**: 
    - Based on the user's input, the program updates the data array to reflect the movement of tiles.

5. **Synchronizing Data Array with Display**: 
    - The program synchronizes the data array with the graphical display to ensure that the display matches the current state of the puzzle.

6. **Comparing with Goal State**: 
    - The program compares the current state of the puzzle with the predefined goal state to determine if the puzzle has been solved.

7. **Continuously Updating Display**: 
    - The program continuously updates the display to reflect any changes made to the puzzle grid.

8. **Winning Condition Check**: 
    - If the puzzle is solved, the program displays a winning message and provides options to restart or quit the game.

## Dependencies

- Python 3.x
- Pygame library

## Stack Used

![Python and Pygame](https://img.shields.io/badge/Python-Pygame-blue)

## How to Run

1. Clone this repository to your local machine.
2. Make sure you have Python and Pygame installed.
3. Navigate to the directory where the repository is cloned.
4. Run the `main.py` file using Python.
5. Follow the on-screen instructions to play the game.

## Credits

This game is developed by Aldovadev.
