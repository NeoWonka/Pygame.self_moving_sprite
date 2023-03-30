import sys
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500,500))

class Player(pygame.sprite.Sprite):
    def __init__(self, surf, rect):
        self.surf = pygame.Surface((50, 50))
        color = self.surf.fill((250, 250, 250))
        self.rect = pygame.surf.get_rect(surf, center=(250, 250))
        pygame.draw.rect(surf, color, rect)
        
player = Player()

def drawPlayer(sprite):
    screen.blit(sprite)
    pygame.display.update()

def drawScreen(window):
    pygame.display.flip(window)

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
        draw(screen)
        drawPlayer(player)

        
runPyGame()
