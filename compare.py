from importlib.machinery import SourceFileLoader
a = SourceFileLoader(
    "accesser.py", "C:/AppDevelopment/Sortieren und Suchen/globalVariables/accesser.py").load_module()


def compare(elementOne, elementTwo, wayOfComparing):
    a.updateVergleiche(a.getVergleiche() + 1)
    if wayOfComparing == "smaller equals":
        if elementOne <= elementTwo:
            return True
        else:
            return False
    elif wayOfComparing == "greater equals":
        if elementOne >= elementTwo:
            return True
        else:
            return False
    elif wayOfComparing == "smaller":
        if elementOne < elementTwo:
            return True
        else:
            return False
    elif wayOfComparing == "greater":
        if elementOne > elementTwo:
            return True
        else:
            return False
    elif wayOfComparing == "equals":
        if elementOne == elementTwo:
            return True
        else:
            return False
