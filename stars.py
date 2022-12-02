#!/usr/bin/env python
""" VIS 142 Section A01 & A02 - Week 6
    TA: Mingyong Cheng
    This example adapted from the beautiful starfield example shared in Pygame4000

    pg.examples.stars

    We are all in the gutter,
    but some of us are looking at the stars.
                                            -- Oscar Wilde

A simple starfield example. Note you can move the 'center' of
the starfield by leftclicking in the window. This example show
the basics of creating a window, simple pixel plotting, and input
event management.

"""
import random
import math
import pygame as pg

# constants
WINSIZE = [640, 480]
WINCENTER = [WINSIZE[0] / 2, WINSIZE[1] / 2]
NUMSTARS = 1000


def init_star():
    # creates new star values
    dir = random.randrange(100000)
    # random.random() returns a random float between 0-1
    velmult = random.random() * 0.6 + 0.4
    vel = [math.sin(dir) * velmult, math.cos(dir) * velmult]
    return vel, WINCENTER[:]


def initialize_stars():
    # creates a new starfield
    stars = []
    for x in range(NUMSTARS):
        star = init_star()
        # vel take the 1st value that stored in star
        # pos take the second value that stored in star
        vel, pos = star
        # print(vel, pos)
        # Give each star an initial random pos and vel
        steps = random.randint(0, WINCENTER[0])
        pos[0] = pos[0] + (vel[0] * steps)
        pos[1] = pos[1] + (vel[1] * steps)
        vel[0] = vel[0] * (steps * 0.09)
        vel[1] = vel[1] * (steps * 0.09)
        stars.append(star)
    move_stars(stars)
    return stars


def move_stars(stars):
    # animate the star values"
    for vel, pos in stars:
        # update pos each frame
        pos[0] = pos[0] + vel[0]
        pos[1] = pos[1] + vel[1]
        if not 0 <= pos[0] <= WINSIZE[0] or not 0 <= pos[1] <= WINSIZE[1]:
            # Limit the range of the stars' movement
            vel[:], pos[:] = init_star()
        else:
            # change the value multiply vel will change the speed of the stars
            vel[0] = vel[0] * 1.01
            vel[1] = vel[1] * 1.01

def draw_stars(surface, stars, color):
    # used to draw (and clear) the stars
    for vel, pos in stars:
        pos = (int(pos[0]), int(pos[1]))
        surface.set_at(pos, color)
        """ set_at((x, y), Color) -> None Set the RGBA or mapped integer color
            value for a single pixel. If the Surface does not have per pixel
            alphas, the alpha value is ignored. Setting pixels outside the
            Surface area or outside the Surface clipping will have no effect.
            Getting and setting pixels one at a time is generally too slow to
            be used in a game or realtime situation.
        """


def main():
    # This is the starfield code"
    # create our starfield
    random.seed()
    # The seed() method is used to initialize the random number generator
    stars = initialize_stars()
    clock = pg.time.Clock()
    """Creates a new Clock object that can be used to track an amount of
    time. The clock also provides several functions to help control a game's
    framerate """
    # initialize and prepare screen
    pg.init()
    screen = pg.display.set_mode(WINSIZE)
    pg.display.set_caption("My Starfield")
    white = 255, 240, 200
    black = 20, 20, 40
    screen.fill(black)

    # main game loop
    done = 0
    while not done:
        # infinite animated stars
        draw_stars(screen, stars, black)
        move_stars(stars)
        draw_stars(screen, stars, white)
        pg.display.update()
        for e in pg.event.get():
            """ All pygame.event.Eventpygame object for representing events
            instances contain an event type identifier and attributes
            specific to that event type. check this page for more about
            event: https://www.pygame.org/docs/ref/event.html """
            if e.type == pg.QUIT or (
                e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
                """The pygame.eventpygame module for interacting with events
                and queues queue gets pygame.KEYDOWN and pygame.KEYUP events
                when the keyboard buttons are pressed and released. Both
                events have key and mod attributes. """
                done = 1
                break
            elif e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
                # button: 1 refers to the left click
                # button: 3 refers to the right click
                # print(e.pos)
                # update the position of the starfield
                WINCENTER[:] = list(e.pos)
        clock.tick(50)
        """update the clock tick(framerate=0) -> milliseconds This method
        should be called once per frame. It will compute how many
        milliseconds have passed since the previous call. If you pass the
        optional framerate argument the function will delay to keep the game
        running slower than the given ticks per second. This can be used to
        help limit the runtime speed of a game. By calling Clock.tick(40)
        once per frame, the program will never run at more than 40 frames
        per second. """


# if python says run, then we should run
if __name__ == "__main__":
    main()

    # I prefer the time of insects to the time of stars.
    #
    #                              -- Wisława Szymborska
