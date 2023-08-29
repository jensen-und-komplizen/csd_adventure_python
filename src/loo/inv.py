class Inv():
    inventory_list = []
    
    @staticmethod
    def add_item(cls, item):
        cls.inventory_list.append(item)
    @staticmethod
    def get_all_items(cls):
        return cls.inventory_list
        
    @staticmethod
    def show_inventory(cls):
        return f"<mark>{str(cls.inventory_list)}</mark>"