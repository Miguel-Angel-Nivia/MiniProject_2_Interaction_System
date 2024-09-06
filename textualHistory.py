from openal import *
import functions as func
import csv

def load_story_data(file_path):
    """Load story data from CSV file."""
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return {row['id']: row for row in reader}

def play_intro(sounds):
    start_thread = func.play_sound(sounds, "sonidoEmpezar.wav", 0.8, 1.5, [0, 0, -1], 3.5, False, "static")
    sounds["sonidoEmpezar.wav"].stop()
    start_thread.join()
    func.loading_screen()
    menu_thread = func.play_sound(sounds, "sonidoInicioMenu.wav", 0.8, 1, [0, 0, 0], 0, True, "static")
    input("\n                         Press enter to continue...                            \n\n")
    sounds["sonidoInicioMenu.wav"].stop()
    menu_thread.join()

def play_scene(sounds, scene_data):
    text = scene_data['text']
    if scene_data['type'] == 'decision':
        func.print_text(text, int(scene_data['clear_screen']))
    else:
        sound_name = scene_data['sound']
        sound_thread = func.play_sound(sounds, sound_name, 
                                       float(scene_data['volume']) if scene_data['volume'] else 1.0, 
                                       float(scene_data['speed']) if scene_data['speed'] else 1.0,
                                       eval(scene_data['position']) if scene_data['position'] else [0, 0, 0],
                                       float(scene_data['duration']) if scene_data['duration'] else 0,
                                       scene_data['loop'] == 'True', 
                                       scene_data['type'])
        func.player_interaction(sounds, "continue", text, sound_thread, sound_name, int(scene_data['clear_screen']))

def get_player_decision(sounds, options):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    return func.player_interaction(sounds, "selection", "", "", "", 0)

"""
def main():
    oalInit()
    player = Listener()
    player.set_position((0, 0, 0))
    sounds = func.obtain_sounds()
    
    story_data = load_story_data('story.csv')
    
    play_intro(sounds)
    
    current_scene_id = '1'
    background_thread = None
    
    while current_scene_id in story_data:
        scene = story_data[current_scene_id]
        
        if scene['text'] == 'detener':
            if background_thread.is_alive():
                sounds[scene['sound']].stop()
                background_thread.join()
            current_scene_id = scene['next_id']
        else:
            play_scene(sounds, scene)
            if scene['loop'] == "True":
                background_thread = func.threading.Thread(target=func.play_sound_threaded, args=(sounds[scene['sound']], 0.3, 1, [0, 0, -2], True))
                background_thread.start()
            if scene['options']:
                options = scene['options'].split('|')
                next_ids = scene['next_id'].split('|')
                decision = get_player_decision(sounds, options)
                current_scene_id = next_ids[decision - 1]
            else:
                current_scene_id = scene['next_id']
    
    # End of game
    print("Thanks for playing!")
"""

def main():
    oalInit()
    # Player
    player = Listener()
    player.set_position((0, 0, 0))
    # Sounds dictionary
    sounds = func.obtain_sounds()    
    # Loading CSV
    story_data = load_story_data('story2.csv')
    # Load Screen
    play_intro(sounds)
    current_scene_id = '1'
    background_thread = None
    bonfire_thread = None
    stop_event = func.threading.Event()
    
    while current_scene_id in story_data:
        scene = story_data[current_scene_id]
        
        if scene['text'] == 'detener':
            if background_thread.is_alive(): sounds[scene['sound']].stop() and background_thread.join()
        if scene['text'] == 'detener2':
            if bonfire_thread.is_alive(): 
                bonfire_thread.set() 
                sounds[scene['sound']].stop() 
                bonfire_thread.join() 
            current_scene_id = scene['next_id']
        else:
            if scene['type'] == 'move':
                bonfire_thread = func.threading.Thread(
                                    target=func.play_sound_with_distance,
                                    args=(sounds[scene['sound']], [0, 0, 0], eval(scene['position']) if scene['position'] else [0, 0, 5], float(scene['volume']) if scene['volume'] else 5.0, 10, True, stop_event)
                                    )
                bonfire_thread.start()
                current_scene_id = scene['next_id']
            else:
                play_scene(sounds, scene)
                if scene['type'] == 'static' and scene['loop'] == "True" and not background_thread:
                    sound = sounds[scene['sound']]
                    background_thread = func.threading.Thread(
                                    target=func.play_sound_threaded, 
                                    args=(sound,float(scene['volume']) if scene['volume'] else 1.0, float(scene['speed']) if scene['speed'] else 1.0, eval(scene['position']) if scene['position'] else [0, 0, 0], True)
                                    )
                    background_thread.start()
                if scene['options']:
                    options = scene['options'].split('|')
                    next_ids = scene['next_id'].split('|')
                    decision = get_player_decision(sounds, options)
                    current_scene_id = next_ids[decision - 1]
                else:
                    current_scene_id = scene['next_id']

if __name__ == "__main__":
    main()
