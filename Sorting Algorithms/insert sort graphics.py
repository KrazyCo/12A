from math import trunc
import pygame, sys
from pygame.locals import *
import random

width = 1280
height = 720
numbers = 200
delay = 10

numList = range(1, numbers+1)
sortList = []
for number in numList:
    sortList.append(number)
random.shuffle(sortList)


pygame.init()
display=pygame.display.set_mode((width,height))

barWidth = max((width-40)/numbers-2,1)
heghtMultiplier = (height-40)/numbers

swapped = True
currentIndex = 0

while True:
    pygame.time.delay(delay)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    display.fill((255,255,255))
    for num, count in enumerate(sortList):
        if count == currentIndex or count == currentIndex+1:
            left = count*(barWidth+2)+10
            top = height-20-(trunc(max(num*heghtMultiplier,1)))
            barHeight = max(num*heghtMultiplier,1)
            pygame.draw.rect(display,(0,255,0),(left,top,barWidth,barHeight))
        else:
            left = count*(barWidth+2)+10
            top = height-20-(trunc(max(num*heghtMultiplier,1)))
            barHeight = max(num*heghtMultiplier,1)
            pygame.draw.rect(display,(0,0,255),(left,top,barWidth,barHeight))

    if (swapped and not currentIndex == numbers-1) or not currentIndex == numbers-1:
        swapped = False
        if sortList[currentIndex] > sortList[currentIndex+1]:
            temp = sortList[currentIndex]
            sortList[currentIndex] = sortList[currentIndex+1]
            sortList[currentIndex+1] = temp
            swapped = True
    currentIndex+=1
        # print(sortList)
    if currentIndex == number-1:
        currentIndex = 0


    pygame.display.flip()

