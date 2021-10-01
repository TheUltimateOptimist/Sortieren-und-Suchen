# insertion sort wählt ein element aus der unsortierten liste und fügt es an die richtige stelle in der sortierten Liste ein,
# indem es am ende der sortierten liste anfängt alle element mit dem einzusortierenden element zu vergleichen,
# und eins weiter  zu schieben, bis die richtige Stelle für das einzusortierende Element gefunden ist
from importlib.machinery import SourceFileLoader
compare = SourceFileLoader(
    "compare.py", "C:/AppDevelopment/Sortieren und Suchen/compare.py").load_module()
# in place


def insertion_sort(liste):
    for i in range(1, len(liste)):
        value = liste[i]
        j = i - 1
        while j >= 0 and compare.compare(value, liste[j], "smaller"):
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = value
    return liste
