# vis 142 fall 2022 project 2
# This can take 20 minutes to hours to run.

# imports, don't change these but you can add imports you need
import pygame
from pygame.locals import *
from sys import exit
import random
import time
# record the start time
start_time = time.time()

#####################################################################
# We will be producing 4K video from an image sequence
# Important: you might want to work at lower resolution that fits, 
# your screens! Such as 1920 x 1080.
# And then change these back to 4096 × 2160 for production.
# On the other hand, you will have to deal with scaling issues if you do.
#####################################################################
width = 500
height = 500

#width = 4096 
#height = 2160 

#####################################################################
# Name and title, update to your name and title
#####################################################################
name = "Meihui Liu"
title = "SSSSnakes" 

#####################################################################
# IMPORTANT - you will get your start sequence number from your TA
# If you use the default number 1000000 below, your work will not 
# be part of the class reel, as in every student must have different
# start sequence numbers.
#####################################################################
start_sequence_num = 2042000 # CHANGE HERE

# Do not change these variables
# normal pygame stuff
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('generate 4K animation pngs')
frame_num = start_sequence_num
titles_font = pygame.font.SysFont(None, int(width/12)) # if name or title run off screen, try setting the literal to 16 instead of 12
name_f = titles_font.render(name, True, (255,255,255))
title_f = titles_font.render(title, True, (255,255,255))

# print resolution warning
if (width != 4096 and height != 2160):
    print("Warning: dimensions not 4K, be sure width and height are set to 4096 and 2160.")

# this function makes one second of black frames
def make_black():
    global frame_num
    screen.fill((0,0,0))
    pygame.display.update()
    for i in range(0, 60):
       # pygame.image.save(screen, "./frames/" + str(frame_num) + ".png")
       frame_num = frame_num + 1
       clock.tick(60)
        
#############################################################
# Object Sanke
# Defines all the proporties of a snake object and makes it movable.
class Snake:
    color = (15,15,15)
    prev_heading = 0
    heading = 0
    startPosX = 0
    startPosY = 0
    endPosX = 0
    endPosY = 0
    turningPosX = 0
    turningPosY = 0
    turning = 0
    length = 50
    size = 1

    def __init__(self):
        self.color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        self.length = random.randint(2, width - int(width/4))
        self.size = random.randint(2, 7)
        self.startPosX = random.randint(100, width-100) 
        self.startPosY = random.randint(100, height-100)
        self.heading = random.randint(0, 3)
        self.prev_heading = self.heading
        if (self.heading == 0): # heading right
            self.endPosX = self.startPosX - self.length
            self.endPosY = self.startPosY
        if (self.heading == 1): # heading left
            self.endPosX = self.startPosX + self.length
            self.endPosY = self.startPosY
        if (self.heading == 2): # heading up
            self.endPosX = self.startPosX
            self.endPosY = self.startPosY + self.length
        if (self.heading == 3): # heading down
            self.endPosX = self.startPosX
            self.endPosY = self.startPosY - self.length
    
    def choose_turn_heading(self):
        self.prev_heading = self.heading
        up_down = [2, 3]
        left_right = [1, 0]
        if(self.prev_heading == 0 or self.prev_heading == 1):
            self.heading = random.choice(up_down)
        else:
            self.heading = random.choice(left_right)
    
    def set_turning_point(self):
        self.turningPosX = self.startPosX
        self.turningPosY = self.startPosY

    def turn(self):
        # Before the turning point, only end positions are changing
        if (self.prev_heading == 0): # heading right
            self.endPosX += 1
        if (self.prev_heading == 1): # heading left
            self.endPosX -= 1
        if (self.prev_heading == 2): # heading up
            self.endPosY -= 1
        if (self.prev_heading == 3): # heading down
            self.endPosY += 1
        #After the turning point, only start positions are changing
        if (self.heading == 0): # heading right
            self.startPosX += 1
        if (self.heading == 1): # heading left
            self.startPosX -= 1
        if (self.heading == 2): # heading up
            self.startPosY -= 1
        if (self.heading == 3): # heading down
            self.startPosY += 1
        #checking if we are done turning
        # print("endPosX " + str(self.endPosX) + " endPosY " + str(self.endPosY))
        # print("turningPosX " + str(self.turningPosX) + " turningPosY " + str(self.turningPosY))
        # print("startPosX " + str(self.startPosX) + " startPosY " + str(self.startPosY))
        if(self.prev_heading == 0 or self.prev_heading == 1):
            self.turning = int(self.endPosX != self.turningPosX)
        else:
            self.turning = int(self.endPosY != self.turningPosY)
        
    def move(self):
        if(not self.turning):
            p_turn = random.randint(0, 100)
            if(p_turn > 98):
                self.turning = 1
                self.choose_turn_heading()
                self.set_turning_point()
                # print("CURRENT " + str(self.heading))
                # print("PREV " + str(self.prev_heading))
        if(self.turning):
            self.turn()
            pygame.draw.line(screen, self.color, (self.startPosX, self.startPosY), (self.turningPosX, self.turningPosY), self.size)
            pygame.draw.line(screen, self.color, (self.turningPosX, self.turningPosY), (self.endPosX, self.endPosY), self.size)
        else:
            if (self.heading == 0): # heading right
                # print("right")
                self.startPosX += 1
                self.endPosX += 1
            if (self.heading == 1): # heading left
                # print("left")
                self.startPosX -= 1
                self.endPosX -= 1
            if (self.heading == 2): # heading up
                # print("up")
                self.startPosY -= 1
                self.endPosY -= 1
            if (self.heading == 3): # heading down
                # print("down")
                self.startPosY += 1
                self.endPosY += 1    
            pygame.draw.line(screen, self.color, (self.startPosX, self.startPosY), (self.endPosX, self.endPosY), self.size)
################################ end object

# this is the credits loop, which puts the title of your work
# and your name on the screen
make_black() # one second black
# produce title sequence
screen.fill((0,0,0))
screen.blit(name_f, (int(width/8), int(width/8)))
screen.blit(title_f, (int(width/8), int(width/4))) 
for i in range(0, 3*60):
    pygame.display.update()
    # pygame.image.save(screen, "./frames/" + str(frame_num) + ".png")
    frame_num = frame_num + 1
    clock.tick(60)
make_black() # one second black

# make a list of snakes (20 snakes)
snakes = [Snake()]
for i in range (0, 20):
    snakes.append(Snake())

# here is the main animation loop
for i in range(0, 20*60): # 20*60 frames is 20 seconds
    #########################################################
    # in the skeleton, your animation goes from here ########
    #########################################################
    screen.fill((0,0,0))
    for thing in snakes:
        thing.move()
    #########################################################
    # to here ###############################################
    #########################################################

    # The next line can be commented out to speed up testing frame rate
    # by not writing the file. But for output to final frames,
    # you will need to ucomment it.
    #pygame.image.save(screen, "./frames/" + str(frame_num) + ".png")
    frame_num = frame_num + 1
    pygame.display.update()
    clock.tick(60)

# print out stats
print("seconds:", int(time.time() - start_time))
print("~minutes: ", int((time.time() - start_time)/60))
# we just quit here
pygame.display.quit()
pygame.quit()
exit()

# you can make your files into a movie with ffmpeg:
# ffmpeg -r 60 -start_number 1000000 -s 4096x2160 -i %d.png -vcodec libx264 -crf 5 -pix_fmt yuv420p final.mp4
# with a few changes such as to start number, but this is just extra info here
