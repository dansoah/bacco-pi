from src.menu.menu_item import MenuItem
import datetime

def draw():
    return [
        datetime.datetime.now().strftime('%Y-%m-%d'),
        datetime.datetime.now().strftime('%H:%M:%S')
    ]

def get_item():
    item = MenuItem()
    item.set_handler(draw)
    return item