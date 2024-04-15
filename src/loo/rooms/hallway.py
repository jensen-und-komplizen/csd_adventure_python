from src.loo.rooms.abstract_room import AbstractRoom


class Hallway(AbstractRoom):

    def get_description(self):
        return "You enter a hallway that looks dark."

    def get_detailed_description(self):
        return "On the other side of the hall you see a door leading to a team room." + "</br>" + \
               "There is a door to the washroom."

    def get_help(self):
        return super().get_help() + "try to 'look around' or 'use door to washroom'. Might help."
    
    def handle_command(self, command):
        match command.lower():
            case "look at the corner":
                return "you are seeing a pile of blocks"
            case _:
                return "you wake up on the Loo" + "\n" + super().handle_command(command)