import pygame
import sys

pygame.init()

okno = pygame.display.set_mode((640, 480))

el_x = 400
el_y = 300

ob_y = 100
ob_v = 0.1
ob_blue = 0

w = 120

v = 0.05

# nekonecna smycka generujici framy obrazu
while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            sys.exit()
    
    # ziskam informace o stisknutych klavesach
    stisknuto = pygame.key.get_pressed()
    
    # vypnuti aplikace klavesou ESC
    if stisknuto[pygame.K_ESCAPE]:
        sys.exit()
    
    # pohnu obdelnikem pomoci sipek
    if stisknuto[pygame.K_UP]:
        ob_y = ob_y - ob_v
    if stisknuto[pygame.K_DOWN]:
        ob_y = ob_y + ob_v
    if stisknuto[pygame.K_b]:
        ob_blue += 0.1
    
    # aby mi obdelnik neutikal z okna
    if ob_y < 0:
        ob_y = 0
    if ob_y > 480 - 75:
        ob_y = 480 - 75
    
    # aby mi obdelnik prilis nezmodral
    if ob_blue > 255:
        ob_blue = 255
    
    # automaticky pohyb elipsy
    el_x = el_x + 0.01

    # aby mi elipsa neutikala doprava
    if el_x > 640 - w:
        el_x = 640 - w
    
    # premazani okna barvou pozadi
    okno.fill((255, 255, 255))
    # vykresleni obdelniku
    pygame.draw.rect(okno, (0, 0, ob_blue), (200, ob_y, 150, 75))
    # vykresleni elipsy
    pygame.draw.ellipse(okno, (0, 0, 255), (el_x, el_y, w, 80))
    
    pygame.display.update()
