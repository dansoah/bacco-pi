from src.menu.menu_item import MenuItem

class Menu:

    def __init__(self, name):
        self.name = name
        self.items = []
        self.current_item = None

    def add_item(self, item):
        self.items.append(item)

    def next_item(self):
        index = self.items.index(self.current_item)
        index += 1
        
        if(index > len(self.items) -1):
            index = 0

        self.current_item = self.items[index]
    
    def previous_item(self):
        index = self.items.index(self.current_item)
        index -= 1
        
        if(index < 0):
            index = len(self.items) -1

        self.current_item = self.items[index]

    def first_item(self):
        self.current_item = self.items[0]

    def last_item(self):
        self.current_item = self.items[Len(items)]

    def select_item(self):
        return self.current_item.selected()

    def get_data(self):
        return self.current_item.get_info()