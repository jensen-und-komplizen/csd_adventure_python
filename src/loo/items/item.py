class Item():

    def __init__(self, name, message):
        self.name = name
        self.message = message
    
    def __str__(self):
        return f"<mark>{self.name}</mark>"