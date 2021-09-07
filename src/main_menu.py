from src.menu.menu import Menu
from src.menu.menu_item import MenuItem
import datetime
import socket
    
def get_ip_addr():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_addr = s.getsockname()[0]
    s.close()
    return ip_addr

def draw_ip_addr():
    ip_addr = get_ip_addr()
    return ["IP Address", ip_addr]

def draw_hello_screen():
    return ["Hello!", "I'm awake :)"]

def draw_current_time():
    return [
        datetime.datetime.now().strftime('%Y-%m-%d'),
        datetime.datetime.now().strftime('%H:%M:%S')
    ]

def get_main_menu():
    main_menu = Menu("Main")

    hello_screen = MenuItem()
    hello_screen.set_handler(draw_hello_screen)

    ip_addr = MenuItem()
    ip_addr.set_handler(draw_ip_addr)

    date_time = MenuItem()
    date_time.set_handler(draw_current_time)

    main_menu.add_item(hello_screen)
    main_menu.add_item(ip_addr)
    main_menu.add_item(date_time)
    
    return main_menu