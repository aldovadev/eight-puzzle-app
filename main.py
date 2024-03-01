# Importing necessary modules for the project
from cgitb import text
from pdb import Restart
import pygame
from pygame.locals import QUIT
import sys

# Initial state of the puzzle
initialState = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]

pygame.init()  # Initializing pygame
pygame.display.set_caption(
    "8 PUZZLE | BY : Aldovadev"
)  # Setting the title of the game window
clock = pygame.time.Clock()  # Creating a pygame clock object to control frame rate
screen = pygame.display.set_mode(
    (300, 300)
)  # Creating a game window with dimensions 300x300 pixels
blank = pygame.Surface(
    [100, 100]
)  # Creating a blank surface with dimensions 100x100 pixels
hor = pygame.Surface([4, 300])  # Creating a horizontal surface for puzzle grid lines
ver = pygame.Surface([300, 4])  # Creating a vertical surface for puzzle grid lines
myFont1 = pygame.font.SysFont(
    "verdana", 20
)  # Creating a font object for numbers in the puzzle
myFont2 = pygame.font.SysFont("verdana", 12)  # Creating a font object for messages


# Function to find the position of the empty cell (0) in the puzzle grid
def findZero():
    for i in range(3):
        for j in range(3):
            if initialState[i][j] == 0:
                findZero.iPos = i
                findZero.jPos = j


# Function to display the puzzle grid on the game window
def displayPuzzle():
    findZero()  # Calling the findZero function to get the position of the empty cell
    # Rendering text for each number in the puzzle grid
    text00 = myFont1.render(str(initialState[0][0]), True, (0, 0, 0))
    text01 = myFont1.render(str(initialState[1][0]), True, (0, 0, 0))
    text02 = myFont1.render(str(initialState[2][0]), True, (0, 0, 0))
    text10 = myFont1.render(str(initialState[0][1]), True, (0, 0, 0))
    text11 = myFont1.render(str(initialState[1][1]), True, (0, 0, 0))
    text12 = myFont1.render(str(initialState[2][1]), True, (0, 0, 0))
    text20 = myFont1.render(str(initialState[0][2]), True, (0, 0, 0))
    text21 = myFont1.render(str(initialState[1][2]), True, (0, 0, 0))
    text22 = myFont1.render(str(initialState[2][2]), True, (0, 0, 0))

    screen.fill((255, 255, 255))  # Filling the game window with white color

    x = 0 + (findZero.jPos * 100)  # Calculating the x-coordinate of the empty cell
    y = 0 + (findZero.iPos * 100)  # Calculating the y-coordinate of the empty cell

    # Blitting the surfaces and text to display the puzzle grid
    screen.blit(blank, (x, y))
    screen.blit(hor, (-2, 0))
    screen.blit(hor, (98, 0))
    screen.blit(hor, (198, 0))
    screen.blit(hor, (298, 0))
    screen.blit(ver, (0, -2))
    screen.blit(ver, (0, 98))
    screen.blit(ver, (0, 198))
    screen.blit(ver, (0, 298))
    screen.blit(text00, (40, 40))
    screen.blit(text01, (40, 140))
    screen.blit(text02, (40, 240))
    screen.blit(text10, (140, 40))
    screen.blit(text11, (140, 140))
    screen.blit(text12, (140, 240))
    screen.blit(text20, (240, 40))
    screen.blit(text21, (240, 140))
    screen.blit(text22, (240, 240))


# Function to display the winning message and options to restart or quit the game
def winScreen():
    winText1 = myFont2.render("Selamat!!!", True, (255, 0, 0))
    winText2 = myFont2.render(
        "Kamu Berhasil, Puzzle Telah Terpecahkan.", True, (255, 0, 0)
    )
    winText3 = myFont2.render("Restart Y/N?", True, (255, 0, 0))

    screen.fill((0, 255, 0))  # Filling the game window with green color

    # Blitting the winning messages to the screen
    screen.blit(winText1, (115, 120))
    screen.blit(winText2, (30, 140))
    screen.blit(winText3, (110, 160))


# Function to compare the current puzzle state with the goal state to check if the puzzle is solved
def comparePos():
    global clearedState
    if (
        initialState[0][0] == 1
        and initialState[0][1] == 2
        and initialState[0][2] == 3
        and initialState[1][0] == 8
        and initialState[1][1] == 0
        and initialState[1][2] == 4
        and initialState[2][0] == 7
        and initialState[2][1] == 6
        and initialState[2][2] == 5
    ):
        clearedState = True
    else:
        clearedState = False


# Function to update the puzzle state based on user input
def updatePos():
    global clearedState
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if findZero.jPos != 2:
                    initialState[findZero.iPos][findZero.jPos] = initialState[
                        findZero.iPos
                    ][findZero.jPos + 1]
                    initialState[findZero.iPos][findZero.jPos + 1] = 0
            elif event.key == pygame.K_LEFT:
                if findZero.jPos != 0:
                    initialState[findZero.iPos][findZero.jPos] = initialState[
                        findZero.iPos
                    ][findZero.jPos - 1]
                    initialState[findZero.iPos][findZero.jPos - 1] = 0
            elif event.key == pygame.K_UP:
                if findZero.iPos != 0:
                    initialState[findZero.iPos][findZero.jPos] = initialState[
                        findZero.iPos - 1
                    ][findZero.jPos]
                    initialState[findZero.iPos - 1][findZero.jPos] = 0
            elif event.key == pygame.K_DOWN:
                if findZero.iPos != 2:
                    initialState[findZero.iPos][findZero.jPos] = initialState[
                        findZero.iPos + 1
                    ][findZero.jPos]
                    initialState[findZero.iPos + 1][findZero.jPos] = 0
            elif event.key == pygame.K_y:
                if clearedState == True:
                    clearedState = False
                    # Resetting the puzzle state to initial state
                    initialState[0][0] = 2
                    initialState[0][1] = 8
                    initialState[0][2] = 3
                    initialState[1][0] = 1
                    initialState[1][1] = 6
                    initialState[1][2] = 4
                    initialState[2][0] = 7
                    initialState[2][1] = 0
                    initialState[2][2] = 5
            elif event.key == pygame.K_n:
                if clearedState == True:
                    pygame.quit()
                    sys.exit()


# Main function to run the game loop
def main():
    while True:
        updatePos()  # Updating the puzzle state based on user input
        comparePos()  # Comparing the puzzle state with the goal state
        if clearedState == False:
            displayPuzzle()  # Displaying the puzzle grid if the puzzle is not solved
        else:
            winScreen()  # Displaying the winning message if the puzzle is solved

        pygame.display.update()  # Updating the display


if __name__ == "__main__":
    main()  # Running the main function to start the game
