from src.menu.menu_item import MenuItem

def draw():
    return ["Hello!", "I'm awake :)"]

def get_item():
    item = MenuItem()
    item.set_handler(draw)
    return item

