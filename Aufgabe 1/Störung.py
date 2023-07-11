import string
satzzeichen_liste = ["«", "»"]
buch = []
#wertet die Datei aus und entfernt Satzzeichen
def dateiauswertung(dateiname):
    with open(dateiname, encoding='utf-8') as d:
        text = d.read()
        words = text.split()
        words = [''.join(letter for letter in word if letter not in string.punctuation and letter not in satzzeichen_liste) for word in words if word]
        return words
#dateiname für die Dateiauswertung
zitat = dateiauswertung("stoerung5.txt")
buch = [words.lower()  for words  in dateiauswertung("Alice_im_Wunderland.txt") if words != ""]
#fumktion die alle indexe der  worte des Zitats ausgibt
def getwords(zitat):
    blankwordindex = []
    counter = 0
    for i in zitat:
        if i != "":
            blankwordindex.append(counter)
        counter = counter +1
    return blankwordindex
#funktion die alle "zensierten" Worte des Zitats ausgibt
def censoredwords(zitat):
    blankwordindex = []
    counter = 0
    for i in zitat:
        if i == "":
            blankwordindex.append(counter)
        counter = counter +1
    return blankwordindex

words =[ i for i in zitat if i != "_"]
index_words = getwords(zitat)
index_censoredwords = censoredwords(zitat)
print("Das unfertige Zitat lautet:",words)
print("An den Indexen:",index_words,"sind Wörter in dem Zitat vorhanden  ")
#vergleicht die beiden Listen
def checklists(oldlist,newlist,index_words):
    checker = "false"
    wordlist = [i for i in oldlist if i != ""]
    checklist = [ v for i, v  in enumerate(newlist) if i not in index_words ]
    if wordlist ==  checklist:
        checker = "True"
        return checker
    else:
        checker = "false"
        return checker

existing_words = [i for i in zitat if i != ""]
#temporäre Listen
fertiges_zitat = []
fertiges_zitatindex= []
for zahl,b in enumerate(buch):
    for i in index_words:
     if b == zitat[0] and buch[zahl+i] == zitat[i].lower():
        for i in range(len(zitat)):
            fertiges_zitat.append(buch[zahl+i])
            fertiges_zitatindex.append(zahl+i)
        #wenn das Zitat mit allen Überprüfungspunkten übereinstimmt gibt es das fertige Zitat aus
        if len(fertiges_zitat) == len(zitat)and checklists(words, fertiges_zitat,index_censoredwords)== "True":
             print("die Indexliste für das fertige Zitat:",fertiges_zitatindex)
             print("das fertige Zitat lautet:"," ".join(fertiges_zitat))
             zahl =zahl+1
        #löscht die temporäre liste wenn sie die Länge des ursprünglichen Zitat überschreitet
        if len(fertiges_zitat) > len(zitat):
            fertiges_zitat.clear()
            fertiges_zitatindex.clear()





