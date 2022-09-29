import pygame, sys
from pygame.locals import *
import random

width = 1280
height = 720
numbers = 50

numList = range(1, numbers+1)
sortList = []
for number in numList:
    sortList.append(number)
random.shuffle(sortList)

pygame.init()
display=pygame.display.set_mode((width,height))

barWidth = (width-40)/numbers-2
heghtMultiplier = (height-40)/50

while True:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    display.fill((255,255,255))
    for num, count in enumerate(sortList):
        pygame.draw.rect(display,(0,0,255),(count*barWidth+10,height-20-(num*heghtMultiplier),barWidth,num*heghtMultiplier))

    pygame.display.flip()

