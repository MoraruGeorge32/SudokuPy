from difficulty import select_difficulty
from start import start
from sudoku_board import createBoard
import pygame
WIDTH = 550
HEIGHT = 750
window_color = (255,255,255)
def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH,HEIGHT))
    window.fill(window_color)
    pygame.display.update()
    if start(window) == True:
        window.fill(window_color)
        pygame.display.update()
        if select_difficulty(window) == 'Easy':
            window.fill(window_color)
            pygame.display.update()
            createBoard(window,0)
        if select_difficulty(window) == 'Medium':
            window.fill(window_color)
            pygame.display.update()
            createBoard(window,1)
        if select_difficulty(window) == 'Hard':
            window.fill(window_color)
            pygame.display.update()
            createBoard(window,2)
main()