import sys
import time
import threading
import os
import scenes.py

# Global flag
_skip_event = threading.Event()

def _key_listener():
    """Runs in background — sets the event when any key is pressed"""
    try:
        input()                    # Blocks until Enter is pressed
        _skip_event.set()          # Tell the main thread: "SKIP!"
    except EOFError:
        pass

def slow_print(text, delay=0.03, end='\n'):
    """
    Prints text slowly.
    Player can press Enter (or any key) to instantly finish the current line.
    Works perfectly on Linux/Mac/WSL/Windows without hanging.
    """
    global _skip_event
    _skip_event.clear()

    # Start background listener
    listener = threading.Thread(target=_key_listener, daemon=True)
    listener.start()

    printed = 0
    for i, char in enumerate(text):
        if _skip_event.is_set():
            # Dump the rest instantly
            print(text[printed:] + end, end='', flush=True)
            return
        print(char, end='', flush=True)
        printed += 1
        time.sleep(delay)

    print(end=end)

def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')

def show_intro():
    clear_screen()
    slow_print("The year is Tenmei 8.")
    slow_print("Winter clings to Kyoto like a dying breath.")
    slow_print("Ash drifts in the wind.")
    slow_print("The city waits for those who remain.\n")
    input("Press ENTER to continue...")

def main_menu():
    clear_screen()
    print("===============================================")
    print("                 AFTER KYOTO")
    print("        A Story of Ashes, Loss, and Renewal")
    print("===============================================\n")
    print("[1] Start New Journey")
    print("[2] Continue Last Save")
    print("[3] Load Saved Game")
    print("[4] Settings")
    print("[5] Quit\n")
    print("-----------------------------------------------")

    choice = input("Select an option: ")
    return choice

def play_scenes(start_scene_id):
    current_scene_id = start_scene_id

    while True:
        scene = scenes[current_scene_id]
        print('\n' + "=" * 50)
        scene.display()
        print()

        if len(scene.choices) == 1 and scene.choices[0].next_scene_id == "End":
            input('\n Press ENTER to return to the main menu...')
            break

        player_input = input('\n Choose an option: ').strip()

        chosen = None

        for choice in scene.choices:
                if choice.key == player_input:
                    chosen = choice
                    break
        if not chosen:
            print('Please choose a valid option')
        
        if chosen.next_scene_id == "END":
            print("\nThe story will continue in a future chapter...")
            input("\nPress ENTER to return to the main menu...")
            break
        else:
            current_scene_id = chosen.next_scene_id


def start_new_game():
    create_scenes()
    play_scenes("approach_kyoto")


# ---------- GAME LOOP STARTS HERE ----------
if __name__ == "__main__":
    show_intro()

    while True:
        choice = main_menu()

        if choice == "1":
            print("Starting a new journey...")
            clear_screen()
            play_scenes(scene1)
            # start_new_game()
            break
        elif choice == "2":
            print("Continuing last save...")
            # continue_last_save()
            break
        elif choice == "3":
            print("Loading a saved game...")
            # load_saved_game()
            break
        elif choice == "4":
            print("Opening settings...")
            # open_settings()
        elif choice == "5":
            print("Farewell, traveler.")
            break
        else:
            print("Please enter a valid option.")
            time.sleep(1)

