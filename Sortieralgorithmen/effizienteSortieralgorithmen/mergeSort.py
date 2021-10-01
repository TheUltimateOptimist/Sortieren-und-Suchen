# Merge Sort teilt die Liste von Zahlen solange in kleinere Teillisten, bis jede Teilliste nicht länger als 1 Element ist
# Anschließend fügt es alle Teillisten wieder in der richtigen Reihenfolge zusammen

import math
from importlib.machinery import SourceFileLoader
compare = SourceFileLoader(
    "compare.py", "C:/AppDevelopment/Sortieren und Suchen/compare.py").load_module()


# index 1 and index 2 identify the part of the list that will be split of of the main list and returned
def split_list(index1, index2, list):
    finalList = []
    for i in range(index1, index2 + 1):
        finalList.append(list[i])
    return finalList


def merge(teil1, teil2):
    n1 = len(teil1)  # Anzahl Elemente in Teil 1
    n2 = len(teil2)  # Anzahl Elemente in Teil 2
    merged = []
    while (n1 > 0) or (n2 > 0):
        # wenn der vom zweiten Stapel schon alles hinzugefügt wurde oder noch nicht alles vom zweiten Stapel hinzugefügt wurde, sich aber auf dem ersten Stapel noch eine Zahl befidet, die größer ist, als die Zahl auf dem zweiten Stapel,
        # wird die entsprechende Zahl des ersten Stapels gemerged
        if (n2 == 0) or ((n1 > 0 and compare.compare(teil1[0], teil2[0], "smaller equals"))):
            merged.append(teil1[0])
            teil1.pop(0)
            n1 -= 1
        # andernfalss muss die Zahl des zweiten Stapels gemerged werden
        else:
            merged.append(teil2[0])
            teil2.pop(0)
            n2 -= 1
    return merged


def merge_sort(liste):
    n = len(liste)
    if n <= 1:
        return liste
    else:
        n1 = math.ceil(n/2)  # Anzahl Elemente der ersten Hälfte
        teil1 = merge_sort(split_list(0, n1-1, liste))
        teil2 = merge_sort(split_list(n1, n-1, liste))
        return merge(teil1, teil2)
