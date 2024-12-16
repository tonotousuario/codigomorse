class NodoMorse:
    def __init__(self, valor: str | None = None, letra: str | None = None):
        self.valor = valor
        self.letra = letra
        self.derecha = None
        self.izquerda = None

    def __str__(self):
        return f"{self.letra} -> ({self.valor})"


def insertar(raiz, letra: str, morse: str):
    actual = raiz

    for caracter in morse:
        if caracter == ".":
            if actual.izquerda is None:
                actual.izquerda = NodoMorse(".")
            actual = actual.izquerda
        elif caracter == "-":
            if actual.derecha is None:
                actual.derecha = NodoMorse("-")
            actual = actual.derecha

    actual.letra = letra


def buscar(raiz, morse: str):
    if morse == ".-.-.":
        return ""
    actual = raiz

    for caracter in morse:
        if caracter == ".":
            actual = actual.izquerda
        elif caracter == "-":
            actual = actual.derecha

    return actual.letra


def inorden(raiz):
    if raiz is None:
        return

    inorden(raiz.izquerda)
    print(raiz)
    inorden(raiz.derecha)


ARBOL_MORSE = NodoMorse()

# Lista de morse
insertar(ARBOL_MORSE, "a", ".-")
insertar(ARBOL_MORSE, "b", "-...")
insertar(ARBOL_MORSE, "c", "-.-.")
insertar(ARBOL_MORSE, "d", "-..")
insertar(ARBOL_MORSE, "e", ".")
insertar(ARBOL_MORSE, "f", "..-.")
insertar(ARBOL_MORSE, "g", "--.")
insertar(ARBOL_MORSE, "h", "....")
insertar(ARBOL_MORSE, "i", "..")
insertar(ARBOL_MORSE, "j", ".---")
insertar(ARBOL_MORSE, "k", "-.-")
insertar(ARBOL_MORSE, "l", ".-..")
insertar(ARBOL_MORSE, "m", "--")
insertar(ARBOL_MORSE, "n", "-.")
insertar(ARBOL_MORSE, "o", "---")
insertar(ARBOL_MORSE, "p", ".--.")
insertar(ARBOL_MORSE, "q", "--.-")
insertar(ARBOL_MORSE, "r", ".-.")
insertar(ARBOL_MORSE, "s", "...")
insertar(ARBOL_MORSE, "t", "-")
insertar(ARBOL_MORSE, "u", "..-")
insertar(ARBOL_MORSE, "v", "...-")
insertar(ARBOL_MORSE, "w", ".--")
insertar(ARBOL_MORSE, "x", "-..-")
insertar(ARBOL_MORSE, "y", "-.--")
insertar(ARBOL_MORSE, "z", "--..")
insertar(ARBOL_MORSE, "0", "-----")
insertar(ARBOL_MORSE, "1", ".----")
insertar(ARBOL_MORSE, "2", "..---")
insertar(ARBOL_MORSE, "3", "...--")
insertar(ARBOL_MORSE, "4", "....-")
insertar(ARBOL_MORSE, "5", ".....")
insertar(ARBOL_MORSE, "6", "-....")
insertar(ARBOL_MORSE, "7", "--...")
insertar(ARBOL_MORSE, "8", "---..")
insertar(ARBOL_MORSE, "9", "----.")
