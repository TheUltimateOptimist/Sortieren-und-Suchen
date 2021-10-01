# die binäre Suche startet mit dem mittlersten Element der zu durchsuchenden List. Ist das gesuchte Element größer, sucht sie in der rechten Hälfte der
# Restliste weiter, ist es kleiner sucht sie in der linken Hälfte der Restliste weiter. Dieses Schema wird rekursiv wiederholt, bis das Element
# gefunden ist. Bei jedem Durchgang wird die Größe der zu durchsuchenden Liste halbiert. Die Worst-Case-Komplexität beträgt dementsprechend O(log(n))
import math
from importlib.machinery import SourceFileLoader
compare = SourceFileLoader(
    "compare.py", "C:/AppDevelopment/Sortieren und Suchen/compare.py").load_module()


def binaere_Suche(liste, value, leftIndex, rightIndex):
    print(str(leftIndex) + " ," + str(rightIndex))
    if len(liste) <= 2:
        if compare.compare(liste[leftIndex], value, "equals"):
            return leftIndex
        elif compare.compare(liste[rightIndex], value, "equals"):
            return rightIndex
        else:
            return None
    else:
        middleIndex = leftIndex + math.floor((rightIndex - leftIndex + 1)/2)
        print(middleIndex)
        if compare.compare(liste[middleIndex], value, "equals"):
            return middleIndex
        elif compare.compare(value, liste[middleIndex], "greater"):
            return binaere_Suche(liste, value, middleIndex + 1, rightIndex)
        else:
            return binaere_Suche(liste, value, leftIndex, middleIndex - 1)
