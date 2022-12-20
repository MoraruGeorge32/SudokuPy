import pygame

def select_difficulty(window):
    difficulties=['Easy','Medium','Hard']
    pygame.display.set_caption("Choose the difficulty:")
    button_color = (0,0,0)
    title_font = pygame.font.SysFont('arialms',40)
    start_font = pygame.font.SysFont('arialms',35)
    title = title_font.render("Choose your difficulty:",True,(0,0,0))
    window.blit(title, (90,80))
    y_start_button=200
    for buttonIndex in range(0,3):
        pygame.draw.rect(window,button_color,(180,y_start_button+100*buttonIndex,200,50))
        difficulty_text = start_font.render(difficulties[buttonIndex],True,(255,255,255))
        window.blit(difficulty_text, (280 - 10*len(difficulties[buttonIndex]),200+buttonIndex*100))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                print(pos)
                if 180<pos[0]<380 and 200<pos[1]<250:
                    return 'Easy'
                elif 180<pos[0]<380 and 300<pos[1]<350:
                    return 'Medium'
                elif 180<pos[0]<380 and 400<pos[1]<450:
                    return 'Hard'