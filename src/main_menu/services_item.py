from src.menu.menu_item import MenuItem
from src.services_menu.get_menu import get_services_menu 

def execute():
    return  get_services_menu()

def draw():
    return ["Services", "               >"]

def get_item():
    item = MenuItem()
    item.set_handler(draw)
    item.on_select(execute)
    return item

