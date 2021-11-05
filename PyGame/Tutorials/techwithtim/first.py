# https://www.youtube.com/watch?v=i6xMBig-pP4&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5&ab_channel=TechWithTim

import pygame
pygame.init()

# setting up window
screenWidth = 500
screenHeight = 500
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("TechWithTim Tutorial")

# rectangle setup variables
x = 50
y = 50
width = 40
height = 60
vel = 2

isJump = False
jumpCount = 40

# main game loop
run = True
while run:
    pygame.time.delay(10)

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
    if keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < screenHeight - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        # jumping
        if jumpCount >= -40:
            negative = 1
            if jumpCount < 0:
                negative = -1
            y -= (jumpCount ** 2) * 0.005 * negative
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 40

    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) #drawing rectangle
    pygame.display.update()

pygame.quit()