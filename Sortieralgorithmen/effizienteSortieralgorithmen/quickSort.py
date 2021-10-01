# Quicksort wählt das erste Element der Liste und teilt die Liste in zwei Teile, wobei der erste Teil die Elemente enthält die kleiner gleich dem ersten und der zweite Teile die Elmente enthält, die größer als das erste, sind.
# Anschließend fügt er an dem ersten Teil das erste Element und den zweiten Teil an. Dieses Verfahren wird rekursiv ausgeführt.
from importlib.machinery import SourceFileLoader
compare = SourceFileLoader(
    "compare.py", "C:/AppDevelopment/Sortieren und Suchen/compare.py").load_module()


def quick_sort(liste):
    if len(liste) <= 1:
        return liste
    else:
        teil1 = []
        teil2 = []
        for j in range(1, len(liste)):
            if compare.compare(liste[j], liste[0], "smaller equals"):
                teil1.append(liste[j])
            else:
                teil2.append(liste[j])
        teil1 = quick_sort(teil1)
        teil2 = quick_sort(teil2)
        return teil1 + [liste[0]] + teil2
