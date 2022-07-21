from src.menu.menu_item import MenuItem

def execute():
    pass

def draw():
    return ["Back", ""]

def get_item():
    item = MenuItem()
    item.set_handler(draw)
    item.on_select(execute)
    return item

