import pytest
from morse import obtener_codificacion, decodificar


@pytest.mark.parametrize(
    "texto_morse,esperado",
    [
        (
            ".--. --- -.. .-. .. .-   .... .- -.-. . .-.   . ... - ---   - --- -.. ---   . .-..   -.. .. .- .-.-.",
            [
                ".--.",
                "---",
                "-..",
                ".-.",
                "..",
                ".-",
                " ",
                "....",
                ".-",
                "-.-.",
                ".",
                ".-.",
                " ",
                ".",
                "...",
                "-",
                "---",
                " ",
                "-",
                "---",
                "-..",
                "---",
                " ",
                ".",
                ".-..",
                " ",
                "-..",
                "..",
                ".-",
                ".-.-.",
            ],
        ),
        (
            ".--. .- ... . / .-.. --- / --.- ..- . / .--. .- ... . / -- .- .- -. .- / .--. .-. --- -- - .- -- . / .- .-.. --. --- / --.- ..- . / ... . --. ..- .. .-. / ... .. . -. -.. --- / ..- ... - . -.. / -. --- / ..- -. / ... --- .-.. -.. .- -.. --- / .--. . .-. ..-. . -.-. - --- --..-- / ... .. -. --- / ..- -. / -... ..- . -. / .... --- -- -... .-. . .-.-.",
            [
                ".--.",
                ".-",
                "...",
                ".",
                " ",
                ".-..",
                "---",
                " ",
                "--.-",
                "..-",
                ".",
                " ",
                ".--.",
                ".-",
                "...",
                ".",
                " ",
                "--",
                ".-",
                ".-",
                "-.",
                ".-",
                " ",
                ".--.",
                ".-.",
                "---",
                "--",
                "-",
                ".-",
                "--",
                ".",
                " ",
                ".-",
                ".-..",
                "--.",
                "---",
                " ",
                "--.-",
                "..-",
                ".",
                " ",
                "...",
                ".",
                "--.",
                "..-",
                "..",
                ".-.",
                " ",
                "...",
                "..",
                ".",
                "-.",
                "-..",
                "---",
                " ",
                "..-",
                "...",
                "-",
                ".",
                "-..",
                " ",
                "-.",
                "---",
                " ",
                "..-",
                "-.",
                " ",
                "...",
                "---",
                ".-..",
                "-..",
                ".-",
                "-..",
                "---",
                " ",
                ".--.",
                ".",
                ".-.",
                "..-.",
                ".",
                "-.-.",
                "-",
                "---",
                "--..--",
                " ",
                "...",
                "..",
                "-.",
                "---",
                " ",
                "..-",
                "-.",
                " ",
                "-...",
                "..-",
                ".",
                "-.",
                " ",
                "....",
                "---",
                "--",
                "-...",
                ".-.",
                ".",
                ".-.-.",
            ],
        ),
        (
            "-. --- ... --- - .-. --- ... / ... --- -- --- ... / .-.. --- ... / -- .- .-.. -.. .. - --- ... / --. ..- .- .-. -.. .. .- -. . ... / -.. . / .-.. .- / --. .- .-.. .- -..- .. .- .-.-.",
            [
                "-.",
                "---",
                "...",
                "---",
                "-",
                ".-.",
                "---",
                "...",
                " ",
                "...",
                "---",
                "--",
                "---",
                "...",
                " ",
                ".-..",
                "---",
                "...",
                " ",
                "--",
                ".-",
                ".-..",
                "-..",
                "..",
                "-",
                "---",
                "...",
                " ",
                "--.",
                "..-",
                ".-",
                ".-.",
                "-..",
                "..",
                ".-",
                "-.",
                ".",
                "...",
                " ",
                "-..",
                ".",
                " ",
                ".-..",
                ".-",
                " ",
                "--.",
                ".-",
                ".-..",
                ".-",
                "-..-",
                "..",
                ".-",
                ".-.-.",
            ],
        ),
        (
            "-.-- --- / ... --- .-.. --- / .- -.-. - ..- --- / -.-. --- -- --- / ... .. / . -. / ...- . .-. -.. .- -.. / .-.. --- / ... ..- .--. .. . .-. .- / - --- -.. --- .-.-.",
            [
                "-.--",
                "---",
                " ",
                "...",
                "---",
                ".-..",
                "---",
                " ",
                ".-",
                "-.-.",
                "-",
                "..-",
                "---",
                " ",
                "-.-.",
                "---",
                "--",
                "---",
                " ",
                "...",
                "..",
                " ",
                ".",
                "-.",
                " ",
                "...-",
                ".",
                ".-.",
                "-..",
                ".-",
                "-..",
                " ",
                ".-..",
                "---",
                " ",
                "...",
                "..-",
                ".--.",
                "..",
                ".",
                ".-.",
                ".-",
                " ",
                "-",
                "---",
                "-..",
                "---",
                ".-.-.",
            ],
        ),
        (
            "-.-. .... .. -.-. --- ... / . ... - --- -.-- / .-.. .-.. . ...- .- -. -.. --- / .-.. .- / ..-. .. . ... - .- / .... .- -.-. .. .- / ..- ... - . -.. . ... .-.-.",
            [
                "-.-.",
                "....",
                "..",
                "-.-.",
                "---",
                "...",
                " ",
                ".",
                "...",
                "-",
                "---",
                "-.--",
                " ",
                ".-..",
                ".-..",
                ".",
                "...-",
                ".-",
                "-.",
                "-..",
                "---",
                " ",
                ".-..",
                ".-",
                " ",
                "..-.",
                "..",
                ".",
                "...",
                "-",
                ".-",
                " ",
                "....",
                ".-",
                "-.-.",
                "..",
                ".-",
                " ",
                "..-",
                "...",
                "-",
                ".",
                "-..",
                ".",
                "...",
                ".-.-.",
            ],
        ),
    ],
)
def test_obtener_codificacion(texto_morse, esperado):
    assert obtener_codificacion(texto_morse) == esperado


@pytest.mark.parametrize(
    "arreglo_morse,esperado",
    [
        (
            [
                ".--.",
                "---",
                "-..",
                ".-.",
                "..",
                ".-",
                " ",
                "....",
                ".-",
                "-.-.",
                ".",
                ".-.",
                " ",
                ".",
                "...",
                "-",
                "---",
                " ",
                "-",
                "---",
                "-..",
                "---",
                " ",
                ".",
                ".-..",
                " ",
                "-..",
                "..",
                ".-",
                ".-.-.",
            ],
            "podria hacer esto todo el dia",
        )
    ],
)
def test_decodificar(arreglo_morse, esperado):
    assert decodificar(arreglo_morse) == esperado
