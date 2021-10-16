from src.main_menu.get_menu import get_main_menu
import os
current_menu = get_main_menu()
current_menu.first_item()

while True:
    os.system('clear')

    lines = current_menu.get_data()
    print(lines[0])
    print(lines[1])
    print(" ")
    x = input()
    print(x)
    if x == 'n':
        current_menu.next_item()
    
    if x == 'p':
        current_menu.previous_item()

    if x == 's':
        current_menu.select_item()

    