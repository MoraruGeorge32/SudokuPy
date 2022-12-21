import copy
import time
import pygame
import sudoku_utils
from sudoku import Sudoku
button_color = (17,18,17)
number_color = (86,3,252)
wrong_color = (235,0,20)
WIDTH = 550
HEIGHT = 750
background_color = (251,247,245)

def drawNumber(window, pos, game_font, grid, original_grid):
    global background_color
    column, line = pos[0], pos[1]
    width_first_col = 4 if (pos[0]-1)%3 == 0 else 2
    width_second_col = 4 if (pos[0])%3 == 0 else 2
    width_first_line = 4 if (pos[1]-1)%3 == 0 else 2
    width_second_line = 4 if (pos[1])%3 == 0 else 2
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
                    pygame.draw.rect(window, background_color, (pos[0]*50+5, pos[1]*50 + 5, 50-10, 50-10))
                    pygame.draw.line(window,(0,0,0),(pos[0]*50,pos[1]*50), (pos[0]*50 + 50,pos[1]*50),width_first_line)
                    pygame.draw.line(window,(0,0,0),(pos[0]*50,pos[1]*50), (pos[0]*50,pos[1]*50+50),width_first_col)
                    pygame.draw.line(window,(0,0,0),(pos[0]*50+50,pos[1]*50), (pos[0]*50 + 50,pos[1]*50+50),width_second_col)
                    pygame.draw.line(window,(0,0,0),(pos[0]*50,pos[1]*50+50), (pos[0]*50 + 50,pos[1]*50+50),width_second_line)
                    pygame.display.update()
                    return
                if(0<event.key-48<10):
                    pygame.draw.rect(window,background_color,(pos[0]*50+5,pos[1]*50+5,50-10,50-10))
                    value = game_font.render(str(event.key-48),True,(0,0,0))
                    window.blit(value,(pos[0]*50+15,pos[1]*50))
                    grid[line-1][column-1] = event.key - 48
                    pygame.draw.line(window,(0,0,0),(pos[0]*50,pos[1]*50), (pos[0]*50 + 50,pos[1]*50),width_first_line)
                    pygame.draw.line(window,(0,0,0),(pos[0]*50,pos[1]*50), (pos[0]*50,pos[1]*50+50),width_first_col)
                    pygame.draw.line(window,(0,0,0),(pos[0]*50+50,pos[1]*50), (pos[0]*50 + 50,pos[1]*50+50),width_second_col)
                    pygame.draw.line(window,(0,0,0),(pos[0]*50,pos[1]*50+50), (pos[0]*50 + 50,pos[1]*50+50),width_second_line)
                    pygame.display.update()
                    return
                return

