import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
green = (0,155,0)
red = (255,0,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Slither")
pygame.display.update()

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(white)
    


pygame.quit()

quit()
