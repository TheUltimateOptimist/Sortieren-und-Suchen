from importlib.machinery import SourceFileLoader
variables = SourceFileLoader(
    "variables.py", "C:/AppDevelopment/Sortieren und Suchen/globalVariables/variables.py").load_module()


def updateVergleiche(value):
    variables.vergleiche = value


def getVergleiche():
    return variables.vergleiche
