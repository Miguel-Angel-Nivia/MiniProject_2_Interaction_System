import requests
from openal import *

# Codigo Hecho por: Miguel Angel Nivia Y Daniel Vasquez

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

def reproducirSonido(nombre, volumen):
    # Cargar y reproducir el archivo de sonido descargado
    sonido = oalOpen(nombre)
    # Configuracion de sonido
    sonido.set_gain(volumen)  # Volumen (1.0 es el normal)
    sonido.set_position((-1, 0, 0))  # Posición en el espacio (x, y, z)
    """
    En teoria con set_position((x, y, z))
    donde x = 1 es derecha y -1 es izquierda,
    donde y = 1 es arriba y -1 es abajo y
    donde z = 1 cerca(adelante) y -1 lejos(atras)
    pero no funciona al parecer.
    """
    sonido.set_velocity((0, 0, 0))  # Velocidad del sonido (x, y, z)
    sonido.play()
    # Mantener el sonido reproduciéndose
    while sonido.get_state() == AL_PLAYING:
        pass

# Sonido disparo
obtencionSonido("https://drive.google.com/uc?export=download&id=1TQJz68mIqiSVJqwomfhRvDLG2Y_Y02jg", "Sonidos/sonidoDisparo.wav")
reproducirSonido("Sonidos/sonidoDisparo.wav", 1)
"""
# Sonido Empezar(Musica corta epica)
obtencionSonido("https://drive.google.com/uc?export=download&id=1kjZC2SO6ek0cEiTA9nhxDPqhdoqg2gvQ", "Sonidos/sonidoEmpezar.wav")
reproducirSonido("Sonidos/sonidoEmpezar.wav", 1)

# Sonido Radio(Un poco largo)
obtencionSonido("https://drive.google.com/uc?export=download&id=1aq60Dzq8p4WShZVDcmbSCzodskn3NcNs", "Sonidos/sonidoRadio.wav")
reproducirSonido("Sonidos/sonidoRadio.wav", 1)
"""

def main():
    return 0

# Limpiar y cerrar openAL
oalQuit()
