
# Verbesserung: Satzzeichen als Set speichern
satzzeichen_set = set("«!#$%&'()*+,-./:;<=>?@[\]^_`{|}~. »")

def dateiauswertung(dateiname):
    with open(dateiname, encoding='utf-8') as datei:
        text = datei.read()
        wörter = text.split()
        wörter = [''.join(Buchstabe for Buchstabe in wort if Buchstabe  not in satzzeichen_set) for wort in wörter if wort]
    return wörter

for i in range(6):
    zitat_dateiname = f"stoerung{i}.txt"
    zitat = list(dateiauswertung(zitat_dateiname))
    buch = [wort.lower() for wort in dateiauswertung("Alice_im_Wunderland.txt") if wort != ""]

    wörter_indexe, zensierte_wörter_indexe = [index for index, wort in enumerate(zitat) if wort != ""], [index for index, wort in enumerate(zitat) if wort == ""]

    print(f"Das unfertige Zitat aus {zitat_dateiname} lautet: {[wort for wort in zitat if wort != '_']}")
    print(f"An den Indexen: {wörter_indexe} sind Wörter in dem Zitat vorhanden")

    def check_lists(altes_wort, neues_wort, wörter_indexe):
        # Verbesserung: Direkter Vergleich der Listen
        return all(altes_wort == neues_wort for altes_wort, neues_wort in zip((wort for wort in altes_wort if wort != ""), (v for zahl, v in enumerate(neues_wort) if zahl not in wörter_indexe)))

    temporäre_liste = []
    for index, wort in enumerate(buch):
        if all(wort == zitat[0] and buch[index + neuer_index] == zitat[neuer_index].lower() for neuer_index in wörter_indexe):
            fertiges_zitat, fertiges_zitat_index = [buch[index + länge] for länge in range(len(zitat))], [index + länge for länge in range(len(zitat))]
            if len(fertiges_zitat) == len(zitat) and check_lists(zitat, fertiges_zitat, zensierte_wörter_indexe):
                temporäre_liste.append((fertiges_zitat, fertiges_zitat_index))

    for fertiges_zitat, fertiges_zitat_index in temporäre_liste:
        fertiges_zitat_text = ' '.join(fertiges_zitat)
        print(f"Die Indexliste für das fertige Zitat: {fertiges_zitat_index}")
        print(f"Das fertige Zitat lautet: {fertiges_zitat_text}")

    print("--------------------------------------")
print("--------------------------------------")
