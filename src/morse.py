def obtener_codificacion(texto: str) -> list[str]:
    texto = texto.split(" ")
    for i in range(len(texto)):
        if texto[i] == "/":
            texto[i] = " "
    return texto
