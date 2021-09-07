from src.menu.menu import Menu
from src.menu.menu_item import MenuItem
import datetime
import socket
import psutil
import math
from subprocess import call

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

def percentile_to_bars(percentile):
    bar_length = 10
    checked_bars = math.ceil(percentile * bar_length / 100)
    filled_bars = ["#"] * checked_bars
    blank_bars = [" "] * (bar_length - checked_bars)
    return "".join(filled_bars + blank_bars)

def get_cpu_usage():
    percentile = psutil.cpu_percent()
    return "CPU [" + percentile_to_bars(percentile) + "]"

def get_ram_usage():
    percentile = psutil.virtual_memory().percent
    return "RAM [" + percentile_to_bars(percentile) + "]"

def draw_usage():
    return [
        get_cpu_usage(),
        get_ram_usage()
    ]


def draw_shutdown():
    return ["Shutdown", ""]

def execute_shutdown():
    call("sudo shutdown -h now", shell=True)
    pass


def get_main_menu():
    main_menu = Menu("Main")

    hello_screen = MenuItem()
    hello_screen.set_handler(draw_hello_screen)

    usage = MenuItem()
    usage.set_handler(draw_usage)

    ip_addr = MenuItem()
    ip_addr.set_handler(draw_ip_addr)

    date_time = MenuItem()
    date_time.set_handler(draw_current_time)

    shutdown = MenuItem()
    shutdown.set_handler(draw_shutdown)
    shutdown.on_select(execute_shutdown)

    main_menu.add_item(hello_screen)
    main_menu.add_item(usage)
    main_menu.add_item(ip_addr)
    main_menu.add_item(date_time)
    main_menu.add_item(shutdown)
    
    return main_menu