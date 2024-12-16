from arbol_morse import buscar, ARBOL_MORSE


def obtener_codificacion(texto: str) -> list[str]:
    """
    Este texto tiene que estar en formato morse (.,-, , ), espacio para separar
    letras y barra para separar palabras esta funcion tiene que estos
    caracteres a una lista con puntos y rayas y espacios para palabras.

    Por ejemplo:
        Entrada: ".--. --- -.. .-. .. .-   .... .- -.-. . .-.   . ... - ---   - --- -.. ---   . .-..   -.. .. .- .-.-."
        Salida: [".--.","---","-..",".-.","..",".-"," ","....",".-","-.-.",".",".-."," ",".","...","-","---"," ","-","---","-..","---"," ",".",".-.."," ","-..","..",".-",".-.-."]
    """
    texto = texto.split(" ")
    for i in range(len(texto)):
        if texto[i] == "/":
            texto[i] = " "
    return texto


def decodificar(lista_texto: list[str]):
    texto_final = ""
    for caracter in lista_texto:
        if caracter == " ":
            texto_final += " "
        else:
            texto_final += buscar(ARBOL_MORSE, caracter)
    return texto_final