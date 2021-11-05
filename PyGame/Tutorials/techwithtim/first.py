# https://www.youtube.com/watch?v=i6xMBig-pP4&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5&ab_channel=TechWithTim

import pygame
pygame.init()

# setting up window
screenWidth = 852
screenHeight = 480
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("TechWithTim Tutorial")

# importing images
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

# setup variables
x = 50
y = 200
width = 64
height = 64
vel = 4
jumpVel = 0.2
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def drawGameWindow():
    global walkCount
    # background
    win.blit(bg, (0,0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y))


    pygame.display.update()

# main game loop
run = True
while run:
    clock.tick(27)

    #checking for user events
    for event in pygame.event.get():
        # checking if user closed window
        if event.type == pygame.QUIT:
            run = False

    # getting current held keys
    keys = pygame.key.get_pressed()

    # character moving
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if not(isJump):
        if keys[pygame.K_UP]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        # jumping
        if jumpCount >= -10:
            negative = 1
            if jumpCount < 0:
                negative = -1
            y -= (jumpCount ** 2) * jumpVel * negative
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    drawGameWindow()


pygame.quit()