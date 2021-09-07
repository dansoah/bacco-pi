class MenuItem:
    def __init__(self):
        self.handler = None
        pass

    def set_handler(self, handler):
        if not callable(handler):
            raise ValueError("The handler for a menu item must be a function!")
        
        self.handler = handler

    def get_info(self):
        return self.handler()
