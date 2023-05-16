from src.loo.rooms.abstract_room import AbstractRoom


class WashRoom(AbstractRoom):

    def get_description(self):
        return "You enter a room that looks like a wash room."

    def get_detailed_description(self):
        return "You see a coin on the floor. " + "<br/>" + "You also see an incredibly nasty sink with an undefinable substance in it. Ew!" + "<br/>" + "You notice a <mark>DoD</mark> on the door." + "</br>" + "On the other side of the room you see two doors, one <mark>door</mark> to the hallway and another one to the loo." + "</br>" + "Oh, and there's a blockchain in the corner. Interesting.."

    def handle_command(self, command):
        match command.lower():
            case "read dod":
                return "hands washed?" + "</br>" + "paper towels in bin?" + "</br>" + "toilet flushed?"
            case _:
                return super().handle_command(command)

    def get_help(self):
        return super().get_help() + "try to 'look around', 'read DoD', or 'use door to hallway', or 'use door to loo'. Might help."
