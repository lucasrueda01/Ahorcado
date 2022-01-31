from urllib.request import urlopen
import json
from unidecode import unidecode


def get_palabra():
    respuesta = urlopen("https://palabras-aleatorias-public-api.herokuapp.com/random")
    resultado = json.load(respuesta)
    palabra = resultado['body']['Word']
    palabra = unidecode(palabra)
    return palabra