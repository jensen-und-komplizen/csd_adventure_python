from src.loo.rooms.room import Room
from abc import abstractmethod
from src.loo.inv import Inv


class AbstractRoom(Room):

    def handle_command(self, command):
        message = "Did you just ask me to '{}'<br /><br />404 - command not found. {}".format(command, self.get_help())
        return message

    def get_help(self):
        return "If you want to restart, just try to 'commit suicide' or 'open your inventory' to open your inventory or "

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_detailed_description(self):
        pass

    def open_inventory(self):
        inv = Inv.get_all_items(Inv)
        if(len(inv) == 0):
            return "your inventory is empty :("
        return str(inv)
