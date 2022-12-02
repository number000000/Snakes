import pygame
import random
from math import pi

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
screen.fill((0,0,0))

startPosX = random.randint(0, 1000) 
startPosY = random.randint(0, 1000)
heading = random.randint(0, 3)
if (heading == 0): # heading right
        endPosX = startPosX + 100
        endPosY = startPosY
if (heading == 1): # heading left
        endPosX = startPosX - 100
        endPosY = startPosY
if (heading == 2): # heading up
        endPosX = startPosX
        endPosY = startPosY - 100
if (heading == 3): # heading down
        endPosX = startPosX
        endPosY = startPosY + 100

pygame.draw.line(screen, (100, 100, 100), (startPosX, startPosY), (endPosX, endPosY), 4)
pygame.image.save(screen, "test.png")

pygame.display.quit()
pygame.quit()