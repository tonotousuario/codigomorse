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


raiz = NodoMorse()

# Lista de morse
insertar(raiz, "a", ".-")
insertar(raiz, "b", "-...")
insertar(raiz, "c", "-.-.")
insertar(raiz, "d", "-..")
insertar(raiz, "e", ".")
insertar(raiz, "f", "..-.")
insertar(raiz, "g", "--.")
insertar(raiz, "h", "....")
insertar(raiz, "i", "..")
insertar(raiz, "j", ".---")
insertar(raiz, "k", "-.-")
insertar(raiz, "l", ".-..")
insertar(raiz, "m", "--")
insertar(raiz, "n", "-.")
insertar(raiz, "o", "---")
insertar(raiz, "p", ".--.")
insertar(raiz, "q", "--.-")
insertar(raiz, "r", ".-.")
insertar(raiz, "s", "...")
insertar(raiz, "t", "-")
insertar(raiz, "u", "..-")
insertar(raiz, "v", "...-")
insertar(raiz, "w", ".--")
insertar(raiz, "x", "-..-")
insertar(raiz, "y", "-.--")
insertar(raiz, "z", "--..")
insertar(raiz, "0", "-----")
insertar(raiz, "1", ".----")
insertar(raiz, "2", "..---")
insertar(raiz, "3", "...--")
insertar(raiz, "4", "....-")
insertar(raiz, "5", ".....")
insertar(raiz, "6", "-....")
insertar(raiz, "7", "--...")
insertar(raiz, "8", "---..")
insertar(raiz, "9", "----.")
