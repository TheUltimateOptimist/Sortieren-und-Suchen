import time
from binaereSuche import binaere_Suche
from lineareSuche import lineare_Suche
from importlib.machinery import SourceFileLoader
a = SourceFileLoader(
    "accesser.py", "C:/AppDevelopment/Sortieren und Suchen/globalVariables/accesser.py").load_module()


def generateList(length):
    outputList = []
    for i in range(length):
        outputList.append(i)
    return outputList


def werteAus(name, liste, value):
    a.updateVergleiche(0)
    currentSeconds = time.time()
    if name == "Lineare Suche":
        lineare_Suche(liste, value)
    elif name == "Binäre Suche":
        binaere_Suche(liste, value, 0, len(liste) - 1)
    print(
        f"Die {name} brauchte {time.time() - currentSeconds} Sekunden und {a.getVergleiche()} vergleiche")


def testAlgorithms(list):
    import random
    value = random.randint(a=0, b=len(list) - 1)
    werteAus("Lineare Suche", list, value)
    werteAus("Binäre Suche", list, value)


testAlgorithms(generateList(100000000))
