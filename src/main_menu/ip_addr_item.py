from src.menu.menu_item import MenuItem
import socket

def get_ip_addr():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_addr = s.getsockname()[0]
    s.close()
    return ip_addr

def draw():
    ip_addr = get_ip_addr()
    return ["IP Address", ip_addr]

def get_item():
    item = MenuItem()
    item.set_handler(draw)
    return item

