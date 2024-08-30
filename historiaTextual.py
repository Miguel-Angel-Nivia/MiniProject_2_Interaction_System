import requests, os, time
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

def obtencionSonido(link, nombre):
    """
    # Funcion para descargar y obtencion de los sonidos a usar desde google drive, con el link y el nombre ambos en string con que se guardara.

    Argumentos:
        link (str): Direccion url del archivo compartido desde Drive.
        nombre (str): Nombre del archivo de sonido.

    Excpecion:
        Si no esta descargado el archivo se descargara inmediatamente, en caso contrario pasa.
    """
    url = link
    file_name = nombre

    # Crear la carpeta "Sonidos" si no existe
    directorio = os.path.dirname(file_name)
    if directorio and not os.path.exists(directorio):
        os.makedirs(directorio)

    # Descargar y verificar si el archivo de sonido de Google Drive ya esta en el pc.
    if not os.path.exists(file_name):
        with open(nombre, 'wb') as file:
            file.write(requests.get(url).content)
            #print("Archivo descargado exitosamente.")
    else:
        pass
        #print("No se necesita descargar.")
    return 0

def reproducirSonido(nombre, volumen, posEspacial, velEspacial, velocidad, tiempo, loop):
    """
    # Funcion para reproducir los sonidos, donde se puede modificar varias caracteristicas del mismo.

    Argumentos:
        nombre (str): Nombre del archivo de sonido a reproducir.
        volumen (float): Valor numerico del volumen del sonido donde 1.0 es el estandar. 
        posEspacial (list(float)): Lista de enteros de tamaño 3 que contiene las posiciones "x", "y" y "z" del sonido espacialmente.
                                donde x = 1 es derecha y -1 es izquierda,
                                donde y = 1 es arriba y -1 es abajo y
                                donde z = 1 cerca(adelante) y -1 lejos(atras)
        velEspacial (list(float)): Lista de enteros de tamaño 3 que contiene las velocidades "x", "y" y "z" del sonido.
        velocidad (float): velocidad de reproduccion del sonido.
        tiempo (float): tiempo de ejecucion antes de que suente el sonido
        loop (bool): Bandera que indica si el sonido se reproduce infinitamente o no.
    """
    # Cargar y reproducir el archivo de sonido descargado
    sonido = oalOpen(nombre)
    # Configuracion de sonido
    sonido.set_gain(volumen)
    sonido.set_position((posEspacial[0], posEspacial[1], posEspacial[2]))
    sonido.set_velocity((velEspacial[0], velEspacial[1], velEspacial[2]))
    sonido.set_pitch(velocidad)
    if tiempo != 0:
        time.sleep(tiempo)
    if loop == True:
        sonido.set_looping(True)
        # Mantener el sonido reproduciéndose en loop hasta que el usuario presione Enter
        sonido.play()
        try:
            input("\n                         Presiona enter para continuar...                            \n\n")
        finally:
            sonido.stop()
    else:
        sonido.play()
        # Mantener el sonido reproduciéndose
        while sonido.get_state() == AL_PLAYING:
            pass
    return 0

"""
# Sonido disparo
obtencionSonido("https://drive.google.com/uc?export=download&id=1QBLLeiHKAXqpMUdgQXXmFMPBkvVAvv1R", "Sonidos/sonidoDisparo.wav")
"""

def avanzar():
    """
    # Funcion para interaccion con el usuario para avanzar.
    """
    input("\nPresiona enter para continuar...\n")
    return os.system('cls')

