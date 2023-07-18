import pygame
breite = 10
# je nach der breite des kristalls muss der abstand teilbar sein ohne nach komma stellen bei 1 min 1 bei 10 min 10 ......
print("Es gibt bis zu drei mögliche verschiedene Kristallen die man mithilfe von x und y koordinaten eingeben kann")
koordinaten1 = []
koordinaten2 = []
koordinaten3 = []
schnelligkeit = 10
def alle_koordinaten(lst):
    lst =  []
    koordinaten = input("Koordinaten:")
    koordinaten_tuple = tuple(int(koor) for koor in koordinaten.split())
    lst.append(koordinaten_tuple)
    return lst
Entwicklung = int(input("Entwicklungen:"))
# gibt alle richtungen aus für die Koordinate
def allerichtungen(xposition,yposition,schnelligkeit):
    oben = xposition, yposition+ schnelligkeit
    unten = xposition, yposition-schnelligkeit
    rechts = xposition  +schnelligkeit , yposition
    links = xposition -schnelligkeit ,  yposition
    return tuple(oben) , tuple(unten),tuple(rechts),tuple(links)
koordinaten1 = alle_koordinaten(koordinaten1)
koordinaten2 = alle_koordinaten(koordinaten2)
koordinaten3 = alle_koordinaten(koordinaten3)
#erstellt für die Koordinate die ausgabe Liste
def checker(lists,schnelligkeit):
    Entwicklungen = 0
    for x,y in lists:
        Entwicklungen = Entwicklungen + 1
        o,u,r,l = allerichtungen(x,y,schnelligkeit)
        if o not in lists:
           lists.append(o)
        if u  not in lists:
            lists.append(u)
        if r  not in lists:
            lists.append(r)
        if l  not in lists:
              lists.append(l)
        if Entwicklungen >= Entwicklung:
           break
    return lists
checker(koordinaten1,schnelligkeit)
checker(koordinaten2,schnelligkeit)
checker(koordinaten3,schnelligkeit)
#überprüft alle Listen und ihre überschneidungen
def keine_überschneidungen(lst1,lst2,lst3):
    lst = []
    for i in lst1:
        if i not in lst2:
            if i not in lst3:
                 lst.append(i)
        if i not in lst3:
            if i not in lst2:
                lst.append(i)
    return lst
def überschneidungen(lst1,lst2,lst3):
    lst = []
    for i in lst1:
        if i in lst2  and lst1.index(i) < lst2.index(i):
            if i in lst3 and lst1.index(i) < lst3.index(i):
                lst.append(i)
            if i not in lst3 and lst1.index(i) < lst2.index(i):
                lst.append(i)
        if i in lst3  and lst1.index(i) < lst3.index(i):
            if i in lst2 and lst1.index(i) < lst2.index(i):
                lst.append(i)
            if i not in lst2 and lst1.index(i) < lst3.index(i):
                lst.append(i)
    return lst
testkü1 = keine_überschneidungen(koordinaten1,koordinaten2,koordinaten3)
testkü2 = keine_überschneidungen(koordinaten2,koordinaten3,koordinaten1)
testkü3 = keine_überschneidungen(koordinaten3,koordinaten1,koordinaten2)
testü1 = überschneidungen(koordinaten1,koordinaten2,koordinaten3)
testü2 = überschneidungen(koordinaten2,koordinaten3,koordinaten1)
testü3 = überschneidungen(koordinaten3,koordinaten1,koordinaten2)
def kristall_zeichnen(liste,zahl,schnelligkeit):
    Farbe = [10+zahl,10+zahl,10+zahl]
    for x,y in liste:
        pygame.draw.rect(screen, Farbe, [x, y, schnelligkeit, schnelligkeit], filled)
#größe der Bildschirm ausgabe
screen=pygame.display.set_mode([1000,1000])
surface = pygame.Surface((100,100))
screen.fill([255, 255, 255])
red=255
blue=0
green=0
left=251
top=316
width=10
height=10
filled=0
lst = []
counter = -1
pygame.display.flip()
running=True
#gibt das Fertige Bild aus
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        kristall_zeichnen(testü1,12,schnelligkeit)
        kristall_zeichnen(testü2,20,schnelligkeit)
        kristall_zeichnen(testü3,40,schnelligkeit)
        kristall_zeichnen(testkü1,12,schnelligkeit)
        kristall_zeichnen(testkü2,20,schnelligkeit)
        kristall_zeichnen(testkü3,40,schnelligkeit)
        pygame.display.flip()
        running = "Truet"
