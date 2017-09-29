import pygame
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
green = (0,155,0)
red = (255,0,0)

display_width = 1000
display_height = 700
block_size = 20
FPS = 10
apple_size = 30
direction = "right"


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Slither")
pygame.display.update()

img = pygame.image.load('C:/Users/HP PC/Desktop/wally/snakehead.png')
appleimg = pygame.image.load('C:/Users/HP PC/Desktop/wally/apple.png')

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms",25)
medfont = pygame.font.SysFont("comicsansms",50)
largefont = pygame.font.SysFont("comicsansms",80)

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text,True,color,size)
    if size == "medium":
        textSurface = medfont.render(text,True,color,size)
    if size == "large":
        textSurface = largefont.render(text,True,color,size)
        
    return textSurface,textSurface.get_rect()

def message_on_screen(msg,color,y_displace = 0,size = "small"):
    textSurf,textRect = text_objects(msg,color,size)
    textRect.center = (display_width/2),(display_height/2)+y_displace
    gameDisplay.blit(textSurf,textRect)

def snake(block_size,snakeList):

    if direction == "right":
        head = pygame.transform.rotate(img,270)
    if direction == "left":
        head = pygame.transform.rotate(img,90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img,180)
        
    gameDisplay.fill(black)
    gameDisplay.blit(head,[snakeList[-1][0],snakeList[-1][1]])
    pygame.display.update
    
    for XnY in snakeList[:-1]:
        gameDisplay.fill(green, rect = [XnY[0],XnY[1],block_size,block_size])

def pause():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        #gameDisplay.fill(black)

        
        message_on_screen("Paused",white,-100,"large")
        message_on_screen("Press C to Continue or Q to Quit",white,50,"small")
        pygame.display.update()
        
                    

def score(score):
    text = smallfont.render("Score:"+str(score),True,white)
    gameDisplay.blit(text,[1,1])
    pygame.display.update()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    gameLoop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(black)
        message_on_screen("Welcome to SnakeXenzia",green,-100,"large")
        message_on_screen("The motive of this game is to eat all Apples",red,80,"small")
        message_on_screen("The more Apples snake will eat,the more speed and length it will gain",red,130,"small")
        message_on_screen("If snake will run into itself or out of the boundary.IT DIES",red,180,"small")
        message_on_screen("Press C to Play Game or Q to Quit or P to Pause",white,300,"small")
        pygame.display.update()
        clock.tick(15)


def gameLoop():

    global direction
    direction = "right"

    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    AppleX = round(random.randrange(0,display_width-apple_size)/10.0)*10.0
    AppleY = round(random.randrange(0,display_height-apple_size)/10.0)*10.0

    snakeList = []
    snakeLength = 1
    
    while not gameExit:
        while gameOver == True:
            #gameDisplay.fill(black)
            message_on_screen("GameOver",red,-100,"large")
            message_on_screen("Press C to PlayAgain or Q to Quit",white,100,"medium")
            score(snakeLength-1)
            pygame.display.update()
           

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                if event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                if event.key == pygame.K_UP:
                    direction = "up"
                    lead_x_change = 0
                    lead_y_change = -block_size
                if event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_x_change = 0
                    lead_y_change = block_size
                if event.key == pygame.K_p:
                    pause()                    
                    

        lead_x += lead_x_change
        lead_y += lead_y_change

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        if lead_x > AppleX and lead_x < AppleX+apple_size or lead_x+block_size > AppleX and lead_x+block_size < AppleX+apple_size:
            if lead_y > AppleY and lead_y < AppleY+apple_size or lead_y+block_size > AppleY and lead_y+block_size < AppleY+apple_size:
                AppleX = round(random.randrange(0,display_width-apple_size)/10.0)*10.0
                AppleY = round(random.randrange(0,display_height-apple_size)/10.0)*10.0
                snakeLength += 1

        gameDisplay.fill(black)        
                
        if len(snakeList) > snakeLength:
            del snakeList [0]

        for each_segment in snakeList[:-1]:
            if each_segment == snakeHead:
                gameOver = True
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        snake(block_size,snakeList)

        gameDisplay.blit(appleimg,(AppleX,AppleY))
        
        score(snakeLength-1)

        
        
        
        pygame.display.update()

        clock.tick(FPS+snakeLength)

        
        
        
    pygame.quit()

    quit()

game_intro()
gameLoop()
