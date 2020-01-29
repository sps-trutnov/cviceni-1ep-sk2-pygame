# pouzite knihovny
import pygame
import sys
import math
import random

# nastaveni aplikace
rozmer_okna_x = 800
rozmer_okna_y = 600

cernobily_rezim = False
min_velikost_micku = 5
max_velikost_micku = 50
max_rychlost_micku = 0.1

rychlost_hrace = 0.2
pocet_micku = 100

# pomocne podprogramy
def vypnout_aplikaci():
    for udalost in pygame.event.get():
        if udalost.type == pygame.KEYDOWN and udalost.key == pygame.K_ESCAPE:
            sys.exit()
        if udalost.type == pygame.QUIT:
            sys.exit()

def vytvorit_hrace():
    hrac = dict()

    hrac["w"] = hrac["h"] = max_velikost_micku

    hrac["x"] = (rozmer_okna_x - hrac["w"]) / 2
    hrac["y"] = (rozmer_okna_y - hrac["h"]) / 2

    hrac["v"] = rychlost_hrace
    hrac["rgb"] = (0, 0, 0)
    
    return hrac

def vytvorit_micky():
    micky = []
    
    for i in range(pocet_micku):
        micek = dict()

        micek["w"] = micek["h"] = random.randint(min_velikost_micku, max_velikost_micku)

        micek["x"] = random.randint(0, rozmer_okna_x - micek["w"])
        micek["y"] = random.randint(0, rozmer_okna_y - micek["h"])

        micek["dx"] = random.random() * random.choice([-1, 1])
        micek["dy"] = random.random() * random.choice([-1, 1])

        korekce = math.sqrt(micek["dx"] ** 2 + micek["dy"] ** 2)
        
        if korekce > 0:
            micek["dx"] /= korekce
            micek["dy"] /= korekce
        
        micek["dx"] *= max_rychlost_micku
        micek["dy"] *= max_rychlost_micku

        micek["sezrany"] = False

        if cernobily_rezim:
            odstin = random.randint(5, 250)
            micek["rgb"] = (odstin, odstin, odstin)
        else:
            micek["rgb"] = (random.randint(5, 250), random.randint(5, 250), random.randint(5, 250))
        
        micky.append(micek)
    else:
        return micky

def udrzet_v_okne(obrazec):
    if obrazec["y"] < 0:
        obrazec["y"] = 0
    if obrazec["y"] > rozmer_okna_y - obrazec["h"]:
        obrazec["y"] = rozmer_okna_y - obrazec["h"]
    if obrazec["x"] < 0:
        obrazec["x"] = 0
    if obrazec["x"] > rozmer_okna_x - obrazec["w"]:
        obrazec["x"] = rozmer_okna_x - obrazec["w"]

def odrazit_od_kraje(obrazec):
    if obrazec["y"] < 0:
        obrazec["dy"] *= -1
    if obrazec["y"] > rozmer_okna_y - obrazec["h"]:
        obrazec["dy"] *= -1
    if obrazec["x"] < 0:
        obrazec["dx"] *= -1
    if obrazec["x"] > rozmer_okna_x - obrazec["w"]:
        obrazec["dx"] *= -1    

def pohnout_s_mickem(micek):
    micek["x"] = micek["x"] + micek["dx"]
    micek["y"] = micek["y"] + micek["dy"]

def ovladat_hrace(hrac):
    stisknuto = pygame.key.get_pressed()
    
    vektor_hrace = {"x": 0, "y": 0}
    
    if stisknuto[pygame.K_RIGHT]:
        vektor_hrace["x"] += 1
    if stisknuto[pygame.K_LEFT]:
        vektor_hrace["x"] -= 1
    if stisknuto[pygame.K_DOWN]:
        vektor_hrace["y"] += 1
    if stisknuto[pygame.K_UP]:
        vektor_hrace["y"] -= 1
    
    korekce = math.sqrt(vektor_hrace["x"] ** 2 + vektor_hrace["y"] ** 2)
    
    if korekce > 0:
        vektor_hrace["x"] /= korekce
        vektor_hrace["y"] /= korekce
    
    hrac["x"] += vektor_hrace["x"] * hrac["v"]
    hrac["y"] += vektor_hrace["y"] * hrac["v"]

def zrat_okolni_micky(hrac, micky):
    for micek in micky:
        if micek["sezrany"]:
            continue
        
        soucet_polomeru = (hrac["w"] + micek["w"]) / 2
        
        x1 = hrac["x"] + hrac["w"] / 2
        x2 = micek["x"] + micek["w"] / 2
        y1 = hrac["y"] + hrac["h"] / 2
        y2 = micek["y"] + micek["h"] / 2
        
        vzdalenost_stredu = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        
        if vzdalenost_stredu < soucet_polomeru:
            rozdil = min(soucet_polomeru - vzdalenost_stredu, micek["w"])
            
            zvetsit_hrace(hrac, rozdil)
            zmensit_micek(micek, rozdil)

def obnovit_po_sezrani(hrac, micky):
    for micek in micky:
        if not micek["sezrany"]:
            return
    
    hrac["w"] = hrac["h"] = max_velikost_micku
    
    hrac["x"] = (rozmer_okna_x - hrac["w"]) / 2
    hrac["y"] = (rozmer_okna_y - hrac["h"]) / 2
    
    for micek in micky:
        micek["w"] = micek["h"] = random.randint(min_velikost_micku, max_velikost_micku)
        micek["sezrany"] = False

def zvetsit_hrace(hrac, jak_moc):
    jak_moc = jak_moc / 6
    
    hrac["w"] += jak_moc
    hrac["h"] += jak_moc
    
    hrac["x"] -= jak_moc / 2
    hrac["y"] -= jak_moc / 2
    
def zmensit_micek(micek, jak_moc):
    micek["w"] -= jak_moc
    micek["h"] -= jak_moc
    
    micek["x"] += jak_moc / 2
    micek["y"] += jak_moc / 2
    
    if micek["w"] < min_velikost_micku:
        micek["sezrany"] = True

# logika aplikace
pygame.init()

okno = pygame.display.set_mode((rozmer_okna_x, rozmer_okna_y))
pygame.display.set_caption("Míčkyyy!")

vsechny_micky = vytvorit_micky()
hrac = vytvorit_hrace()

while True:
    vypnout_aplikaci()        
    
    for micek in vsechny_micky:
        pohnout_s_mickem(micek)
        odrazit_od_kraje(micek)
        udrzet_v_okne(micek)
        
    ovladat_hrace(hrac)
    udrzet_v_okne(hrac)
    
    zrat_okolni_micky(hrac, vsechny_micky)
    obnovit_po_sezrani(hrac, vsechny_micky)
    
    okno.fill((255, 255, 255))
    
    for micek in vsechny_micky:
        if not micek["sezrany"]:
            pygame.draw.ellipse(okno, micek["rgb"], (micek["x"], micek["y"], micek["w"], micek["h"]))
    else:
        pygame.draw.ellipse(okno, hrac["rgb"], (hrac["x"], hrac["y"], hrac["w"], hrac["h"]))
    
    pygame.display.update()
