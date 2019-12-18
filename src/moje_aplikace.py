import pygame
import sys

pygame.init()

okno = pygame.display.set_mode((640, 480))

okno.fill((255, 255, 255))

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            sys.exit()
    
    # vykresleni obdelniku
    pygame.draw.rect(okno, (0, 0, 0), (200, 100, 150, 75))
    # vykresleni elipsy
    pygame.draw.ellipse(okno, (0, 0, 255), (400, 300, 120, 80))
    
    pygame.display.update()
