from src.menu.menu_item import MenuItem
from src.utils.charts import percentile_to_bars
import psutil

def get_cpu_usage():
    percentile = psutil.cpu_percent()
    return "CPU [" + percentile_to_bars(percentile) + "]"

def get_ram_usage():
    percentile = psutil.virtual_memory().percent
    return "RAM [" + percentile_to_bars(percentile) + "]"

def draw():
    return [
        get_cpu_usage(),
        get_ram_usage()
    ]

def get_item():
    item = MenuItem()
    item.set_handler(draw)
    return item

