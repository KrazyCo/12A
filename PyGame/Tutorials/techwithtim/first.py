# https://www.youtube.com/watch?v=i6xMBig-pP4&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5&ab_channel=TechWithTim

# ! yeah this isnt gonna work on replit 

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

class Player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.jumpVel = 0.5
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x,self.y))

def drawGameWindow():
    global walkCount
    # background
    win.blit(bg, (0,0))

    man.draw(win)
    pygame.display.update()

# main game loop
run = True
man = Player(300, 410, 64, 64)
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
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < screenWidth - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walkCount = 0

    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        # jumping
        if man.jumpCount >= -10:
            negative = 1
            if man.jumpCount < 0:
                negative = -1
            man.y -= (man.jumpCount ** 2) * man.jumpVel * negative
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    drawGameWindow()


pygame.quit()