def descargas():
    """
    # Funcion para descargar los sonidos.
    """
    # Sonido de inicio
    obtencionSonido("https://drive.google.com/uc?export=download&id=1Zjd5gk4rGwL3NseRcXSlNCEbVwl5OVgJ", "Sonidos/sonidoEmpezar.wav")
    # Sonido Musica Menu
    obtencionSonido("https://drive.google.com/uc?export=download&id=1XiK9YyjNfmglSSiN-JeeLBTCFbonrGuJ", "Sonidos/sonidoInicioMenu.wav")
    # Sonido de viento
    obtencionSonido("https://drive.google.com/uc?export=download&id=1T5o32HyMdtbAWLhzDZjl1GiAGwjd5xJ2", "Sonidos/sonidoViento.wav")
    # Sonido de gotas de agua
    obtencionSonido("https://drive.google.com/uc?export=download&id=1yO-1uoF4tK0Xpay14Om46SPgS3Lj_6Ma", "Sonidos/sonidoGotasCueva.wav")
    # Sonido Seleccion Usuario
    obtencionSonido("https://drive.google.com/uc?export=download&id=1ytT4w12rXtc3yytf-S7i3K5ffK86Sbqq", "Sonidos/sonidoSeleccion.wav")
    # Sonido Herida Frederic
    obtencionSonido("https://drive.google.com/uc?export=download&id=1jUfAFOve5z4N-hgRZ1lSX95Jls5kAKEq", "Sonidos/sonidoHeridaFrederic.wav")
    # Sonido Duda Frederic
    obtencionSonido("https://drive.google.com/uc?export=download&id=1t_EpVH0BYOzrYzk-liCL0KpDSyLRf7VE", "Sonidos/sonidoDudaFrederic.wav")
    # Sonido Pasos Humano
    obtencionSonido("https://drive.google.com/uc?export=download&id=1wnRnepYQXsvWRpjG7BR7A2UrZMYZYse9", "Sonidos/sonidoPasosHumano.wav")
    # Sonido Fogata
    obtencionSonido("https://drive.google.com/uc?export=download&id=1Z3mWfJLeb2_XibIkEexpym_g3rAaQs1H", "Sonidos/sonidoFogata.wav")
    # Sonido Crafteo
    obtencionSonido("https://drive.google.com/uc?export=download&id=13L3-VBFhQD94Q-2sX63Dg6IbjF1ahkWI", "Sonidos/sonidoCrafteo.wav")
    # Sonido Baba
    obtencionSonido("https://drive.google.com/uc?export=download&id=1qAjyBHFvrIQ9yieGY9YCwuprQJnidrrv", "Sonidos/sonidoBaba.wav")
    # Sonido Rocas Cayendo
    obtencionSonido("https://drive.google.com/uc?export=download&id=1B67u8L2VqImjrEz4aTi3_c37fLycgEUB", "Sonidos/sonidoRocasCayendo.wav")
    # Sonido Grito Mujer
    obtencionSonido("https://drive.google.com/uc?export=download&id=1WrsJLof67aRzAjEjb-xGfyBTkJIpNznc", "Sonidos/sonidoMujerGritando.wav")
    # Sonido Rugido Monstruo
    obtencionSonido("https://drive.google.com/uc?export=download&id=1ZJJ40UeycO9SEq7ATx4xeDAkJEO9m340", "Sonidos/sonidoMonstruoRugido.wav")
    # Sonido Correr Humano
    obtencionSonido("https://drive.google.com/uc?export=download&id=12txHUcxAB1vFDu3vW0q5XFuBH_c_X1hO", "Sonidos/sonidoCorrerHumano.wav")
    # Sonido Brillo
    obtencionSonido("https://drive.google.com/uc?export=download&id=1u0buluO-HWZkdtea5KylZX8hP_yf-wjN", "Sonidos/sonidoBrillo.wav")
    # Sonido Armadura
    obtencionSonido("https://drive.google.com/uc?export=download&id=114pQGdwaYBJj5l9eLYgiiMkf8Tn5qYt2", "Sonidos/sonidoArmadura.wav")
    # Sonido Murcielagos
    obtencionSonido("https://drive.google.com/uc?export=download&id=1AgNgY4As2NCVQ6kQasTUsN2PkOSbTiQv", "Sonidos/sonidoMurcielagos.wav")
    # Sonido Fuego Incrementa
    obtencionSonido("https://drive.google.com/uc?export=download&id=15glPsbJqf-clAfDFb9fGR-A3dgeWEzyB", "Sonidos/sonidoFuegoIncremento.wav")
    # Sonido Bar
    obtencionSonido("https://drive.google.com/uc?export=download&id=1HYgeonZJ-ho5MQonHgU5B2ZY6pXjh0Fe", "Sonidos/sonidoBar.wav")
    # Sonido Rio
    obtencionSonido("https://drive.google.com/uc?export=download&id=1Z-E8v04f1w2biVErS7GSz2dRiSiRlNzt", "Sonidos/sonidoRio.wav")
    # Sonido Recoger
    obtencionSonido("https://drive.google.com/uc?export=download&id=1Il2f4gyo8wCgM8xg7aSmkscBbCp9SmcC", "Sonidos/sonidoRecoger.wav")
    # Sonido Espada
    obtencionSonido("https://drive.google.com/uc?export=download&id=1PgomXpU6lcbwr1u7CfdgOZ1z5UheDm0R", "Sonidos/sonidoEspada.wav")
    # Sonido Suspiro
    obtencionSonido("https://drive.google.com/uc?export=download&id=13TgeUdtdniIXNQ94uZ5cc_EDVpLNhQk4", "Sonidos/sonidoSuspiro.wav")
    # Sonido Risa Frederic
    obtencionSonido("https://drive.google.com/uc?export=download&id=1NtSi7TOWDUFTKUQiEr0ccQmmBvFNihIE", "Sonidos/sonidoRisaFrederic.wav")
    # Sonido Araña
    obtencionSonido("https://drive.google.com/uc?export=download&id=1QN5RkB50aC3bT0FCtX7Avm9V9A7YAmnx", "Sonidos/sonidoAraña.wav")
    # Sonido Ataque Araña
    obtencionSonido("https://drive.google.com/uc?export=download&id=17EF60ccCHjwI3DM6u_pwRJkLcQIVIJ_-", "Sonidos/sonidoAtaqueAraña.wav")
    # Sonido Dolor Frederic
    obtencionSonido("https://drive.google.com/uc?export=download&id=1UDv-Ej9YEcJj5RL5xu8Lr-7etzMLeMYO", "Sonidos/sonidoDolorHombre.wav")
    # Sonido Splash Agua
    obtencionSonido("https://drive.google.com/uc?export=download&id=1iCdazJgWQbV9WbIJBQRh1W1iKu0awZGM", "Sonidos/sonidoSplashAgua.wav")
    # Sonido Pasos Jefe
    obtencionSonido("https://drive.google.com/uc?export=download&id=1fIPBCkwgLXlnCtZjN_GIbneCoBNqS-9S", "Sonidos/sonidoPasosJefe.wav")
    # Sonido Ayuda Hombre
    obtencionSonido("https://drive.google.com/uc?export=download&id=1C3YR7FbwfBc265UGGP8AzyUOKatT-w0z", "Sonidos/sonidoAyudaM.wav")
    # Sonido Toser Hombre
    obtencionSonido("https://drive.google.com/uc?export=download&id=1Mm3t6ZRgzGsSziIYu_nf8v-AsugahJ5-", "Sonidos/sonidoToserM.wav")
    # Sonido Atras Tuyo Jefe
    obtencionSonido("https://drive.google.com/uc?export=download&id=1lylPPfTl6t7XxXL-0XLbVHFUbLKRhjh8", "Sonidos/sonidoAtrasTuyo.wav")
    # Sonido Muerte Aplastado
    obtencionSonido("https://drive.google.com/uc?export=download&id=1cQH2ntsc77SQe8I7IDhVII3fe4-3NDk8", "Sonidos/sonidoAplastado.wav")
    # Sonido Grito Muerte
    obtencionSonido("https://drive.google.com/uc?export=download&id=16JmlFlfcNvIEz6xTUq-VwCbE1S2fXzF9", "Sonidos/sonidoGritoMuerte.wav")
    # Sonido Caida
    obtencionSonido("https://drive.google.com/uc?export=download&id=1dDBl2i7-AJHEtWPch3uX-fLfP-Vxza6c", "Sonidos/sonidoCaida.wav")
    # Sonido Beso
    obtencionSonido("https://drive.google.com/uc?export=download&id=10R98aIqGbhJDwwiONJlfNF9fbV3Lk54-", "Sonidos/sonidoBeso.wav")
    # Sonido Botella
    obtencionSonido("https://drive.google.com/uc?export=download&id=1E1DXfqBqavfY7EbqG9asIkiqMlV9wHtv", "Sonidos/sonidoBotella.wav")
    # Sonido Hechizo Healing
    obtencionSonido("https://drive.google.com/uc?export=download&id=1GM_1cvetD-fOPWnvd_LoFaHtWyzerHYv", "Sonidos/sonidoHealing.wav")
    # Sonido Hechizo Enchanter
    obtencionSonido("https://drive.google.com/uc?export=download&id=1hJ0nUl2mQC16cSjx4zDOZPC4jr20Q7mx", "Sonidos/sonidoEnchanter.wav")
    # Sonido Risa Maniatica
    obtencionSonido("https://drive.google.com/uc?export=download&id=1fh1Qj0sf_mRI_UD5YAo8G64zjQYIOPIh", "Sonidos/sonidoManiatico.wav")
    # Sonido Victoria
    obtencionSonido("https://drive.google.com/uc?export=download&id=1QiLKFEt_SwKntgQANazS-JAaz7zxGQ6R", "Sonidos/sonidoVictoria.wav")
    # Sonido Neutral
    obtencionSonido("https://drive.google.com/uc?export=download&id=1PzVPs0XryJ4xsn_LIcf8CL7pRIPTQwYE", "Sonidos/sonidoNeutral.wav")
    # Sonido Derrota
    obtencionSonido("https://drive.google.com/uc?export=download&id=1QgjZhdpbNgDssyxUx5UHjKpbrtn6GXFa", "Sonidos/sonidoDerrota.wav")

    return 0

