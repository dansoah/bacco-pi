from src.menu.menu_item import MenuItem
from subprocess import call

def execute():
    call("sudo shutdown -h now", shell=True)

def draw():
    return ["Shutdown", ""]

def get_item():
    item = MenuItem()
    item.set_handler(draw)
    item.on_select(execute)
    return item

