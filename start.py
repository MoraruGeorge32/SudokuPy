import pygame

def start(window):
    button_color = (0,0,0)
    pygame.display.set_caption("Start")
    title_font = pygame.font.SysFont('arialms',70)
    start_font = pygame.font.SysFont('arialms',35)
    title = title_font.render("Sudoku",True,(0,0,0))
    window.blit(title, (160,30))
    pygame.draw.rect(window,button_color,(180,200,200,50))
    start_text = start_font.render("Start",True,(255,255,255))
    window.blit(start_text, (240,200))
    pygame.draw.rect(window,button_color,((180,400,200,50)))
    exit_text = start_font.render("Exit",True,(255,255,255))
    window.blit(exit_text,(245,400))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                print(pos)
                if 180<pos[0]<380 and 200<pos[1]<250:
                    return True
                if 180<pos[0]<380 and 400<pos[1]<450:
                    pygame.quit()
                    return False
