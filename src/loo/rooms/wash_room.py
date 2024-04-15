from src.loo.rooms.abstract_room import AbstractRoom
from src.loo.items.item import Item


class WashRoom(AbstractRoom):

    def __init__(self):
        self.dod = Item(name="DoD", 
                        message="hands washed?" + "\n" + "paper towels in bin?" + "\n" + "toilet flushed?")
        
        self.blockchain = Item(name="blockchain", 
                        message="Nice, now I have a blockhain in my pocket. Maybe I will become a Crpyto millionaire?!")
        
        self.coin = Item(name="coin", 
                        message="Eww, that wasn't a coin?!")
        
        self.door = Item(name="door", 
                        message="")
                        
    def get_description(self):
        return "You enter a room that looks like a wash room."

    def get_detailed_description(self):
        return f"""You see a {self.coin} on the floor. \n
        You also see an incredibly nasty sink with an undefinable substance in it. Ew! \n
        You notice a {self.dod} on the door. \n
        On the other side of the room you see two doors, one {self.door} to the hallway and another one to the loo. \n
        Oh, and there's a {self.blockchain} in the corner. Interesting.."""

    def handle_command(self, command):
        command_lower = command.lower()

        if command_lower == "read dod":
            response = self.dod.message
        elif command_lower == "grab blockchain":
            response = self.blockchain.message
        elif command_lower == "grab coin":
            response = self.coin.message
        else:
            response = super().handle_command(command)
        return response
            
    def get_help(self):
        return super().get_help() + "try to 'look around', 'read DoD', or 'use door to hallway', or 'use door to loo', or 'grab coin', or 'grab blockchain'. Might help."
