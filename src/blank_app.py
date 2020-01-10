# NUTNO MIT NAINSTALOVANY BALICEK PYGAME
import pygame
import sys

# inicializace knihovny
pygame.init()
# inicializace okna
okno = pygame.display.set_mode((800, 600))

# nekonecna smycka generujici framy obrazu
while True:
    # sejmuti stavu vsech klaves
    stisknuto = pygame.key.get_pressed()
    # sejmuti stavu vsech modifikacnich klaves
    alty_apod = pygame.key.get_mods()
    
    # vypnuti aplikace krizkem
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            sys.exit()
    # vypnuti aplikace klavesou ESC
    if stisknuto[pygame.K_ESCAPE]:
        sys.exit()
    # vypnuti aplikace zkratkou ALT + F4
    if stisknuto[pygame.K_F4] and (alty_apod & pygame.KMOD_LALT):
        sys.exit()

    # premazani okna barvou
    okno.fill((255, 255, 255))
    
    # TENTO RADEK MUSI BYT POSLEDNI
    pygame.display.update()
