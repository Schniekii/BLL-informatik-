import pygame
from collections import deque
import random

pygame.init()

Breite, Höhe = 1000, 1000
Bildschirm = pygame.display.set_mode((Breite, Höhe))

class Wachsender_Kristall:
    def __init__(self, x, y, size, color):  #
        self.x = x
        self.y = y
        self.größe = size
        self.farbe = color

    def zeichnen(self):
        pygame.draw.rect(Bildschirm, self.farbe, (self.x, self.y, self.größe, self.größe))
grautöne = [(grauton, grauton, grauton) for grauton in range(20, 255, 12)]  # Erzeugt eine Liste von Grautönen

zink_kristall = deque([Wachsender_Kristall(random.randint(0, Breite), random.randint(0, Höhe), 1, random.choice(grautöne)) for anzahl in range(int(input("Menge an kristall keimen:")))])
vorhanden = set([(kristall.x, kristall.y) for kristall in zink_kristall])

aktiv = True
while aktiv:  # Startet die Hauptschleife
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            aktiv = False

    Bildschirm.fill((0, 0, 0))

    for kristall in zink_kristall:
        kristall.zeichnen()

    neue_kristalle = []
    for kristall in zink_kristall:
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neue_x_koordinate, neue_y_koordinate = kristall.x + dx, kristall.y + dy
            if (neue_x_koordinate, neue_y_koordinate) not in vorhanden:
                vorhanden.add((neue_x_koordinate, neue_y_koordinate))
                neue_kristalle.append(Wachsender_Kristall(neue_x_koordinate, neue_y_koordinate, 1, kristall.farbe))
    zink_kristall.extend(neue_kristalle)

    pygame.display.update()

pygame.quit()