def checkBoard(window, grid):
    congrats_font = pygame.font.SysFont("arialms",35, True)
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
                starting_point_x = 50 + 150*(squareNr%3)
                starting_point_y = 50 + 150*(squareNr//3)
                for lineIndex in range(0,4):
                    width = 4 if lineIndex%3==0 else 2
                    pygame.draw.line(window,wrong_color,(starting_point_x,50*lineIndex+starting_point_y),(starting_point_x+150,50*lineIndex+starting_point_y),width)  #horizontal lines
                    pygame.draw.line(window,wrong_color,(50*lineIndex+starting_point_x,starting_point_y),(50*lineIndex+starting_point_x,starting_point_y+150),width) #vertical lines
                pygame.display.update()
                time.sleep(5)
                drawCleanBoard(window,(0,0,0))
                return
    countZero = 0
    for line in grid:
        countZero = countZero + line.count(0)
    if not countZero:
        drawCleanBoard(window,(0,255,0))
        congrats_text = congrats_font.render("Congratulations! You won!",True,(0,255,0))
        window.blit(congrats_text,(30,570))
        pygame.draw.rect(window, (255,255,255), (400, WIDTH+100, 120, 50))
        pygame.display.update()
        time.sleep(5)
        pygame.quit()

def drawCleanBoard(window,color):
    for gridLines in range(0,10):
        width = 4 if not gridLines % 3 else 2
        pygame.draw.line(window,color,(50+50*gridLines,50),(50+50*gridLines,500),width)
        pygame.draw.line(window,color,(50,50+50*gridLines),(500 ,50+50*gridLines), width)
    pygame.display.update()
    return

def replaceNoneWithZero(grid):
    new_grid = []
    for line in grid:
        array = [] 
        for element in line:
            if element is None:
                array.append(0)
            else:
                array.append(element)
        new_grid.append(array)
    return new_grid

def createBoard(window,difficulty_factor):
    timer_sec = 0
    if difficulty_factor==0:
        puzzle = Sudoku(3).difficulty(0.4)
        timer_sec = 300
    elif difficulty_factor==1:
        puzzle = Sudoku(3).difficulty(0.6)
        timer_sec = 600
    elif difficulty_factor==2:
        puzzle = Sudoku(3).difficulty(0.8)
        timer_sec = 1200
    
    
    grid = puzzle.board
    grid = replaceNoneWithZero(grid)
    original_grid = copy.deepcopy(grid)
    
    game_font = pygame.font.SysFont('arialms',35)
    timer_text = game_font.render(time.strftime('%M:%S',time.gmtime(timer_sec)),True,(0,0,0))
    timer = pygame.USEREVENT + 1
    pygame.time.set_timer(timer,1000)
    pygame.display.set_caption("Sudoku")

    new_grid = []
    for line in grid:
        array = [] 
        for element in line:
            if element is None:
                array.append(0)
            else:
                array.append(element)
        new_grid.append(array)
    grid = new_grid # 103-112 - replacing all the Nones from the board generated by py-sudoku with 0

    for gridLines in range(0,10):
        width = 4 if not gridLines % 3 else 2
        pygame.draw.line(window,(0,0,0),(50+50*gridLines,50),(50+50*gridLines,500),width)
        pygame.draw.line(window,(0,0,0),(50,50+50*gridLines),(500 ,50+50*gridLines), width)
    pygame.display.update() # 116-120 - drawing all the lines of the grid GUI

    for line in range(0,len(grid[0])):
        for column in range(0,len(grid[0])):
            if(0<grid[line][column]<10):
                value = game_font.render(str(grid[line][column]),True,number_color)
                window.blit(value,((column+1)*50+15,(line+1)*50))
    pygame.display.update() # 122-127 - drawing all the numbers from the grid to the GUI

    pygame.draw.rect(window,button_color,(50,WIDTH+100,120,50))
    value = game_font.render("Check",True,(255,255,255))
    window.blit(value,(60,WIDTH+100))
    pygame.display.update()
    
    pygame.draw.rect(window, (255,255,255), (400, WIDTH+100, 120, 50))
    window.blit(timer_text,(415,WIDTH+100))
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == timer:
                if timer_sec > 0:
                    timer_sec -= 1
                    timer_text = game_font.render(time.strftime('%M:%S',time.gmtime(timer_sec)),True,(0,0,0))
                    pygame.draw.rect(window, (255,255,255), (400, WIDTH+100, 120, 50))
                    window.blit(timer_text,(415,WIDTH+100))
                    pygame.display.update()
                else:
                    pygame.draw.rect(window, (255,255,255), (300, WIDTH+100, 220, 50))
                    game_over_text = game_font.render("Game Over", True, wrong_color)
                    window.blit(game_over_text,(315,WIDTH+100))
                    pygame.display.update()
                    time.sleep(5)
                    exit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                print(pos)
                if timer_sec > 0:
                    timer_sec -= 1
                    timer_text = game_font.render(time.strftime('%M:%S',time.gmtime(timer_sec)),True,(0,0,0))
                    pygame.draw.rect(window, (255,255,255), (400, WIDTH+100, 120, 50))
                    window.blit(timer_text,(415,WIDTH+100))
                    pygame.display.update()
                else:
                    pygame.draw.rect(window, (255,255,255), (300, WIDTH+100, 220, 50))
                    game_over_text = game_font.render("Game Over", True, wrong_color)
                    window.blit(game_over_text,(315,WIDTH+100))
                    pygame.display.update()
                    time.sleep(5)
                    exit()
                if 49 < pos[0] < 170 and WIDTH+100 < pos[1] < WIDTH+150:
                    checkBoard(window,grid)
                elif 49<pos[0]<WIDTH and 49<pos[1]<WIDTH:
                    width_first_col = 4 if (pos[0]//50-1)%3 == 0 else 2
                    width_second_col = 4 if (pos[0]//50)%3 == 0 else 2
                    width_first_line = 4 if (pos[1]//50-1)%3 == 0 else 2
                    width_second_line = 4 if (pos[1]//50)%3 == 0 else 2
                    print(pos[0]//50)
                    print(pos[1]//50)
                    pygame.draw.line(window,(0, 255, 255),(pos[0]//50*50,pos[1]//50*50), (pos[0]//50*50 + 50,pos[1]//50*50),width_first_line)
                    pygame.draw.line(window,(0, 255, 255),(pos[0]//50*50,pos[1]//50*50), (pos[0]//50*50,pos[1]//50*50+50),width_first_col)
                    pygame.draw.line(window,(0, 255, 255),(pos[0]//50*50+50,pos[1]//50*50), (pos[0]//50*50 + 50,pos[1]//50*50+50),width_second_col)
                    pygame.draw.line(window,(0, 255, 255),(pos[0]//50*50,pos[1]//50*50+50), (pos[0]//50*50 + 50,pos[1]//50*50+50),width_second_line)
                    pygame.display.update()
                    drawNumber(window, (pos[0]//50,pos[1]//50), game_font,grid,original_grid)
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        