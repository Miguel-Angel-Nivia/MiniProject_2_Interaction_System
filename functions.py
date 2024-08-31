import os, time, textwrap
from openal import *

# Code Functionality
# By: Miguel Angel Nivia Y Daniel Vasquez

# List of Sounds routes.
# Sonido de inicio : Sounds/sonidoEmpezar.wav
# Sonido Musica Menu : Sounds/sonidoInicioMenu.wav
# Sonido de viento : Sounds/sonidoViento.wav
# Sonido de gotas de agua : Sounds/sonidoGotasCueva.wav
# Sonido Seleccion Usuario : Sounds/Soundseleccion.wav
# Sonido Herida Frederic : Sounds/sonidoHeridaFrederic.wav
# Sonido Duda Frederic : Sounds/sonidoDudaFrederic.wav
# Sonido Pasos Humano : Sounds/sonidoPasosHumano.wav
# Sonido Fogata : Sounds/sonidoFogata.wav
# Sonido Crafteo : Sounds/sonidoCrafteo.wav
# Sonido Baba : Sounds/sonidoBaba.wav
# Sonido Rocas Cayendo : Sounds/sonidoRocasCayendo.wav
# Sonido Grito Mujer : Sounds/sonidoMujerGritando.wav
# Sonido Rugido Monstruo : Sounds/sonidoMonstruoRugido.wav
# Sonido Correr Humano : Sounds/sonidoCorrerHumano.wav
# Sonido Brillo : Sounds/sonidoBrillo.wav
# Sonido Armadura : Sounds/sonidoArmadura.wav
# Sonido Murcielagos : Sounds/sonidoMurcielagos.wav
# Sonido Fuego Incrementa : Sounds/sonidoFuegoIncremento.wav
# Sonido Bar : Sounds/sonidoBar.wav
# Sonido Rio : Sounds/sonidoRio.wav
# Sonido Recoger : Sounds/sonidoRecoger.wav
# Sonido Espada : Sounds/sonidoEspada.wav
# Sonido Suspiro : Sounds/Soundsuspiro.wav
# Sonido Risa Frederic : Sounds/sonidoRisaFrederic.wav
# Sonido Araña : Sounds/sonidoAraña.wav
# Sonido Ataque Araña : Sounds/sonidoAtaqueAraña.wav
# Sonido Dolor Frederic : Sounds/sonidoDolorHombre.wav
# Sonido Splash Agua : Sounds/SoundsplashAgua.wav
# Sonido Pasos Jefe : Sounds/sonidoPasosJefe.wav
# Sonido Ayuda Hombre : Sounds/sonidoAyudaM.wav
# Sonido Toser Hombre : Sounds/sonidoToserM.wav
# Sonido Atras Tuyo Jefe : Sounds/sonidoAtrasTuyo.wav
# Sonido Muerte Aplastado : Sounds/sonidoAplastado.wav
# Sonido Grito Muerte : Sounds/sonidoGritoMuerte.wav
# Sonido Caida : Sounds/sonidoCaida.wav
# Sonido Beso : Sounds/sonidoBeso.wav
# Sonido Botella : Sounds/sonidoBotella.wav
# Sonido Hechizo Healing : Sounds/sonidoHealing.wav
# Sonido Hechizo Enchanter : Sounds/sonidoEnchanter.wav
# Sonido Risa Maniatica : Sounds/sonidoManiatico.wav
# Sonido Victoria : Sounds/sonidoVictoria.wav
# Sonido Neutral : Sounds/sonidoNeutral.wav
# Sonido Derrota : Sounds/sonidoDerrota.wav

def obtainingSound():
    """
    # Function to get sounds with relative path.
    """
    # Get the path of the directory where the current script is.
    root = os.path.dirname(os.path.abspath(__file__))

    # Build the path to the sounds file.
    soundsFile = os.path.join(root, "Sounds")
    sounds = {}
    for nombre in os.listdir(soundsFile):
        soundRoute = os.path.join(soundsFile, nombre)
        sound = oalOpen(soundRoute)
        sounds[nombre] = sound
    return sounds

def playSound(sounds, name, volume, spatialPos, spaceVel, speed, time, loop):
    """
    # Function to play Sounds, where you can modify various characteristics of it.

    Arguments:
        name (str): Name of the sound file to play.
        volume (float): Numerical value of sound volume where 1.0 is the standard.
        spatialPos (list(float)): List of integers of size 3 containing the "x", "y" and "z" positions of the sound spatially.
                                where x = 1 is right and -1 is left,
                                where y = 1 is up and -1 is down and
                                where z = 1 near (forward) and -1 far (back).
        spaceVel (list(float)): List of integers of size 3 containing the "x", "y", and "z" velocities of sound.
        velocidad (float): speed of sound reproduction.
        tiempo (float): execution time before sound is played.
        loop (bool): Flag indicating whether the sound plays infinitely or not.
    """
    if name not in sounds:
        print(f"El sonido '{name}' no se encontró.")
        return

    # Load and play the sound file.
    sound = sounds[name]
    # Sound settings.
    sound.set_gain(volume)
    sound.set_position((spatialPos[0], spatialPos[1], spatialPos[2]))
    sound.set_velocity((spaceVel[0], spaceVel[1], spaceVel[2]))
    sound.set_pitch(speed)
    if time != 0:
        time.sleep(time)
    if loop == True:
        sound.set_looping(True)
        # Keep the sound playing in loop until the user presses Enter
        sound.play()
        try:
            input("\n                         Presiona enter para continuar...                            \n\n")
        finally:
            sound.stop()
    else:
        sound.play()
        # Keep the sound playing.
        while sound.get_state() == AL_PLAYING:
            pass
    return 0

def printText(text, clean):
    # Function to display text in cmd with a width of 70.
    line = textwrap.wrap(text, width = 80)
    for i in line:
        print(i)
    input("\nPresiona enter para continuar...\n")
    if clean == 1:
        os.system('cls')
    return 0

def loadingScreen():
    # Function to print the start menu.
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
    return 0
