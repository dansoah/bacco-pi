from src.main_menu.get_menu import get_main_menu
from src.menu.menu import Menu
import os
current_menu = get_main_menu()
current_menu.first_item()

while True:
    #os.system('clear')

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
        selected = current_menu.select_item()
        if isinstance(selected, Menu):
            current_menu = selected
            current_menu.first_item()
            