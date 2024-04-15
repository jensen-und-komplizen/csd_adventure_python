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
        command_lower = command.lower()

        if command_lower == "look at the corner":
            response = "you are seeing a pile of blocks"
        else:
            response = "you wake up on the Loo" + "\n" + super().handle_command(command)

        return response