#!/usr/bin/env python3
def regular_timer():
    return ("Starting regular timer...")
    # Implement the regular timer logic here
    

def long_pomodoro():
    return ("Starting long Pomodoro...")
    # Implement the long Pomodoro logic here

def short_pomodoro():
    return ("Starting short Pomodoro...")
    # Implement the short Pomodoro logic here

def change_settings():
    return ("Changing settings...")
    # Implement the settings change logic here

def exit_program():
    return ("Exiting the program...")
    # Implement the exit logic here


def main_menu():
    switch_dict = {
    '1': regular_timer,
    '2': long_pomodoro,
    '3': short_pomodoro,
    '4': change_settings,
    '5': exit_program
}
    
    while True:
        print("Main Menu:")
        print("1. Regular Timer")
        print("2. Long Pomodoro")
        print("3. Short Pomodoro")
        print("4. Change Settings")
        print("5. Exit")

        choice = input("Please enter number corresponding your choice: ")
        
        if choice in switch_dict:
            switch_dict[choice]()
            if choice == '5':
                break  # Exit the loop if the user chooses to exit
        else:
            print("Invalid choice, please try again.")