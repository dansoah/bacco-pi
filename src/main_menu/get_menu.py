from src.menu.menu import Menu
from src.main_menu.ip_addr_item import get_item as get_ip_addr_item
from src.main_menu.shutdown_item import get_item as get_shutdown_item
from src.main_menu.services_item import get_item as get_services_item
from src.main_menu.resource_usage_item import get_item as get_usage_item
from src.main_menu.hello_screen_item import get_item as get_hello_screen_item
from src.main_menu.current_time_item import get_item as get_current_time_item

def get_main_menu():
    main_menu = Menu("Main")

    main_menu.add_item(get_hello_screen_item())
    main_menu.add_item(get_usage_item())
    main_menu.add_item(get_ip_addr_item())
    main_menu.add_item(get_current_time_item())
    main_menu.add_item(get_services_item())
    main_menu.add_item(get_shutdown_item())
    
    return main_menu