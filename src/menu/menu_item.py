class MenuItem:
    def __init__(self):
        self.handler = None
        self.on_select_callback = None
        pass

    def set_handler(self, handler):
        if not callable(handler):
            raise ValueError("The handler for a menu item must be a function!")
        
        self.handler = handler

    def on_select(self, on_select_callback):
        if not callable(on_select_callback):
            raise ValueError("The handler for a menu item must be a function!")

        self.on_select_callback = on_select_callback

    def get_info(self):
        return self.handler()
    
    def selected(self):
        if not callable(self.on_select_callback):
            return None

        return self.on_select_callback()

    
        
