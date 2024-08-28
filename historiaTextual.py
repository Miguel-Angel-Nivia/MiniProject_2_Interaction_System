import requests
from openal import *

# Codigo Hecho por: Miguel Angel Nivia Y Daniel Vasquez
# Antes de usar el codigo, ejecutar en cmd un pip install requests, pyopenal y ospath.
# Ademas de que tambien los archivos wav deben pasar a mono con audacity para que funcionen adecuadamente.

# Abrir OpenAl
oalInit()

# Funcion para descargar y obtencion de los sonidos a usar desde google drive, con el link y el nombre ambos en string con que se guardara.
def obtencionSonido(link, nombre):
    url = link
    file_name = nombre
    # Descargar y verificar si el archivo de sonido de Google Drive ya esta en el pc.
    if not os.path.exists(file_name):
        with open(nombre, 'wb') as file:
            file.write(requests.get(url).content)
            print("Archivo descargado exitosamente.")
    else:
        print("No se necesita descargar.")

def reproducirSonido(nombre, volumen, posEspacial, velVolumen):
    # Cargar y reproducir el archivo de sonido descargado
    sonido = oalOpen(nombre)
    # Configuracion de sonido
    sonido.set_gain(volumen)  # Volumen (1.0 es el normal)
    sonido.set_position((posEspacial[0], posEspacial[1], posEspacial[2]))  # Posición en el espacio (x, y, z)
    """
    Nota:
    set_position((x, y, z))
    donde x = 1 es derecha y -1 es izquierda,
    donde y = 1 es arriba y -1 es abajo y
    donde z = 1 cerca(adelante) y -1 lejos(atras)
    """
    sonido.set_velocity((velVolumen[0], velVolumen[1], velVolumen[2]))  # Velocidad del sonido (x, y, z)
    sonido.play()
    # Mantener el sonido reproduciéndose
    while sonido.get_state() == AL_PLAYING:
        pass
     
# Sonido disparo
obtencionSonido("https://drive.google.com/uc?export=download&id=1QBLLeiHKAXqpMUdgQXXmFMPBkvVAvv1R", "Sonidos/sonidoDisparo.wav")
reproducirSonido("Sonidos/sonidoDisparo.wav", 1, [1, 0, 0], [0, 0, 0])
"""
# Sonido Empezar(Musica corta epica)
obtencionSonido("https://drive.google.com/uc?export=download&id=1Zjd5gk4rGwL3NseRcXSlNCEbVwl5OVgJ", "Sonidos/sonidoEmpezar.wav")
reproducirSonido("Sonidos/sonidoEmpezar.wav", 1, [0, 0, -1], [0, 0, 0])

# Sonido Radio(Un poco largo)
obtencionSonido("https://drive.google.com/uc?export=download&id=1YGA-36kbX19x_aelRWG484o0imdqFp1U", "Sonidos/sonidoRadio.wav")
reproducirSonido("Sonidos/sonidoRadio.wav", 1, [0, 0, 0], [0, 0, 0])
"""

def main():
    # Desarrollo Historia
    return 0

# Limpiar y cerrar openAL
oalQuit()
