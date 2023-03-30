import sys
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((0, 0, 0))
color = (250, 75, 250)

class Char(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface([width, height])
        self.rect = pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        screen.blit(self.image, (x, y))

    def Movement(self):
        self.move_x = 0
        self.move_y = 0

        for num in range(0,3):
            num = random.randint(0,3)
            if num == 0:
                self.move_x += 5
                if num == 1:
                    self.move_x -= 5
                    if num == 2:
                        self.move_y += 5
                else:
                    self.move_y -= 5
                    
        self.get_rect.x += self.move_x
        self.get_rect.y += self.move_y
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.update()
                        
        
sprites_list = pygame.sprite.Group()

obj_1 = Char(50, 60, 50, 50)                                          
sprites_list.add(obj_1) 



def RunPyGame():
    # Initialise PyGame.
    pygame.init()
    pygame.display.flip()
    # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
    fps = 60.0
    fpsClock = pygame.time.Clock()
    dt = fpsClock.tick(fps)

    running = True
    while running:
    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Opposite of pygame.init
                sys.exit()
                running = False

        
        sprites_list.update()
        sprites_list.draw(screen)
        dt
        
        
        
RunPyGame()
