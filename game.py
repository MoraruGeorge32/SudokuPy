import pygame
WIDTH = 550
background_color = (251,247,245)
number_color = (86,3,252)
pygame.init()
myfont = pygame.font.SysFont('arialms',35)
grid = [[2,0,0,0,0,0,0,0,0],[1,0,0,2,0,6,7,0,0],[0,0,0,3,0,8,0,0,4],[0,0,2,4,0,5,8,0,7],[0,5,0,7,0,9,0,1,3],[0,0,0,1,0,0,0,5,6],[0,2,1,6,0,4,9,0,0],[0,0,0,5,9,0,3,0,1],[0,0,0,8,1,0,5,4,0]]
def addNumber(window,pos):
    column, line = pos[0], pos[1]
    while True:
        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if grid[line-1][column-1] != 0:
                    return
                if event.key == 48:
                    grid[line-1][column-1] = event.key - 48
                    pygame.draw.rect(window, background_color, (pos[0]*50+5, pos[1]*50 + 5, 50-5, 50-5))
                    pygame.display.update()
                    return
                if(0<event.key-48<10):
                    pygame.draw.rect(window,background_color,(pos[0]*50+5,pos[1]*50+5,50-5,50-5))
                    value = myfont.render(str(event.key-48),True,(0,0,0))
                    window.blit(value,(pos[0]*50+15,pos[1]*50))
                    grid[line][column] = event.key - 48
                    pygame.display.update()
                    return
                return


def main():
    window = pygame.display.set_mode((WIDTH,WIDTH))
    pygame.display.set_caption("Sudoku")
    window.fill(background_color)
    for gridLines in range(0,10):
        width = 4 if not gridLines%3 else 2
        pygame.draw.line(window,(0,0,0),(50+50*gridLines,50),(50 + 50*gridLines,500), width)
        pygame.draw.line(window,(0,0,0),(50,50+50*gridLines),(500 ,50+50*gridLines), width)
    pygame.display.update()

    for line in range(0,len(grid[0])):
        for column in range(0,len(grid[0])):
            if(0<grid[line][column]<10):
                value = myfont.render(str(grid[line][column]),True,number_color)
                window.blit(value,((column+1)*50+15,(line+1)*50))
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                addNumber(window, (pos[0]//50,pos[1]//50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()