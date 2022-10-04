from math import trunc
import pygame, sys
from pygame.locals import *
import random

width = 1280
height = 720
numbers = 200
delay = 10
spacing = 1 # should be 2 for correct spacing, for larger lists make it smaller to fit onto screen

numList = range(1, numbers+1)
sortList = []
for number in numList:
    sortList.append(number)
random.shuffle(sortList)


pygame.init()
display=pygame.display.set_mode((width,height))

barWidth = max((width-40)/numbers-1,1)
heghtMultiplier = (height-40)/numbers

swapped = True
currentIndex = 0
finished = False
cycles = 0
finalPass = False

while True:
    # pygame.time.delay(delay)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    if not finished:
        display.fill((0,0,0))
        for count, num in enumerate(sortList):
            if count == currentIndex or count == currentIndex+1:
                left = count*(barWidth+spacing)+10
                top = height-20-(trunc(max(num*heghtMultiplier,1)))
                barHeight = max(num*heghtMultiplier,1)
                pygame.draw.rect(display,(255,0,0),(left,top,barWidth,barHeight))
            else:
                left = count*(barWidth+spacing)+10
                top = height-20-(trunc(max(num*heghtMultiplier,1)))
                barHeight = max(num*heghtMultiplier,1)
                pygame.draw.rect(display,(0,255,0),(left,top,barWidth,barHeight))

        if (swapped and not currentIndex == numbers-1) or not currentIndex == numbers-1:
            swapped = False
            if sortList[currentIndex] > sortList[currentIndex+1]:
                temp = sortList[currentIndex]
                sortList[currentIndex] = sortList[currentIndex+1]
                sortList[currentIndex+1] = temp
                swapped = True
                permSwapped = True
                # print(currentIndex)
                # print(sortList)
        currentIndex+=1
            # print(sortList)
        if currentIndex == number-1-cycles:
            currentIndex = 0
            cycles += 1
            if permSwapped == False:
                finished = True
            permSwapped = False

    if finished and finalPass == False:
        pygame.time.delay(delay)
        display.fill((0,0,0))
        for count, num in enumerate(sortList):
            if count == currentIndex or count == currentIndex+1:
                left = count*(barWidth+spacing)+10
                top = height-20-(trunc(max(num*heghtMultiplier,1)))
                barHeight = max(num*heghtMultiplier,1)
                pygame.draw.rect(display,(255,0,0),(left,top,barWidth,barHeight))
            else:
                left = count*(barWidth+spacing)+10
                top = height-20-(trunc(max(num*heghtMultiplier,1)))
                barHeight = max(num*heghtMultiplier,1)
                pygame.draw.rect(display,(0,255,0),(left,top,barWidth,barHeight))
        currentIndex+=1
        if currentIndex == number-1:
            finalPass = True

    pygame.display.flip()

