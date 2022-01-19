from src.menu.menu import Menu
from src.services_menu.go_back_item import get_item as get_go_back_item

def get_services_menu():
    sub_menu = Menu("Services")

    sub_menu.add_item(get_go_back_item())
    
    return sub_menu