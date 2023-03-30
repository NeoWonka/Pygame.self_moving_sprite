import sys
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((0, 0, 0))
color = (250, 75, 250)

class Char(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))

    def Behavior

sprites_list = pygame.sprite.Group()

obj_1 = Char(50, 50)                                          
sprites_list.add(obj_1)



def RunPyGame():
    # Initialise PyGame.
    pygame.init()
    
    # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
    fps = 60.0
    fpsClock = pygame.time.Clock()
    dt = fpsClock.tick(fps)

    running = True
    while running:
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Opposite of pygame.init
                sys.exit()
                running = False
                
        sprites_list.update()
        sprites_list.draw(screen)
        pygame.display.flip()
        dt
        
        
        
RunPyGame()
