import sys
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((0, 0, 0))
color = (250, 250, 250)

class Char(pygame.sprite.Sprite):
    def __init__(self, left, top, width, height):
        super().__init__()
        pygame.draw.rect(screen, color, pygame.Rect(left, top, width, height))


obj_1 = Char(0, 0, 50, 50)                                          

def drawPlayer():
    screen.blit(obj_1)
    pygame.display.update(obj_1)

def runPyGame():
    # Initialise PyGame.
    pygame.init()

    # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
    fps = 60.0
    fpsClock = pygame.time.Clock()
    dt = fpsClock.tick(fps)
    # Set up the window.
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))

    # screen is the surface representing the window.
    # PyGame surfaces can be thought of as screen sections that you can draw onto.
    # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.

    # Main game loop.
    # dt is the time since last frame.
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Opposite of pygame.init
                sys.exit()  # Not including this line crashes the script on Windows. Possibly
            # on other operating systems too, but I don't know for sure.    update(dt)  # You can update/draw here, I've just moved the code for neatness.
        drawPlayer()
        pygame.display.flip(dt)
        
runPyGame()
