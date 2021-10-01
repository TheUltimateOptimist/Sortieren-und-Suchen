# Die lineare Suche geht ein Liste von vorne nach hinten durch, bis sie das gesuchte Element
# gefunden hat. Dementsprechend beträgt die Worst-Case-Komplexität O(n)

from importlib.machinery import SourceFileLoader
compare = SourceFileLoader(
    "compare.py", "C:/AppDevelopment/Sortieren und Suchen/compare.py").load_module()


def lineare_Suche(liste, element):
    for i, value in enumerate(liste):
        if compare.compare(value, element, "equals"):
            return i
