# selection sort geht die unsortierte liste immer wieder durch und sucht
# das kleinste element und fügt es an die sortierte liste an bis die liste komplett
# sortiert ist: sortieren durch auswählen
from importlib.machinery import SourceFileLoader
compare = SourceFileLoader(
    "compare.py", "C:/AppDevelopment/Sortieren und Suchen/compare.py").load_module()
# in place


def selection_sort(liste):
    for i in range(0, len(liste) - 1):
        smallestElementIndex = i
        for j in range(i + 1, len(liste)):
            if compare.compare(liste[j], liste[smallestElementIndex], "smaller"):
                smallestElementIndex = j
        swappedElement = liste[i]
        liste[i] = liste[smallestElementIndex]
        liste[smallestElementIndex] = swappedElement
    return liste
