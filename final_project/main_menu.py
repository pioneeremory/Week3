import time
import os

def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.1):
    """Print text slowly for dramatic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print() 

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


# ---------- GAME LOOP STARTS HERE ----------
if __name__ == "__main__":
    show_intro()

    while True:
        choice = main_menu()

        if choice == "1":
            print("Starting a new journey...")
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
