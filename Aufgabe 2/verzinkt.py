import pygame  # Importiert das Pygame-Modul, das für die Erstellung von Videospielen verwendet wird
import time  # Importiert das time-Modul, das für Zeitoperationen verwendet wird
from collections import deque  # Importiert das deque-Objekt aus dem collections-Modul. Deque steht für "double-ended queue" und ermöglicht das effiziente Hinzufügen und Entfernen von Elementen sowohl am Anfang als auch am Ende der Warteschlange.
import random  # Importiert das random-Modul, das für die Generierung von Zufallszahlen verwendet wird

pygame.init()  # Initialisiert alle importierten Pygame-Module

WIDTH, HEIGHT = 800, 600  # Legt die Breite und Höhe des Fensters fest
win = pygame.display.set_mode((WIDTH, HEIGHT))  # Erstellt ein Fenster oder einen Bildschirm mit der angegebenen Größe

class ExpandingSquare:  # Definiert eine Klasse namens ExpandingSquare
    def __init__(self, x, y, size, color):  # Definiert den Konstruktor der Klasse, der aufgerufen wird, wenn ein neues Objekt der Klasse erstellt wird
        self.x = x  # Setzt die x-Koordinate des Quadrats
        self.y = y  # Setzt die y-Koordinate des Quadrats
        self.size = size  # Setzt die Größe des Quadrats
        self.color = color  # Setzt die Farbe des Quadrats

    def draw(self):  # Definiert eine Methode namens draw, die das Quadrat zeichnet
        pygame.draw.rect(win, self.color, (self.x, self.y, self.size, self.size))  # Zeichnet ein Rechteck (in diesem Fall ein Quadrat) auf dem Bildschirm. Die Argumente sind das Fenster, in dem es gezeichnet wird, die Farbe, und ein Tuple, das die x- und y-Koordinaten sowie die Breite und Höhe (Größe) des Rechtecks angibt

colors = [(i, i, i) for i in range(20, 255, 12)]  # Erzeugt eine Liste von Grautönen

squares = deque([ExpandingSquare(random.randint(0, WIDTH), random.randint(0, HEIGHT), 1, random.choice(colors)) for _ in range(20)])  # Erstellt 20 zufällige expandierende Quadrate und fügt sie der Warteschlange hinzu
seen = set([(square.x, square.y) for square in squares])  # Erzeugt ein Set von Koordinaten, die bereits von Quadraten besetzt sind

run = True  # Setzt eine Kontrollvariable für die Hauptschleife
while run:  # Startet die Hauptschleife
    for event in pygame.event.get():  # Überprüft alle Ereignisse, die in der Warteschlange stehen
        if event.type == pygame.QUIT:  # Wenn das Ereignis der Typ QUIT ist (d. h. wenn der Benutzer das Fenster schließt)
            run = False  # Setzt run auf False, um die Hauptschleife zu beenden

    win.fill((0, 0, 0))  # Füllt das gesamte Fenster mit Schwarz

    for square in squares:  # Geht durch jedes Quadrat in der Warteschlange
        square.draw()  # Zeichnet das Quadrat

    new_squares = []  # Erzeugt eine leere Liste für neue Quadrate
    for square in squares:  # Geht durch jedes Quadrat in der Warteschlange
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # Geht durch jedes Element in der Liste von Richtungen (rechts, links, unten, oben)
            new_x, new_y = square.x + dx, square.y + dy  # Berechnet die Koordinaten des neuen Quadrats
            if (new_x, new_y) not in seen:  # Wenn das neue Quadrat noch nicht gesehen wurde
                seen.add((new_x, new_y))  # Fügt die Koordinaten des neuen Quadrats zum Set der gesehenen Quadrate hinzu
                new_squares.append(ExpandingSquare(new_x, new_y, 1, square.color))  # Erzeugt ein neues Quadrat und fügt es der Liste der neuen Quadrate hinzu
    squares.extend(new_squares)  # Fügt die Liste der neuen Quadrate zur Warteschlange der Quadrate hinzu

    pygame.display.update()  # Aktualisiert den gesamten Bildschirm

    time.sleep(0.1)  # Legt die Ausführung für 0,1 Sekunden schlafen

pygame.quit()  # Beendet alle Pygame-Module
