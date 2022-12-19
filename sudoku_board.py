import copy
import time
import pygame
import sudoku_utils
from sudoku import Sudoku
WIDTH = 550
HEIGHT = 750
background_color = (251,247,245)
button_color = (17,18,17)
number_color = (86,3,252)
wrong_color = (235,0,20)
pygame.init()
game_font = pygame.font.SysFont('arialms',35)
puzzle = Sudoku(3).difficulty(0.5)
grid = puzzle.board
original_grid = copy.deepcopy(grid)

def drawNumber(window, pos):
    column, line = pos[0], pos[1]
    while True:
        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if grid[line-1][column-1] != 0 and original_grid[line-1][column-1] == grid[line-1][column-1]:
                    return
                if event.key == 48:
                    grid[line-1][column-1] = event.key - 48
                    pygame.draw.rect(window, background_color, (pos[0]*50+5, pos[1]*50 + 5, 50-5, 50-5))
                    pygame.display.update()
                    return
                if(0<event.key-48<10):
                    pygame.draw.rect(window,background_color,(pos[0]*50+5,pos[1]*50+5,50-5,50-5))
                    value = game_font.render(str(event.key-48),True,(0,0,0))
                    window.blit(value,(pos[0]*50+15,pos[1]*50))
                    grid[line-1][column-1] = event.key - 48
                    pygame.display.update()
                    return
                return

def checkBoard(window):
    for line in range(0,9):
        for column in range(0,9):
            if not sudoku_utils.checkRow(line,column,grid):
                width = 4 if line % 3 ==0 else 2
                width1 = 4 if (line+1)%3==0 else 2
                pygame.draw.line(window,wrong_color,(50,50+50*line),(500,50+50*line),width)
                pygame.draw.line(window,wrong_color,(50,50+50*(line+1)),(500,50+50*(line+1)),width1)
                pygame.draw.line(window,wrong_color,(50,50*(line+1)),(50,50*(line+2)),4)
                pygame.draw.line(window,wrong_color,(500,50*(line+1)),(500,50*(line+2)),4)
                pygame.display.update()
                time.sleep(5)
                drawCleanBoard(window,(0,0,0))
                return
            if not sudoku_utils.checkCol(line,column,grid):
                width = 4 if column % 3 ==0 else 2
                width1 = 4 if (column+1)%3==0 else 2
                pygame.draw.line(window,wrong_color,(50+50*column,50),(50+50*column,500),width)
                pygame.draw.line(window,wrong_color,(50+50*(column+1),50),(50+50*(column+1),500),width1)
                pygame.draw.line(window,wrong_color,(50*(column+1),50),(50*(column+2),50),4)
                pygame.draw.line(window,wrong_color,(50*(column+1),500),(50*(column+2),500),4)
                pygame.display.update()
                time.sleep(5)
                drawCleanBoard(window,(0,0,0))
                return
            if not sudoku_utils.checkSquare(line,column,grid):
                squareNr = line//3*3+column//3
                starting_point = 50 + 150*squareNr
                for lineIndex in range(0,4):
                    width = 4 if lineIndex%3==0 else 2
                    pygame.draw.line(window,wrong_color,(starting_point,50*(lineIndex+1)),(starting_point+150,50*(lineIndex+1)),width)
                    pygame.draw.line(window,wrong_color,(starting_point+50*lineIndex,starting_point-150),(starting_point+50*lineIndex,starting_point),width)
                pygame.display.update()
                time.sleep(5)
                drawCleanBoard(window,(0,0,0))
                return
    countZero = 0
    for line in grid:
        countZero = countZero + line.count(0)
    if not countZero:
        drawCleanBoard(window,(0,255,0))





def drawCleanBoard(window,color):
    for gridLines in range(0,10):
        width = 4 if not gridLines % 3 else 2
        pygame.draw.line(window,color,(50+50*gridLines,50),(50+50*gridLines,500),width)
        pygame.draw.line(window,color,(50,50+50*gridLines),(500 ,50+50*gridLines), width)
    pygame.display.update()
    return

def createBoard():
    window = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Sudoku")
    window.fill(background_color)
    for gridLines in range(0,10):
        width = 4 if not gridLines % 3 else 2
        pygame.draw.line(window,(0,0,0),(50+50*gridLines,50),(50+50*gridLines,500),width)
        pygame.draw.line(window,(0,0,0),(50,50+50*gridLines),(500 ,50+50*gridLines), width)
    pygame.display.update()

    for line in range(0,len(grid[0])):
        for column in range(0,len(grid[0])):
            if(0<grid[line][column]<10):
                value = game_font.render(str(grid[line][column]),True,number_color)
                window.blit(value,((column+1)*50+15,(line+1)*50))
    pygame.display.update()

    pygame.draw.rect(window,button_color,(50,WIDTH+100,120,50))
    value = game_font.render("Check",True,(255,255,255))
    window.blit(value,(60,WIDTH+100))
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                print(pos)
                if 49 < pos[0] < 170 and WIDTH+100 < pos[1] < WIDTH+150:
                    checkBoard(window)
                else:
                    drawNumber(window, (pos[0]//50,pos[1]//50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return