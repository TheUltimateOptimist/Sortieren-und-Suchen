# bubble sort geht die zu sortierende List immer wieder von links nach rechts durch und tauscht
# die element die in der falschen Reihenfolge stehen bis die Liste sortiert ist
from importlib.machinery import SourceFileLoader
compare = SourceFileLoader(
    "compare.py", "C:/AppDevelopment/Sortieren und Suchen/compare.py").load_module()


# in place
def bubble_sort(liste):
    for i in range(1, len(liste)):
        noElementWasSwapped = True
        for j in range(1, len(liste) - i + 1):
            if compare.compare(liste[j], liste[j - 1], "smaller"):
                element = liste[j]
                liste[j] = liste[j - 1]
                liste[j - 1] = element
                noElementWasSwapped = False
        if noElementWasSwapped:
            break
    return liste