def main():
    print("Cargando juego, Espere...")
    # Descarga de sonidos
    descargas()
    #Limpieza Consola
    os.system('cls')

    reproducirSonido("Sonidos/sonidoEmpezar.wav", 1, [0, 0, -1], [0, 0, -1], 1.5, 0, False)
    print("                         _____ _                     _   _                              ")
    print("                        | __  |_|___ ___ _ _ ___ ___|_|_| |___                          ")
    print("                        | __ -| | -_|   | | | -_|   | | . | . |                         ")
    print("                        |_____|_|___|_|_|\_/|___|_|_|_|___|___|                         ")
    print("                                                                                        ")
    print("                                     /| ________________                                ")
    print("                               O|===|* >________________>                               ")
    print("                               ____  \|                  ,                              ")
    print("                              /---.'.__             ____//                              ")
    print("                                   '--.\           /.---'                               ")
    print("                              _______  \\         //                                    ")
    print("                            /.------.\  \|      .'/  ______                             ")
    print("                           //  ___  \ \ ||/|\  //  _/_----.\__                          ")
    print("                          |/  /.-.\  \ \:|< >|// _/.'..\   '--'                         ")
    print("                             //   \'. | \'.|.'/ /_/ /  \\                               ")
    print("                            //     \ \_\/  | ~\-'.-'    \\                              ")
    print("                           //       '-._| :H: |'-.__     \\                             ")
    print("                          //           (/'==='\)'-._\     ||                            ")
    print("                          ||                        \\    \|                            ")
    print("                          ||                         \\    '                            ")
    print("                          |/                          \\                                ")
    print("                                                       ||                               ")
    print("                                                       ||                               ")
    print("                                                       \\                               ")
    print("                                  _______________|\     '                               ")
    print("                                 <_______________*|===|O                                ")
    print("                                                 |/                                     ")    
    print(" __    _____    _____ _____ _____ _____ _____    ____  _____    _____ _____ ____  _____ ")
    print("|  |  |  _  |  |_   _|  |  |     | __  |  _  |  |    \|   __|  |   __|   __|    \|  _  |")
    print("|  |__|     |    | | |  |  | | | | __ -|     |  |  |  |   __|  |__   |   __|  |  |     |")
    print("|_____|__|__|    |_| |_____|_|_|_|_____|__|__|  |____/|_____|  |_____|_____|____/|__|__|")
    print("                                                                                        ")
    print("                                  Hecho Por: Miguel Angel Nivia Y Daniel Vasquez Murillo")
    reproducirSonido("Sonidos/sonidoInicioMenu.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, True)
    #Limpieza Consola
    os.system('cls')

    tiene_pechera = False

    print("Dios - Frederic es un aventurero común y corriente que hace parte de un grupo de mercenarios, el cual despierta después de una exploración que salió mal, con un fuerte dolor de cabeza.")
    reproducirSonido("Sonidos/sonidoViento.wav", 1, [0, 1, 0], [0, 1, 0], 2, 0, False)
    avanzar()

    print("Frederic - Ahg que.. que paso? ¿Dónde estoy? No veo absolutamente nada, hay un olor a humo, estoy mojado y repleto de lodo.")
    reproducirSonido("Sonidos/sonidoGotasCueva.wav", 1, [1, 0, -1], [1, 0, -1], 1, 0, False)
    avanzar()

    contador = 0
    while contador < 2:
        
        print("¿Qué quieres hacer? \n1. Levantarse \n2. Mirar a tu alrededor")
        reproducirSonido("Sonidos/sonidoSeleccion.wav", 0.7, [0, 0, 0], [0, 0, 0], 2, 0, False)
        decision = input(":")
        if decision == "1":
            print("Frederic - ¿Qué es esto? ¿una herida? Mierda tengo una cortada infectada en el abdomen.")
            reproducirSonido("Sonidos/sonidoHeridaFrederic.wav", 1, [0, 0, 0], [0, 0, 0], 1, 2, False)
            avanzar()

            contador += 1
            print("¿Qué quieres hacer? \n1. Mirar a tu alrededor \n2. Mirar arriba")
            reproducirSonido("Sonidos/sonidoSeleccion.wav", 0.7, [0, 0, 0], [0, 0, 0], 2, 0, False)
            decision = input(":")
            while contador < 2:
                if decision == "1":
                    print("Frederic - Qué carajo no se ve nada alrededor, ¿Uh?… ¿Qué es eso? Algo brilla al fondo.")
                    reproducirSonido("Sonidos/sonidoDudaFrederic.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    avanzar()
                    
                    contador += 1
                elif decision == "2":
                    contador += 1

        elif decision == "2":
            print("Frederic - Qué carajo no se ve nada alrededor, ¿Uh?… ¿Qué es eso? Algo brilla al fondo.")
            reproducirSonido("Sonidos/sonidoDudaFrederic.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            avanzar()

            contador += 1
            print("¿Qué quieres hacer? \n1. Levantarse \n2. Mirar arriba")
            reproducirSonido("Sonidos/sonidoSeleccion.wav", 0.7, [0, 0, 0], [0, 0, 0], 2, 0, False)
            decision = input(":")
            while contador < 2:
                if decision == "1":
                    print("Frederic - ¿Qué es esto? ¿una herida? Mierda tengo una cortada infectada en el abdomen.")
                    reproducirSonido("Sonidos/sonidoHeridaFrederic.wav", 1, [0, 0, 0], [0, 0, 0], 1, 2, False)
                    avanzar()

                    contador += 1
                elif decision == "2":
                    contador += 1

    print("Frederic - Parece que estoy en una especie de cueva ¿Dónde demonios está mi equipo? Demonios esa espada me costó tanto como una semana en el burdel, me acercaré a esa luz, puede que encuentre algo de utilidad o ver algo.")
    reproducirSonido("Sonidos/sonidoGotasCueva.wav", 0.8, [-1, 0, -1], [-1, 0, -1], 1, 0, False)
    avanzar()

    print("Dios - Frederic confundido y sin saber dónde está, se acerca a la luz con cautela.")
    reproducirSonido("Sonidos/sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
    avanzar()

    print("Frederic - ¿Una fogata? ¿Qué hace una fogata aquí?")
    reproducirSonido("Sonidos/sonidoFogata.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
    avanzar()

    print("Frederic - No veo nada de relevancia excepto este palo seco.")
    reproducirSonido("Sonidos/sonidoFogata.wav", 1, [0, 0, -1], [0, 0, 0], 1, 0, False)
    avanzar()

    contador = 0
    while contador < 1:

        print("¿Qué quieres hacer? \n1. Hacer una antorcha \n2. Arrojar el palo al fuego")
        reproducirSonido("Sonidos/sonidoSeleccion.wav", 0.7, [0, 0, 0], [0, 0, 0], 2, 0, False)
        decision = input(":")

        if decision == "1":

            print("Frederic - Parece que este palo puede servir para hacer una antorcha.")
            reproducirSonido("Sonidos/sonidoCrafteo.wav", 1, [0, 0, 1], [0, 0, 0], 1, 0, False)
            avanzar()

            print("Dios - Frederic ahora con antorcha en mano, se dispuso a explorar las inmediaciones de la cueva.")
            reproducirSonido("Sonidos/sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
            avanzar()

            print("Frederic - Ojalá ahora encuentre esa maldita espada, Pero que carajo… toda la cueva está llena de arañazos y de un extraño líquido verde…")
            reproducirSonido("Sonidos/sonidoBaba.wav", 1, [0, 0, 0], [0, 0, 0], 1, 2, False)
            avanzar()

            reproducirSonido("Sonidos/sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
            print("Frederic - ¿Eso es un derrumbe? Veo algo de luz del otro lado…, ¿Que mierda paso aquí? Este camino está bloqueado...")
            reproducirSonido("Sonidos/sonidoRocasCayendo.wav", 0.8, [0, 1, 0], [0, 1, 0], 1, 0, False)
            avanzar()

            reproducirSonido("Sonidos/sonidoMujerGritando.wav", 0.8, [0, 0, -8], [0, 0, -8], 1, 0, False)
            reproducirSonido("Sonidos/sonidoMonstruoRugido.wav", 1.2, [0, 0, -10], [0, 0, 0], 1, 1, False)
            print("Frederic - ¿Qué fue eso? ¿Quién está ahí? ¿Sal y pelea cobarde?.")
            avanzar()

            contador = 0

            while contador < 1:
                print("¿Qué quieres hacer? \n1. Devolverse y avanzar por el camino de la fogata \n2. Despejar el camino bloqueado")
                reproducirSonido("Sonidos/sonidoSeleccion.wav", 0.7, [0, 0, 0], [0, 0, 0], 2, 0, False)
                decision = input(":")

                if decision == "1":
                    print("Frederic - No sé que fue eso, mejor me muevo rápido, me devuelvo a la fogata y me preparo para luchar.")
                    reproducirSonido("Sonidos/sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    avanzar()

                    print("Frederic - aquí está la pechera que compré en rebaja, qué porquería de pechera, casi me cuesta la vida, tiene una gran abertura en el abdomen, ¿Por qué estaba aquí? Las correas están intactas.")
                    reproducirSonido("Sonidos/sonidoBrillo.wav", 1, [0, 0, 1], [0, 0, 1], 1, 0, False)
                    avanzar()

                    print("Frederic - ¿Quién me la habrá quitado? Bueno eso no importa, me la pondré, de algo debe servir, esto es mejor que nada.")
                    reproducirSonido("Sonidos/sonidoArmadura.wav", 1, [0, 0, 0], [0, 0, 0], 1, 2, False)
                    avanzar()

                    contador += 1
                    tiene_pechera = True

                elif decision == "2":
                    reproducirSonido("Sonidos/sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
                    print("Frederic - Supongo que puedo intentar salir por donde entré.")
                    reproducirSonido("Sonidos/sonidoRocasCayendo.wav", 1.3, [0, 0, 0], [0, 0, 0], 0.8, 0, False)
                    avanzar()

                    print("Frederic - Carajo llevo varios minutos y estas piedras no se mueven ni un centímetro, maldita sea.")
                    reproducirSonido("Sonidos/sonidoDudaFrederic.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    avanzar()
                    
                    reproducirSonido("Sonidos/sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
                    print("Frederic - Esta cueva es más grande de lo que pensaba, está llena de estalagmitas y de estalactitas, sin quitar de lado esta asquerosa cantidad de murciélagos.")
                    reproducirSonido("Sonidos/sonidoMurcielagos.wav", 1.2, [0, 1, 5], [0, 1, 5], 1, 0, False)
                    avanzar()

                    reproducirSonido("Sonidos/sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
                    print("Frederic - Mejor me devuelvo hacia la fogata y me preparo para avanzar.")
                    reproducirSonido("Sonidos/sonidoFogata.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    avanzar()
                    
                    contador += 1
                    tiene_pechera = False

        elif decision == "2":

            reproducirSonido("Sonidos/sonidoFuegoIncremento.wav", 1.2, [0, -3, 0], [0, -3, 0], 1, 0, False)
            print("Frederic - Mierda casi me quemo, el fuego creció demasiado, por lo menos ahora puedo ver lo que está en la cercanía.")
            avanzar()

            reproducirSonido("Sonidos/sonidoFogata.wav", 1, [0, 0, -1], [0, 0, 0], 1, 0, False)
            print("Dios - Frederic sin nada de luz para explorar, se sienta a ver la fogata, mientras recuerdos llegan a su mente, luego de eso la fogata se extingue por completo.")
            reproducirSonido("Sonidos/sonidoBar.wav", 1, [0, 0, -10], [0, 0, -10], 1, 0, False)
            avanzar()

            print("Frederic - Ahora solo tengo dos opciones, avanzar por esta cueva o morir de viejo esperando a que pase algo interesante…")
            reproducirSonido("Sonidos/sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
            avanzar()

            contador += 1
            tiene_pechera = False

    print("Frederic - Llevo quince minutos caminando, ¿Dónde está la salida?, esta cueva es enorme, al menos veo el camino con este río fosforescente color verde vómito.")
    reproducirSonido("Sonidos/sonidoRio.wav", 0.8, [0, -5, 0], [0, -5, 0], 1, 0, False)
    avanzar()

    reproducirSonido("Sonidos/sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
    print("Frederic - Qué suerte la mía, esta cueva será mi tumba y este río apesta a cadáver de grifo.")
    reproducirSonido("Sonidos/sonidoRio.wav", 0.8, [0, -5, 0], [0, -5, 0], 1, 0, False)
    avanzar()

    reproducirSonido("Sonidos/sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
    print("Frederic - ¿Qué es eso?… Bien!!!! mi espada, pensé que no te encontraría, ven aquí preciosa, te besaría, pero no quiero hacerme otra herida.")
    reproducirSonido("Sonidos/sonidoRecoger.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
    avanzar()

    print("Frederic - Aún manchada de verde tienes tanto filo como las palabras de verónica.")
    reproducirSonido("Sonidos/sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
    avanzar()

    print("Frederic - ¿Que!!!!!? Veronica, maldición, ¿Dónde está esa sexy clérigo de ojos morados? Mierda dónde están el Jefe y Axcel, Vinimos aquí buscando algo pero… ¿Que era?")
    reproducirSonido("Sonidos/sonidoDudaFrederic.wav", 1.5, [0, 0, 0], [0, 0, 0], 1, 0, False)
    avanzar()

    print("Frederic - Céntrate, ahora estoy solo, por lo menos ahora tengo algo para defenderme.")
    reproducirSonido("Sonidos/sonidoSuspiro.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
    avanzar()

    print("Dios - Frederic camino otros cinco minutos sin parar de hacerse la misma pregunta, ¿Que paso en la cueva?")
    reproducirSonido("Sonidos/sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
    avanzar()

    reproducirSonido("Sonidos/sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
    print("Frederic - ¿Ah? ¿Qué es eso? Una puerta de madera rota madera, es gigante, parece que llegue al final de este maldito camino, pensé que no saldría de aquí, espero que allí esté Veronica esperándome con algun hechizo para recuperarme de esta herida, no puedo esperar para poner mis manos sobre esas curvas…")
    reproducirSonido("Sonidos/sonidoRisaFrederic.wav", 0.8, [0, 0, 0], [0, 0, 0], 1, 2.5, False)
    avanzar()

    print("Frederic - Pero que carajo, ¿Una araña? esta cosa es tan grande como un lobo blanco.")
    reproducirSonido("Sonidos/sonidoAraña.wav", 0.7, [0, 0, 0], [0, 0, 0], 1, 0, False)
    avanzar()

    if tiene_pechera:
        reproducirSonido("Sonidos/sonidoAraña.wav", 0.7, [0, 0, 0], [0, 0, 0], 1, 0, False)
        print("Frederic - Uh… ¿La pechera? Fue directo al hombro.")
        reproducirSonido("Sonidos/sonidoRio.wav", 0.8, [0, -5, 0], [0, -5, 0], 2, 0, False)
        avanzar()

        print("Frederic - Buen ataque idiota, no falles el próximo, pero espera tu turno, ahora me toca a mí.")
        avanzar()
    else:
        reproducirSonido("Sonidos/sonidoDolorHombre.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
        print("Frederic - Ahhh!!! maldición, me diste en el hombro izquierdo ¿eso es ácido?, idiota eso va a dejar cicatriz, ven aquí estúpida arañita, vamos a jugar.")
        reproducirSonido("Sonidos/sonidoSuspiro.wav", 1, [0, 0, 0], [0, 0, 0], 1, 2, False)
        avanzar()

    contador = 0
    while contador < 1:
        print("¿Qué quieres hacer? \n1. Atacar \n2. Bloquear y contraatacar \n3. Engañar a la araña")
        reproducirSonido("Sonidos/sonidoSeleccion.wav", 0.7, [0, 0, 0], [0, 0, 0], 2, 0, False)
        decision = input(":")

        if decision == "1":
            contador += 1
            reproducirSonido("Sonidos/sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            print("Frederic - Toma esto idiota ¿Te gustó? ¿Quieres una segunda cita?, Ahg!!!! quédate quieta de una vez")
            reproducirSonido("Sonidos/sonidoAtaqueAraña.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)
            avanzar()

        elif decision == "2":
            contador += 1
            reproducirSonido("Sonidos/sonidoAraña.wav", 0.8, [0, 0, 0], [0, 0, 0], 1, 0, False)
            print("Frederic - ¿Crees que ese ataque podría hacerme algo? No en esta vida, Ahg!!! Eso estuvo cerca, déjame mostrarte cómo se hace.")
            reproducirSonido("Sonidos/sonidoAtaqueAraña.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)
            avanzar()

        elif decision == "3":
            contador += 1
            reproducirSonido("Sonidos/sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            print("Frederic - Ven aquí, sígueme.")
            reproducirSonido("Sonidos/sonidoAraña.wav", 0.8, [0, 0, 0], [0, 0, 0], 2, 0, False)
            avanzar()

            reproducirSonido("Sonidos/sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            print("Dios - Frederic para en seco justo después de dar vuelta en una esquina, esperando a que la araña llegara, velozmente utilizó su espada logrando cortarle dos patas lo que la desestabiliza.")
            reproducirSonido("Sonidos/sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)
            avanzar()

            print("Frederic - que se siente eso idiota, vamos ¿Qué haces ahí descansando? ¿No tenías ganas de darme un buen mordisco?")
            reproducirSonido("Sonidos/sonidoRisaFrederic.wav", 0.9, [0, 0, 0], [0, 0, 0], 1, 0, False) 
            avanzar()
           
            reproducirSonido("Sonidos/sonidoAraña.wav", 0.8, [0, 0, 0], [0, 0, 0], 2, 0, False)
            print("Frederic - Bueno uno, dos, tres!!!! Toma!!!!!")
            reproducirSonido("Sonidos/sonidoAtaqueAraña.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)
            avanzar()

            reproducirSonido("Sonidos/sonidoRio.wav", 0.8, [0, -5, 0], [0, -5, 0], 2, 0, False)
            print("Dios - Frederic empujó a la araña con una embestida lo que la hizo retroceder y caer en el río verde.")
            reproducirSonido("Sonidos/sonidoSplashAgua.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)
            avanzar()

    reproducirSonido("Sonidos/sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)
    print("Frederic - Puff, espero no encontrarme con más de una al mismo tiempo… Ahora debo centrarme en avanzar y encontrar a los demás.")
    reproducirSonido("Sonidos/sonidoSuspiro.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
    avanzar()

    reproducirSonido("Sonidos/sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
    print("Frederic - ¿Nogh ahora qué? ¿Tres caminos? ¿Esto es un laberinto o es una cueva? A este paso tendré que pensar en quedarme aquí y vender araña asada en un palo.")
    avanzar()

    print("Dios - Frederic vacilante pensó cuál camino tomar.")
    avanzar()

    if not tiene_pechera:
        reproducirSonido("Sonidos/sonidoRocasCayendo.wav", 0.8, [0, 1, 0], [0, 1, 0], 1, 0, False)
        print("Frederic - Por el segundo camino veo cráneos, demasiadas telarañas y sangre verde por todos lados, definitivamente no voy a ir ahí a morir.")
        reproducirSonido("Sonidos/sonidoMurcielagos.wav", 1.2, [-1, 1, 3], [-1, 1, 3], 1, 0, False)
        avanzar()

    else:
        print("Frederic - Ahg hay que descartar… bueno, no voy a entrar al primer camino, está demasiado oscuro y algo me dice que alguna cosa me esperaría del otro lado.")
        reproducirSonido("Sonidos/sonidoViento.wav", 1, [0, 1, 0], [0, 1, 0], 1, 0, False)
        avanzar()
    
    contador = 0
    while contador < 1:
        if not tiene_pechera:
            print("¿Qué quieres hacer? \n1. Primer camino(Se ve muy oscuro, pero hay un luz al final) \n3. Tercer camino(Parece el mas seguro, esta muy limpio)")
            reproducirSonido("Sonidos/sonidoSeleccion.wav", 0.7, [0, 0, 0], [0, 0, 0], 2, 0, False)
            decision = input(":")

        else: 
            print("¿Qué quieres hacer? \n2. Segundo camino(Tiene manchas de sangre y huesos, pero tambien tiene un aroma familiar) \n3. Tercer camino(Parece el mas seguro, esta muy limpio)")
            reproducirSonido("Sonidos/sonidoSeleccion.wav", 0.7, [0, 0, 0], [0, 0, 0], 2, 0, False)
            decision = input(":")

        print("Frederic - Bueno en marcha, no saldré si no me muevo.")
        reproducirSonido("Sonidos/sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
        avanzar()

        print("Dios - Frederic avanza por la cueva hasta que…")
        reproducirSonido("Sonidos/sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
        avanzar()

        if decision == "1" and not tiene_pechera:
            contador += 1

            reproducirSonido("Sonidos/sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
            print("Frederic - ¿Qué es eso? Que bien, hay luz al final del túnel, estoy cerca de una salida, pero antes de eso, dónde están mis compañeros, pensándolo bien…")
            reproducirSonido("Sonidos/sonidoBar.wav", 1, [0, 0, -10], [0, 0, -10], 1, 0, False)
            avanzar()

            contador = 0
            while contador < 1:
                print("¿Qué quieres hacer? \n1. Enfocarse en el pensamiento \n2. Ignorar este pensamiento y seguir avanzando")
                reproducirSonido("Sonidos/sonidoSeleccion.wav", 0.7, [0, 0, 0], [0, 0, 0], 2, 0, False)
                decision = input(":")

                if decision == "1":
                    contador += 1

                    reproducirSonido("Sonidos/sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)
                    reproducirSonido("Sonidos/sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)
                    print("Frederic - Mierda…, ya recorde, vinimos buscando una estupida mazmorra para encontrar un huevo de araña matriarca, nos pagarian una buena cantidad en el mercado negro, demonios chicos, Veronica…, Chef… Axel… Dónde están? Creo que peleamos con algo y eso nos separó… ¿Qué era esa cosa?")
                    reproducirSonido("Sonidos/sonidoSplashAgua.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)
                    avanzar()

                elif decision == "2":
                    contador += 1

                    print("Frederic - Nada, no recuerdo que paso, no tiene sentido tener pensamientos intrusivos ahora, tengo que seguir avanzando.")
                    reproducirSonido("Sonidos/sonidoViento.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    avanzar()

            print("Dios - Frederic continúa avanzando hasta que ve a lo lejos una sala de la cueva muy diferente a lo que ya ha visto antes.")
            reproducirSonido("Sonidos/sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
            avanzar()

            print("Frederic - Que maldito  asco, ¿Que pise? ¿Qué es eso?, son cientos de huevos y telarañas… parece la casa de otra asquerosa araña… ENORME!!!, mierda, mierda, puta madre, ya se donde estoy…")
            reproducirSonido("Sonidos/sonidoBaba.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
            avanzar()

            print("Frederic - El nido de la matriarca!!!")
            reproducirSonido("Sonidos/sonidoPasosJefe.wav", 0.8, [0, 0, -5], [0, 0, -5], 1, 0, False)
            avanzar()

            print("Dios - Frédéric al escuchar las fuertes pisadas aproximándose se esconde detrás de unos huevos.")
            reproducirSonido("Sonidos/sonidoBaba.wav", 1, [0, -1, 0], [0, -1, 0], 1.5, 0, False)
            avanzar()

            reproducirSonido("Sonidos/sonidoMonstruoRugido.wav", 1.2, [0, 0, -5], [0, 0, -5], 1, 0, False)
            print("Frederic - Ahora que, piensa, piensa, que se supone que haga? Yo solo no soy capaz de matar a esa cosa, debo escapar de aquí de inmediato, pero como?, parece que esa mamá araña quiere comida para sus horribles bebés, carajo.")
            avanzar()

            print("Frederic - Me tengo que ir rápido, este asqueroso huevo podrido huele horrible… oh… mierda")
            avanzar()

            print("Dios - Frederic sin decir una palabra, observa como entra a la habitación una enorme, horripilante, tenebrosa araña matriarca negra con manchas verdes y con unos grandes colmillos altamente venenosos.")
            avanzar()

            reproducirSonido("Sonidos/sonidoPasosJefe.wav", 1, [0, 0, -3], [0, 0, -3], 1, 0, False)
            print("Frederic - Qué demonios come esa araña en una cueva como esta para estar así, si me enfrento a esa cosa estaré muerto. Fue ella la que causó todo este maldito infierno, fuimos emboscados y nos atrapó, supongo que fui el único que no se llevó por alguna razón, la bastarda me dejo para morir o simplemente no quiso comerme, maldita, todos deben estar aquí.")
            reproducirSonido("Sonidos/sonidoMonstruoRugido.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            avanzar()

            print("Frederic - Demonios… siento algo en la espalda… Esto picha, es un bigote, color blanco, pegado a un enano calvo con cara de enojado, mmm… me parece familiar, OH JEFE! Chef!, esperame ya te voy a sacar de ahí.")
            reproducirSonido("Sonidos/sonidoAyudaM.wav", 0.8, [1, 0, 0], [1, 0, 0], 1, 0, False)
            avanzar()

            print("Dios - Fue entonces que Frederic se dio cuenta que además de haber cientos de huevos a su alrededor, también había docenas de criaturas de diferentes especies atrapadas en capullos de telaraña esperando ser alimento para las crías de arañas.")
            reproducirSonido("Sonidos/sonidoBaba.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
            avanzar()

            print("Chef - Qu…Qué es esto? ¿Dónde estoy? Frede…ric? Dónde estamos, informarme de la situación actual, donde están los demás?")
            reproducirSonido("Sonidos/sonidoToserM.wav", 0.7, [0, 0, 1], [0, 0, 1], 2, 0, False)
            avanzar()

            print("Frederic - Jefecito pensé que lo perdería, los demás están atrapados pero eso no importa, primero voy a sacarte de este capullo, solo deja que te quite esto de encima.")
            reproducirSonido("Sonidos/sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            avanzar()           

            reproducirSonido("Sonidos/sonidoAtrasTuyo.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            print("Chef - Gracias Frede…")
            reproducirSonido("Sonidos/sonidoAplastado.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            avanzar()

            print("Dios - Fue en ese entonces que Frederic bañado en la sangre de su amigo se da cuenta que la araña los había escuchado e inmediatamente mató a Chef para darle sus entrañas a sus crías prontas a nacer.")
            reproducirSonido("Sonidos/sonidoDudaFrederic.wav", 0.7, [0, 0, 0], [0, 0, 0], 1, 3, False)
            avanzar()

            print("Frederic - JEFEEEEE!!! NOOOOO!!!, MIERDA!; MIERDA!, Maldita puta araña,quieres comer, ven aquí idiota!!!, esa es…, a quien está apunto de comerse, no, no, NOOOO ESPERA!!!")
            reproducirSonido("Sonidos/sonidoGritoMuerte.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            avanzar()

            print("Dios - En ese momento Frederic visualizo como entre su boca tiene a Veronica a punto de ser masticada por el monstruo.")
            reproducirSonido("Sonidos/sonidoMonstruoRugido.wav", 1, [0, 0, 0], [0, 0, 0], 1.75, 0, False)
            avanzar()

            print("Frederic - NOOOO MALDITA ARAÑAS, PELEA COBARDE, SUELA A VERONICA AHHHHH")
            reproducirSonido("Sonidos/sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 1, 2, False)
            avanzar()
        
            contador = 0
            while contador < 1:
                print("¿Qué quieres hacer? \n1. Atacar a las patas. \n2. Atacar a la mandibula")
                reproducirSonido("Sonidos/sonidoSeleccion.wav", 0.7, [0, 0, 0], [0, 0, 0], 2, 0, False)
                decision = input(":")

                if decision == "1":
                    contador += 1

                    reproducirSonido("Sonidos/sonidoAtaqueAraña.wav", 1, [0, 1, 0], [0, 1, 0], 1, 0, False)
                    print("Dios - Después de un golpe certero, hace que la araña se descuide y choque con una roca que le cae en la cabeza, el monstruo grita del dolor cayendo al suelo momentáneamente.")
                    reproducirSonido("Sonidos/sonidoMonstruoRugido.wav", 1, [0, 1, 0], [0, 1, 0], 2, 0, False)
                    avanzar()

                    print("Frederic - voy por ti hermosura, espero que después de esta salvada épica me des por fin una cita.")
                    reproducirSonido("Sonidos/sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    avanzar()

                    print("Dios - Frederic inmediatamente al inmovilizar a la araña matriarca abre su mandíbula y entra ligeramente. ")
                    reproducirSonido("Sonidos/sonidoBaba.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)
                    avanzar()

                    print("Frederic - Ya casi te saco, ah!!! vamos.")
                    avanzar()
            
                    print("Dios - Sin embargo en ese momento la araña matriarca despierta y de un solo acto reflejo…")
                    reproducirSonido("Sonidos/sonidoHeridaFrederic.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    avanzar()
                
                elif decision == "2":
                    contador += 1

                    print("Frederic - Es todo o nada, voy a lanzar la espada, ten cuidado Veronica, Sueltala!!!")
                    reproducirSonido("Sonidos/sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    avanzar()

                    reproducirSonido("Sonidos/sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    print("Dios - Derrepente Frederic logra herir a la araña en su mandíbula, la araña enojada empezó a acercarse a Frederic ahora sin un arma en sus manos…")
                    reproducirSonido("Sonidos/sonidoAtaqueAraña.wav", 1, [0, 1, 0], [0, 1, 0], 1, 0, False)
                    avanzar()

                    print("Frederic - Quieres un poco mas idiota? ven, acercate viejo. ")
                    avanzar()

                    print("Dios - Aunque se encontraba motivado por el auge de la batalla, Frederic recordó sus anteriores palabras, “Yo solo no soy capaz de matar a esa cosa”, palabras que lo condenaron, pues al ver a los ojos a esa araña se dio cuenta de que no podía ganar.")
                    avanzar()
            
            print("Frederic - Con un demonio, lo que faltaba…")
            reproducirSonido("Sonidos/sonidoAplastado.wav", 1, [0, 0, 0], [0, 0, 0], 1, 3, False)
            avanzar()

            reproducirSonido("Sonidos/sonidoAraña.wav", 0.8, [0, 0, 0], [0, 0, 0], 2, 0, False)
            print("Dios - Completamente machacado, lamentablemente Frederic y Verónica son comidos por la araña matriarcado, esparciendo sangre y tripas por toda la sala para que sus hijos se alimenten. ")
            reproducirSonido("Sonidos/sonidoDerrota.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            avanzar()

            print("Final Malo(#1)")
        
        elif decision == "2" and tiene_pechera:
            contador += 1

            print("Frederic - Mmm, esto parece un precipicio, está demasiado alto, no veo ninguna otra salida por alguna dirección, solo hacia abajo.")
            reproducirSonido("Sonidos/sonidoSuspiro.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            avanzar()

            contador = 0
            while contador < 1:
                print("¿Qué quieres hacer? \n1. Regresar. \n2. Saltar \n:")
                reproducirSonido("Sonidos/sonidoSeleccion.wav", 0.7, [0, 0, 0], [0, 0, 0], 2, 0, False)
                decision = input(":")

                if decision == "1":
                    contador += 1

                    reproducirSonido("Sonidos/sonidoRocasCayendo.wav", 0.8, [0, 1, 0], [0, 1, 0], 1, 0, False)
                    print("Frederic - Mejor me devuelvo no hay salida por este lado, tal vez por otro camino, yo pueda, AH! otra araña!!!.")
                    reproducirSonido("Sonidos/sonidoAraña.wav", 0.8, [0, 0, -1], [0, 0, -1], 2, 0, False)
                    avanzar()

                    print("Dios - Inmediatamente Frederic fue atacado por una araña que lo vio entrar al lugar, logrando empujarlo hacia el precipicio, donde ambos cayeron varios metros.")
                    reproducirSonido("Sonidos/sonidoGritoMuerte.wav", 0.8, [0, 0, 1], [0, 0, 1], 1, 0, False)
                    avanzar()

                    print("Frederic - Ahhhh, ¿Que hago?, ahora estoy cayendo, Carajo muerete ya. ")
                    reproducirSonido("Sonidos/sonidoAtaqueAraña.wav", 1, [0, 1, 0], [0, 1, 0], 2, 0, False)
                    avanzar()

                    print("Dios - Frederic rápidamente usa el cuerpo de la araña muerta para usarla como cuerpo de soporte para aguantar un poco la caída y que él no sufra lesiones graves.")
                    reproducirSonido("Sonidos/sonidoCaida.wav", 1.2, [0, 0, 0], [0, 0, 0], 1, 3, False)
                    avanzar()
                
                elif decision == "2":
                    contador += 1

                    print("Frederic - Supongo que solo queda ir hacia abajo y rogar para no morir.")
                    avanzar()
                    
                    reproducirSonido("Sonidos/sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    print("Dios - Fue en ese entonces que Frederic, cae un par de metros hasta que choca con varias telarañas rompiendolas unas tras otras pero logrando reducir su velocidad lo suficiente hasta caer al fondo sin daños graves.")
                    reproducirSonido("Sonidos/sonidoRocasCayendo.wav", 1.2, [0, 0, 0], [0, 0, 0], 2, 0, False)
                    avanzar()
        
            print("Frederic - Ahg, Mierda pense que no la contaba, estoy en una pieza aunque siento que me he roto algo, como sea, ¿dónde estoy?, un momento… ")
            reproducirSonido("Sonidos/sonidoHeridaFrederic.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            avanzar()

            print("Frederic - Huevos… telarañas… demonios, esto es… un nido de arañas, entonces debe haber una matriarca cerca, debe ser la misma que causó todo este problema, ")
            reproducirSonido("Sonidos/sonidoBaba.wav", 1, [0, 0, 0], [0, 0, 0], 1, 2, False)
            avanzar()

            print("Frederic - Parece que cuando entramos fuimos emboscados y nos atrapó, sin embargo me debió dejar atrás por estar en ese líquido asqueroso y cubierto de lodo, todos deben estar aquí, espero que estén vivos.")
            avanzar()

            print("Dios - Rápidamente Frederic busco entre los cuerpos enredados para encontrar a sus amigos")
            reproducirSonido("Sonidos/sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            avanzar()

            print("Frederic - Esa es?…VERONICA!, Esperame, ya te saco.")
            reproducirSonido("Sonidos/sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            avanzar()

            print("Veronica - … Freder…ic? ¿Eres tu?")
            reproducirSonido("Sonidos/sonidoBaba.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)
            avanzar()

            print("Frederic - Si, me alegra que estés con vida, estás un poco herida según veo, pero así solo te ves más sexy. ")
            reproducirSonido("Sonidos/sonidoBeso.wav", 1, [0, 0, 0], [0, 0, 0], 1, 3, False)
            avanzar()

            print("Veronica - Quítate!!!, ni en esta situación puedes estar serio?, como sea, no tengo heridas graves, ¿vez mi mochila por algún lado?")
            reproducirSonido("Sonidos/sonidoCaida.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            avanzar()

            print("Frederic - Si, está al lado de dos hombres bestia que no lo lograron, qué pasa con ella?")
            avanzar()

            print("Veronica - Necesita que la traigas, ahi tengo una botella de maná, necesito recuperar energía para usar algún hechizo de curación.")
            avanzar()

            print("Dios - Frederic camino hasta la mochila con cuidado de no despertar ninguna cría y llevarle la poción a Veronica.")
            reproducirSonido("Sonidos/sonidoRecoger.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
            avanzar()

            print("Frederic - Toma, bébetela toda, no dejes ni una gota, así crecerás grande y fuerte.")
            reproducirSonido("Sonidos/sonidoRisaFrederic.wav", 0.9, [0, 0, 0], [0, 0, 0], 1.5, 0, False) 
            avanzar()

            print("Veronica - Callate.")
            avanzar() 

            reproducirSonido("Sonidos/sonidoBotella.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            print("Veronica - Aún estoy herida pero creo tener la suficiente energía para hacer algunos hechizos.")
            avanzar()

            print("Dios - Inmediatamente Verónica cura a Frederic y a ella misma.")
            reproducirSonido("Sonidos/sonidoHealing.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            avanzar()

            print("Frederic - Excelente, Ahora me siento mejor, gracias preciosa, busquemos a los otros y larguémonos de aquí.")
            avanzar()

            reproducirSonido("Sonidos/sonidoPasosJefe.wav", 1, [0, 0, -3], [0, 0, -3], 1, 0, False)
            print("Veronica - Esa araña va a ser un problema.")
            avanzar()

            print("Dios - Fue en ese preciso momento que vieron a la distancia en lugares opuestos a Axel y Chef, uno entre varios huevos de araña herido y el otro atrapado en un capullo de telaraña, sin embargo, justamente en ese momento llega la araña matriarca.")
            reproducirSonido("Sonidos/sonidoMonstruoRugido.wav", 1.2, [0, 0, -10], [0, 0, 0], 1.5, 1, False)
            avanzar()

            print("Veronica - Debemos salvar a ambos, pero ahora solo podemos sacar a uno… que… que hacemos Frederic?")
            reproducirSonido("Sonidos/sonidoPasosJefe.wav", 1, [0, 0, -2], [0, 0, -2], 1.5, 0, False)
            avanzar()

            print("Dios - Frederic estaba en una situación terrible donde solo tenían suficiente tiempo para sacar a uno momentáneamente.")
            avanzar()

            print("Frederic - Que hago? Chef es nuestro tranque, cocinero, jefe y maestro, puede ser de gran ayuda pero no sé si necesitamos fuerza bruta o las extrañas habilidades de Axel, al ser un asesino especializado en sigilo, puede enfocarse en ataques vitales… ¿Qué carajo hago? ")
            reproducirSonido("Sonidos/sonidoDudaFrederic.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            avanzar()

            contador = 0
            while contador < 1:
                print("¿Qué quieres hacer? \n1. Salvar a Chef. \n2. Salvar a Axel")
                reproducirSonido("Sonidos/sonidoSeleccion.wav", 0.7, [0, 0, 0], [0, 0, 0], 2, 0, False)
                decision = input(":")

                if decision == "1":
                    contador += 1

                    print("Frederic - Rapido Verónica, ve por Chef, nos será de más utilidad ahora, curalo y prepárense para luchar, yo lo distraigo por ahora.")
                    reproducirSonido("Sonidos/sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    avanzar()

                    print("Veronica - Entendido")
                    avanzar()

                    print("Frederic - Eh!!! Asquerosa araña ves esto¿Te gustó?.")
                    reproducirSonido("Sonidos/sonidoMonstruoRugido.wav", 1.5, [0, 0, 0], [0, 0, 0], 1.5, 0, False)
                    avanzar()

                    print("Dios - En ese momento, Frederic ya recuperado y con su fuerza al máximo comienza el ataque enfocándose en sus patas, corriendo por todos lados y dándole el mayor tiempo posible a Verónica.")
                    reproducirSonido("Sonidos/sonidoAtaqueAraña.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    avanzar()

                    print("Chef - Ho…Hola? Veronica, vaya <sonidos de gritos>, que agradable sorpresa, puedo ver la situación, vamos hay que acabar con esa araña matriarca, está demasiado agresiva por la temporada de apareamiento. ")
                    reproducirSonido("Sonidos/sonidoToserM.wav", 0.7, [0, 0, 1], [0, 0, 1], 2, 0, False)
                    avanzar()

                    print("Frederic - jajajaja Chef, te veo bien anciano, mejor ven y dame una mano antes de que lo mate yo ah!!!.")
                    reproducirSonido("Sonidos/sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    avanzar()

                    print("Chef - Silencio Frederic, ahora te enseño cómo acabar con un monstruo de esa calidad, rápido, Veronica quédate atrás de Frederic, Frederic ve por atrás.")
                    reproducirSonido("Sonidos/sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    avanzar()

                    print("Dios - Chef lider del grupo, ya recuperado utiliza un hechizo de encantamiento para atraer la atención de la araña matriarca y absorber daño para desencadenarlo en un fuerte impacto en su punto débil el abdomen mientras los demás la atacan por detrás sin preocuparse en ser objetivo de daño.")
                    reproducirSonido("Sonidos/sonidoEnchanter.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    reproducirSonido("Sonidos/sonidoHealing.wav", 1, [0, 0, 0], [0, 0, 0], 1, 1, False)
                    reproducirSonido("Sonidos/sonidoAtaqueAraña.wav", 1, [0, 0, 0], [0, 0, 0], 1, 2, False)
                    avanzar()

                    print("Frederic - Vamos Veronica prendele fuego, haz que brille. ")
                    reproducirSonido("Sonidos/sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    avanzar()

                    print("Veronica - Entendido ")
                    avanzar()
            
                elif decision == "2":
                    contador += 1

                    print("Frederic - Rapido Verónica, ve por Axel, nos será de más utilidad tener el mayor daño posible, curalo y prepárense para luchar, yo lo distraigo por ahora.")
                    avanzar()

                    print("Veronica - Entendido")
                    reproducirSonido("Sonidos/sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    avanzar()

                    reproducirSonido("Sonidos/sonidoPasosJefe.wav", 1, [0, 0, -2], [0, 0, -2], 1.5, 0, False)
                    print("Frederic - Eh!!! Asquerosa araña ves esto ¿Te gustó? ")
                    reproducirSonido("Sonidos/sonidoMonstruoRugido.wav", 1.5, [0, 0, 0], [0, 0, 0], 1.5, 0, False)
                    avanzar()

                    print("Dios - En ese momento, Frederic ya recuperado y con su fuerza al máximo comienza el ataque enfocándose en sus patas, corriendo por todos lados y dándole el mayor tiempo posible a Verónica.")
                    reproducirSonido("Sonidos/sonidoAtaqueAraña.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    avanzar()

                    print("Axel - Ughhh!!!, maldita sea que asco, puaj, vaya, Veronica eres tu, gracias, ¿Como te lograste liberar? ")
                    reproducirSonido("Sonidos/sonidoBaba.wav", 1, [0, 0, 0], [0, 0, 0], 1.5, 0, False)
                    avanzar()

                    print("Veronica - No, me salvo Frederic, pero ahora lo más importante es acabar con esa cosa.")
                    reproducirSonido("Sonidos/sonidoAtaqueAraña.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    avanzar()

                    print("Axel - jejejejeje ya veo, interesante, muy divertido, hagámoslo VAMOS!, OYEEE FREDERIC!")
                    reproducirSonido("Sonidos/sonidoManiatico.wav", 1, [0, 0, 0], [0, 0, 0], 1.25, 0, False)
                    avanzar()

                    print("Frederic - jajajaja hijo de perra, ya estás bien, muévete ya, dame una mano.")
                    reproducirSonido("Sonidos/sonidoRisaFrederic.wav", 0.9, [0, 0, 0], [0, 0, 0], 1.5, 0, False) 
                    avanzar()

                    print("Axel - Claro, no te voy a dejar toda esta diversión, jejejejeje, ahora escuchen, Veronica, apoyanos desde atrás, Frederic la distrae mientras yo la apuñalo, el jefe dijo que en el abdomen es débil, JEJEJE.")
                    avanzar()
                    
                    print("Dios - Axel psicomaniatico del grupo, enfocó su daño en el abdomen mientras Veronica golpeaba en la cabeza a la araña y engañándole con un encantamiento de espejismo, mientras Frederic golpea con gran fuerza desde el otro extremo, con la ayuda de un potenciador de Veronica.")
                    reproducirSonido("Sonidos/sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    reproducirSonido("Sonidos/sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1.5, 0, False)
                    avanzar()

                    print("Frederic - No te emociones demasiado Axel.")
                    reproducirSonido("Sonidos/sonidoHealing.wav", 1, [0, 0, 0], [0, 0, 0], 1, 1, False)
                    reproducirSonido("Sonidos/sonidoAtaqueAraña.wav", 1, [0, 0, 0], [0, 0, 0], 1, 2, False)
                    avanzar()

                    print("Axel - jejejeje!")
                    reproducirSonido("Sonidos/sonidoManiatico.wav", 1, [0, 0, 0], [0, 0, 0], 1.25, 0, False)
                    avanzar()

            print("Dios - Después de una gran lucha, logran salir con vida del encuentro, salvando de paso al otro compañero atrapado, tomando como recompensa un huevo de araña matriarcal y equipo de aventureros caídos, eliminando el resto de arañas para así lograr salir de la tumba de la seda, una de las mazmorras más engañosas por la que han pasado este grupo de mercenarios.")
            reproducirSonido("Sonidos/sonidoVictoria.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            avanzar()

            print("Final Bueno(#2)")
    
        elif decision == "3":
            contador += 1
        
            print("Frederic - Vaya, al parecer es un camino bastante seguro, me parece extraño que no vea rastro de monstruos o humanos.")
            reproducirSonido("Sonidos/sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
            avanzar()

            print("Frederic - ¿Dónde estarán los chicos? Carajo.")
            reproducirSonido("Sonidos/sonidoDudaFrederic.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            avanzar()

            print("Dios - Fue en ese entonces que a través de unos agujeros naturales logró ver al otro lado una gran sala muy diferente a las otras, llena de huevos y telaraña.")
            reproducirSonido("Sonidos/sonidoRocasCayendo.wav", 1.2, [0, 0, 0], [0, 0, 0], 1, 0, False)
            avanzar()

            print("Frederic - Pero que carajo, eso es un nido de araña matriarca, seguramente la madre de las arañas, Mejor sigo moviendome antes de que algo me vea…")
            reproducirSonido("Sonidos/sonidoPasosJefe.wav", 1, [0, 0, -3], [0, 0, -3], 1, 0, False)
            avanzar()

            print("Dios - Frederic justo antes de seguir avanzando observa como entra a la habitación una enorme, horripilante, tenebrosa araña matriarca negra con manchas verdes y con unos grandes colmillos altamente venenosos . ")
            reproducirSonido("Sonidos/sonidoMonstruoRugido.wav", 1.5, [0, 0, 0], [0, 0, 0], 1, 0, False)
            avanzar()

            print("Frederic - Parece que cuando entramos fuimos emboscados y nos atrapó, sin embargo me debió dejar atrás por estar en ese líquido asqueroso y cubierto de lodo, todos deben estar aquí, espero que estén vivos.")
            avanzar()

            print("Dios - Fue entonces que Frederic se dio cuenta que estaba atrapado Axel ahí, envuelto como capullo en telaraña, además de haber huevos a su alrededor, también había criaturas de diferentes especies atrapadas esperando ser alimento para las crías de arañas.")
            reproducirSonido("Sonidos/sonidoBaba.wav", 1, [0, 0, 0], [0, 0, 0], 1, 2, False)
            avanzar()

            print("Frederic - AXEL!, espera, si el esta ahi y no he visto ningún rastro de los demás, entonces ahí estarán los otros, MIERDA!")
            avanzar()

            print("Axel - Con que hasta allí estás… TE LOGRO VER FEDERIC SACAME HIJO DE PERRA…")
            reproducirSonido("Sonidos/sonidoToserM.wav", 0.7, [0, 0, 4], [0, 0, 4], 1, 0, False)
            avanzar()

            print("Frederic - AXEL!!! NO TE MUERAS; YA VOY POR USTEDES!!!")
            avanzar()

            reproducirSonido("Sonidos/sonidoToserM.wav", 0.7, [0, 0, 4], [0, 0, 4], 2, 0, False)
            print("Axel - jajajaja, lo siento hermano, pero eso no va a ser posible, no hay forma sencilla de atravesar los muros, ya lo intente… lo siento… pero debes irte, escapa co… co… con… vida.")
            reproducirSonido("Sonidos/sonidoGritoMuerte.wav", 1.5, [0, 0, 0], [0, 0, 0], 1, 0, False)
            avanzar()

            print("Frederic - AXEL!!! IDIOTA!!! AXEL!!! AXEEEEEL!!!")
            avanzar()

            reproducirSonido("Sonidos/sonidoPasosJefe.wav", 1, [0, 0, 3], [0, 0, 3], 1, 0, False)
            print("Dios - Fue entonces que la araña matriarca, saca entre varios montículos de cuerpos a Verónica para comérsela.")
            avanzar()

            print("Frederic - Veronica!!!, que hago, no tengo suficiente tiempo para volver y no creo ser capaz de abrir este agujero lo suficientemente para pasar, Mierda!.")
            reproducirSonido("Sonidos/sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            avanzar()
            
            contador = 0
            while contador < 1:
                print("¿Qué quieres hacer? \n1. Gritar. \n2. Rendirse \n:")
                reproducirSonido("Sonidos/sonidoSeleccion.wav", 0.7, [0, 0, 0], [0, 0, 0], 2, 0, False)
                decision = input(":")

                if decision == "1":
                    contador += 1

                    reproducirSonido("Sonidos/sonidoAraña.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    print("Dios - En ese momento Frederic grita logrando atraer a la araña matriarca, la cual de un grito mucho mayor al de él, hace que despierten todas sus crías las cuales salen corriendo hacia él.")
                    reproducirSonido("Sonidos/sonidoAraña.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    avanzar()
                    
                    print("Frederic - Mierda, son demasiadas, debo salir rápido o voy a morir, ATRÁS MALDITOS BICHOS!! AHHHHHHHH!!!!.")
                    reproducirSonido("Sonidos/sonidoAtaqueAraña.wav", 1, [0, 0, 0], [0, 0, 0], 1, 2, False)
                    avanzar()

                    print("Dios - Después de una gran pelea contra las crías de araña, Frederic logra salir vivo de la cueva.")
                    reproducirSonido("Sonidos/sonidoPasosHumano.wav", 0.8, [0, -1, 0], [0, -1, 0], 0.8, 0, False)
                    avanzar()

                    print("Frederic - Maldición, estoy vivo, gracias a Rumania, esos malditos me quitaron el brazo, tengo que curarme rápido… mierda mis amigos…... no los pude salvar, ya deben estar muertos, MIERDAAAAAAAA!!!!.")
                    avanzar()

                elif decision == "2":
                    print("Frederic - Carajo… tal vez si yo… solamente yo… fuera capaz de hacer algo lo haría, pero… no soy capaz, perdonenme <Sonido de Correr>.")
                    reproducirSonido("Sonidos/sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1.5, 0, False)
                    avanzar()
                    
                    print("Dios - Frederic ante la situación y el miedo que le recorría todo el cuerpo decidió abandonar a sus amigos a la suerte, llegando hasta esa luz que vio anteriormente que era la salida de la cueva.")
                    reproducirSonido("Sonidos/sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1.5, 0, False)
                    avanzar()

                    print("Frederic - yo….")
                    reproducirSonido("Sonidos/sonidoGritoMuerte.wav", 1.5, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    avanzar()
                    
                    contador += 1


            print("Dios - Después de salir con vida de la cueva, Frederic herido logra llegar hasta el pueblo más cercano para pedir ayuda, enterrando esta historia de su vida como un recordatorio del día que perdió a sus amigos, su brazo y su vida como aventurero.")
            avanzar()
            
            reproducirSonido("Sonidos/sonidoNeutral.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
    
    print("FIN")

# Empezar el juego
main()#

# Limpiar y cerrar openAL
oalQuit()
