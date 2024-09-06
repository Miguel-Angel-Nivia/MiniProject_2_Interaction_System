import os
import time
import textwrap
import threading
import msvcrt
from openal import *

def obtain_sounds():
    """Get sounds with relative path."""
    root = os.path.dirname(os.path.abspath(__file__))
    sounds_file = os.path.join(root, "Sounds")
    return {name: oalOpen(os.path.join(sounds_file, name)) for name in os.listdir(sounds_file)}

def play_sound_with_distance(sound, player_pos, sound_pos, initial_vol, max_distance, loop, stop_event):
    """Adjust sound volume based on distance between player and target."""
    sound.set_gain(initial_vol)
    sound.set_position(sound_pos)
    sound.set_looping(loop)
    sound.play()
    while not stop_event.is_set():
        # Calculate the distance between the listener (player) and the campfire
        distance = ((player_pos[0] - sound_pos[0]) ** 2 + (player_pos[1] - sound_pos[1]) ** 2 + (player_pos[2] - sound_pos[2]) ** 2) ** 0.5
        if distance <= 0.3:
            # Stop adjusting position and volume, but continue to play the sound at maximum volume
            sound.set_gain(initial_vol)
        else:
            # Calculate the new volume based on the distance
            if distance > initial_vol:
                volume = 0
            else:
                volume = initial_vol * (1 - (distance / max_distance))
            sound.set_gain(volume)
            # Update the listener's position based on the direction towards the sound
            oalGetListener().set_position(player_pos) 
            # Check if player has reached the campfire
            step = 0.1
            player_pos[0] += step if player_pos[0] < sound_pos[0] else -step
            player_pos[2] += step if player_pos[2] < sound_pos[2] else -step
            time.sleep(0.5)

def play_sound_threaded(sound, volume, speed, spatial_pos, loop):
    """Play sounds with modifiable characteristics."""
    sound.set_gain(volume)
    sound.set_pitch(speed)
    sound.set_position(tuple(spatial_pos))
    sound.set_looping(loop)
    sound.play()
    while loop and sound.get_state() == AL_PLAYING:
        time.sleep(0.1)

def play_sound(sounds, name, volume, speed, spatial_pos, time_to_wait, loop, sel, stop_event=None):
    """Play sounds concurrently using threads."""
    if name not in sounds:
        return None
    sound = sounds[name]
    if sel == "static":
        thread = threading.Thread(target=play_sound_threaded, args=(sound, volume, speed, spatial_pos, loop))
    elif sel == "move":
        thread = threading.Thread(target=play_sound_with_distance, args=(sound, [0, 0, 0], spatial_pos, volume, 6, loop, stop_event))
    else:
        raise ValueError("Invalid selection. Choose 'static' or 'move'.")
    
    thread.start()
    if time_to_wait:
        time.sleep(time_to_wait)
    return thread

def print_text(text, clean):
    """Display text in cmd with a width of 80."""
    for line in textwrap.wrap(text, width=80):
        print(line)
    print("\nPresione una tecla para continuar...\n")
    msvcrt.getch()

    if clean:
        os.system('cls' if os.name == 'nt' else 'clear')

def player_interaction(sounds, info, text, thread, sound, number):
    """Execute player selection for a decision/interaction."""
    if info == "selection":
        selection_thread = play_sound(sounds, "sonidoSeleccion.wav", 0.7, 2, [0, 0, 0], 0, False, "static")
        if selection_thread.is_alive(): sounds["sonidoSeleccion.wav"].stop() and selection_thread.join()
        decision = input(":")
        return int(decision)
    elif info == "continue":
        print_text(text, number)
        sounds[sound].stop()
        thread.join()
    return 0

def loading_screen():
    """Print the start menu."""
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
