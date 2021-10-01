import time
from effizienteSortieralgorithmen.mergeSort import merge_sort
from effizienteSortieralgorithmen.quickSort import quick_sort
from einfacheSortieralgorithmen.insertionSort import insertion_sort
from einfacheSortieralgorithmen.bubbleSort import bubble_sort
from einfacheSortieralgorithmen.selectionSort import selection_sort
from importlib.machinery import SourceFileLoader
a = SourceFileLoader(
    "accesser.py", "C:/AppDevelopment/Sortieren und Suchen/globalVariables/accesser.py").load_module()


def generateList(length, startOfNumberRange, endOfNumberRange):
    import sys
    sys.setrecursionlimit(length + 100)
    import random
    outputList = []
    for _ in range(length):
        outputList.append(random.randint(startOfNumberRange, endOfNumberRange))
    return outputList


def werteAus(name, algorithm, liste):
    a.updateVergleiche(0)
    currentSeconds = time.time()
    algorithm(liste)
    print(
        f"{name} brauchte {time.time() - currentSeconds} Sekunden und {a.getVergleiche()} vergleiche")


def testAlgorithms(list):
    unsortedList = []
    for i in range(len(list)):
        unsortedList.append(list[i])
    werteAus("Bubble Sort", bubble_sort, list)
    list = unsortedList
    werteAus("Insertion Sort", insertion_sort, list)
    list = unsortedList
    werteAus("Selection Sort", selection_sort, list)
    list = unsortedList
    werteAus("Quick Sort", quick_sort, list)
    list = unsortedList
    werteAus("Merge Sort", merge_sort, list)


testAlgorithms(generateList(1000, 0, 100))
