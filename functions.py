from openal import *
import os, time, textwrap, threading

# Code Functionality
# By: Miguel Angel Nivia Y Daniel Vasquez

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


def playSoundEspecialThreads(sound, playerPos, soundPos, initialVol, maxDistance, loop, stopEvent):
    """
    Adjusts the sound volume based on the distance between the player and the target.
    
    Arguments:
        sound (str): Target sound.
        playerPos: The current position of the player (x, y, z).
        soundPos: The position of the sound (x, y, z).
        initial_volume: The initial volume of the sound.
        max_distance: The maximum distance at which the sound should be audible.
        stopEvent (threading.Event): Event to signal when to stop the sound.
    """
    sound.set_gain(initialVol)  # Set the initial volume
    sound.set_position(soundPos)  # Set the position of the sound
    sound.set_looping(True)  # Loop the sound indefinitely
    sound.play()  # Start playing the sound

    while not stopEvent.is_set():
        # Calculate the distance between the listener (player) and the campfire
        distance = ((playerPos[0] - soundPos[0]) ** 2 + (playerPos[1] - soundPos[1]) ** 2 + (playerPos[2] - soundPos[2]) ** 2) ** 0.5
        if distance <= 0.3:
            # Stop adjusting position and volume, but continue to play the sound at maximum volume
            sound.set_gain(initialVol)
        else:
            # Calculate the new volume based on the distance
            if distance > maxDistance:
                volume = 0
            else:
                volume = initialVol * (1 - (distance / maxDistance))
            # Adjust the volume
            sound.set_gain(volume)
            # Update the listener's position based on the direction towards the sound
            oalGetListener().set_position(playerPos) 
            # Check if player has reached the campfire
            step = 0.1
            playerPos[0] += step if playerPos[0] < soundPos[0] else -step
            playerPos[2] += step if playerPos[2] < soundPos[2] else -step
            time.sleep(0.5)
    # Stop the sound once the event is set
    sound.stop()

def playSoundThreads(sound, volume, speed, spatialPos, loop):
    """
    # Function to play Sounds, where you can modify various characteristics of it.

    Arguments:
        sound (str): Chosen sound.
        volume (float): Numerical value of sound volume where 1.0 is the standard.
        speed (float): Speed of sound reproduction.
        spatialPos (list(float)): List of integers of size 3 containing the "x", "y" and "z" positions of the sound spatially.
                                where x = 1 is right and -1 is left,
                                where y = 1 is up and -1 is down and
                                where z = 1 near (forward) and -1 far (back).
        loop (bool): Flag indicating whether the sound plays infinitely or not.
    """
    # Sound settings.
    sound.set_gain(volume)
    sound.set_pitch(speed)
    sound.set_position((spatialPos[0], spatialPos[1], spatialPos[2]))
    if loop:
        sound.set_looping(True)
    sound.play()
    # Keep the sound playing in loop
    while loop and sound.get_state() == AL_PLAYING:
        time.sleep(0.1)


def playSound(sounds, name, volume, speed, spatialPos, timeToWait, loop, sel, stopEvent=None):
    """
    Function to play Sounds concurrently using threads, where you can modify various characteristics of the sound.
    Arguments:
        The same ones that appear in "playSoundThreads" except this one:
        sounds (dic): Sound dictionary.
        name (str): Name of the sound file to play.
        timeToWait (float): Execution time of the sound.
    """
    if name not in sounds:
        print(f"El sonido '{name}' no se encontró.")
        return None
    
    # Load and play the sound file.
    sound = sounds[name]
    if sel == "static":
        # Setting up and playing sound in a separate threads
        thread = threading.Thread(target = playSoundThreads, args = (sound, volume, speed, spatialPos, loop))
        thread.start()
        if timeToWait != 0:
            time.sleep(timeToWait)
    elif sel == "move":
        # Create a thread to adjust the sound based on distance
        thread = threading.Thread(target = playSoundEspecialThreads, args = (sound, [0, 0, 0], spatialPos, volume, 6, loop, stopEvent))
        thread.start()

    return thread

def printText(text, clean):
    # Function to display text in cmd with a width of 70.
    line = textwrap.wrap(text, width = 80)
    for i in line:
        print(i)
    entrada = None
    while entrada != "":
        entrada = input("\nPresiona enter para continuar...\n")
    if clean == 1:
        os.system('cls')

    return 0

def playerInteraction(sounds, info, text, thread, sound, number):
    """
    Function to execute the player selection for a decision/Interaction.
    Arguments:
        sounds (dic): sound dictionary.
        info (str): Information on action to be taken.
        text (str): Text to print.
        thread (thread): Thread to be executed.
        sound (str): Name of the sound.
        number (int): Number to know if you want to clean the console or not.
    """
    if info == "selection":
        decision = None
        selectionThread = playSound(sounds, "sonidoSeleccion.wav", 0.7, 2, [0, 0, 0], 0, False, "static")
        if selectionThread.is_alive():
            try:
                decision = input(":")
            finally:
                sounds["sonidoSeleccion.wav"].stop() and selectionThread.join()
        return decision
    
    elif info == "continue":
        if thread.is_alive():
            try:
                printText(text, number)
            finally:
                sounds[sound].stop() and thread.join()
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
    print("\n                                Hecho Por: Miguel Angel Nivia Y Daniel Vasquez Murillo")
    return 0
