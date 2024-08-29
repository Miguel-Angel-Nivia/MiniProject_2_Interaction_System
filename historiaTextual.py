import requests
from openal import *

# Codigo Hecho por: Miguel Angel Nivia Y Daniel Vasquez
# Antes de usar el codigo, ejecutar en cmd un pip install requests, pyopenal y ospath.
# Ademas de que tambien los archivos wav deben pasar a mono con audacity para que funcionen adecuadamente.

# Abrir OpenAl
oalInit()

# Crear un listener (el jugador)
listener = Listener()
# Colocar el listener en el centro
listener.set_position((0, 0, 0))
listener.set_velocity((0,0,0))
listener.set_orientation((0, 0, -1, 0, 1, 0))

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

def dialogo(texto):
    return input(texto + "\nPresiona enter para continuar...")

def main():
    # Desarrollo Historia
    dialogo("Dios - Frederic es un aventurero común y corriente que hace parte de un grupo de mercenarios, el cual despierta después de una exploración que salió mal, con un fuerte dolor de cabeza.")
    dialogo("Frederic - Ahg que.. que paso? ¿Dónde estoy? No veo absolutamente nada, hay un olor a humo, estoy mojado y repleto de lodo.")

    # Opciones del jugador: Levantarse o Mirar a tu alrededor
    levantarse = False
    mirar = False

    while not levantarse or not mirar:
        decision1 = input("¿Qué quieres hacer? 1. Levantarse \n 2. Mirar a tu alrededor \n: ")
        if decision1 == "1":
            dialogo("Frederic - <Se sacude la ropa> ¿Qué es esto? ¿una herida? Mierda tengo una cortada infectada en el abdomen.")
            levantarse = True
        elif decision1 == "2":
            dialogo("Frederic - Qué carajo no se ve nada alrededor, ¿Uh?… ¿Qué es eso? Algo brilla al fondo.")
            mirar = True
        else:
            print("Opción no válida. Intenta de nuevo.")

    # Avanzar en la historia
    print("Frederic - Parece que estoy en una especie de cueva ¿Dónde demonios está mi equipo? Demonios esa espada me costó tanto como una semana en el burdel, me acercaré a esa luz, puede que encuentre algo de utilidad o ver algo.")
    print("Dios - Frederic confundido y sin saber dónde está, se acerca a la luz con cautela.")
    print("Frederic - ¿Una fogata? ¿Qué hace una fogata aquí?")
    print("Frederic - No veo nada de relevancia excepto este palo seco.")
    
    # Opciones del jugador: Hacer una antorcha o Arrojar el palo al fuego
    decision2 = input("¿Qué quieres hacer? 1. Hacer una antorcha \n 2. Arrojar el palo al fuego \n: ")
    if decision2 == "1":
        print("Frederic - Parece que este palo puede servir para hacer una antorcha.")
        # Ruta 1
        print("Dios - Frederic ahora con antorcha en mano, se dispuso a explorar las inmediaciones de la cueva.")
        print("Frederic - Ojalá ahora encuentre esa maldita espada, Pero que carajo… toda la cueva está llena de arañazos y de un extraño líquido verde…")
        print("Frederic - ¿Eso es un derrumbe? Veo algo de luz del otro lado…, ¿Que mierda paso aquí? Este camino está bloqueado <sonidos de batalla y gritos>...")
        print("Frederic - ¿Qué fue eso? ¿Quién está ahí? ¿Sal y pelea cobarde?.")

        despejar = False
        volver = False

        while despejar == False and volver == False:
            decision3 = print("¿Qué quieres hacer? 1. Devolverse y avanzar por el camino de la fogata \n 2. Despejar el camino bloqueado \n: ").lower()
            if decision3 == "devolverse y avanzar por el camino de la fogata":
                print("Frederic - No sé que fue eso, mejor me muevo rápido, me devuelvo a la fogata y me preparo para luchar.")
                print("Frederic - <Divisas algo en el camino> aquí está la pechera de compré en rebaja, qué porquería de pechera, casi me cuesta la vida, tiene una gran abertura en el abdomen, ¿Por qué estaba aquí? Las correas están intactas.")
                print("Frederic - ¿Quién me la habrá quitado? Bueno eso no importa, me la pondré, de algo debe servir, esto es mejor que nada.")
                tiene_pechera = True
            else:
                print("Frederic - Supongo que puedo intentar salir por donde entré <Sonido de rocas>.")
                print("Frederic - Carajo llevo varios minutos y estas piedras no se mueven ni un centímetro, maldita sea.")
                print("Frederic - Esta cueva es más grande de lo que pensaba, está llena de estalagmitas y de estalactitas, sin quitar de lado esta asquerosa cantidad de murciélagos <Sonidos de ese animal a lo lejos>.")
                print("Frederic - Mejor me devuelvo hacia la fogata y me preparo para avanzar.")
                tiene_pechera = False

    elif decision2 == "2":
        print("Frederic - Mierda casi me quemo, el fuego creció demasiado, por lo menos ahora puedo ver lo que está en la cercanía.")
        # Ruta 2
        print("Dios - Frederic sin nada de luz para explorar, se sienta a ver la fogata, mientras recuerdos llegan a su mente <Sonido de risas y gente hablando en un bar>, luego de eso la fogata se extingue por completo.")
        print("Frederic - Ahora solo tengo dos opciones, avanzar por esta cueva o morir de viejo esperando a que pase algo interesante…")
        tiene_pechera = False

    else:
        print("Opción no válida. Intenta de nuevo.")

    # Unión de rutas anteriores
    print("Frederic - Llevo quince minutos caminando, ¿Dónde está la salida?, esta cueva es enorme, al menos veo el camino con este río fosforescente color verde vómito <sonido de río>.")
    print("Frederic - Qué suerte la mía, esta cueva será mi tumba y este río apesta a cadáver de grifo.")
    print("Frederic - ¿Qué es eso? <Sonido de rocas moviéndose>… Bien!!!! mi espada, pensé que no te encontraría, ven aquí preciosa, te besaría, pero no quiero hacerme otra herida.")
    print("Frederic - Aún manchada de verde tienes tanto filo como las palabras de verónica.")
    return 0

main()

# Limpiar y cerrar openAL
oalQuit()
