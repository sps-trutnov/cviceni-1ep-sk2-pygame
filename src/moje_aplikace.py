import pygame
import sys

pygame.init()

okno = pygame.display.set_mode((640, 480))

x = 400
y = 100
w = 120

v = 0.05

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            sys.exit()
    
    x = x + 0.01
    y = y - v
    
    # aby mi obdelnik neutikal nahoru
    if y < 0:
        y = 0
        v = v * -1
    # aby mi obdelnik neutikal vubec
    if y > 480 - 75:
        y = 480 - 75
        v = v * -1
    
    # aby mi elipsa neutikala doprava
    if x > 640 - w:
        x = 640 - w
    
    # premazani okna barvou pozadi
    okno.fill((255, 255, 255))
    # vykresleni obdelniku
    pygame.draw.rect(okno, (0, 0, 0), (200, y, 150, 75))
    # vykresleni elipsy
    pygame.draw.ellipse(okno, (0, 0, 255), (x, 300, w, 80))
    
    pygame.display.update()
