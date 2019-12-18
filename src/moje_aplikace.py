# chci delat grafiku v Pythonu
# real-time grafiku, to be precise

# 1) nainstaluju Pygame

# 2) vlozim Pygame do svoji aplikace
import pygame
# pridam taky knihovnu sys
import sys
# 3) zinicializuju Pygame
pygame.init()

# 4) napisu kostru graficke aplikace

# vytvorim okno (a ulozim si handle do promenne)
okno = pygame.display.set_mode((640, 480))
# zvolim barvu pozadi (napr. bilou)
okno.fill((255, 255, 255))

# napisu nekonecnou vykreslovaci smycku
while True:
    # umoznim zavreni okna krizkem
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            sys.exit()
    
    # refreshnu obsah okna
    pygame.display.update()
    
# kostra je hotova
