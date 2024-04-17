import copy

from src.loo.rooms.hallway import Hallway
from src.loo.rooms.loo import Loo
from src.loo.rooms.wash_room import WashRoom


class Adventure:

    _JOKE_COMMANDS = ["read a joke", "read joke", "rj", "joke"]
    _CLOSE_EYES_COMMANDS = ["close eyes", "ce"]
    _LOOK_AROUND_COMMANDS = ["look around", "look", "la"]
    _WASHROOM_COMMANDS = ["use door to washroom", "go to washroom", "washroom"]
    _LOO_COMMANDS = ["use door to loo", "loo", "go to loo"]
    _HALLWAY_COMMANDS = ["use door to hallway", "go to hallway", "hallway"]
    _YES_COMMANDS = ["yes", "y"]
    _NO_COMMANDS = ["no", "n"]
    _HELP_COMMANDS = ["help", "h"]
    _INVENTORY_COMMANDS = ["open inventory", "inventory", "i"]
    counter = None
    current_room = None
    loo = None
    washroom = None
    last_response = None

    def __init__(self):
        self.loo = Loo()
        self.washroom = WashRoom()
        self.hallway = Hallway()
        self.current_room = self.loo
        self.counter = 0
        self.last_response = ""
        self.jokes = [
            "Why do we tell actors to 'break a leg'? - Because every play has a cast ;)",
            "What to call a dog thats also a magician? - a labracadabrador ;)",
            "Did you hear about the actor who fell through the floorboard?...He was just going through a stage. ;)",
            "Did you hear about the claustrophobic astronaut?..He just needed a little space ;)",
            "Why is the e function not invited to the party? - because you can't integrate it ;)",
        ]
        self.standard_commands = [
            "help",
            "read a joke",
            "look around",
            "use door to washroom",
            "use door to loo",
            "use door to hallway",
            "open inventory",
            "close eyes",
        ]
        self.jokes_temp = copy.deepcopy(self.jokes)
        self.reread_jokes = False

    def tell(self, command):
        response = ""
        command_lower = command.lower()
        # keep your print statements to yourself.
        match command_lower:
            case _ if command_lower in self._CLOSE_EYES_COMMANDS:
                self.loo.reset_counter()
                self.current_room = self.loo
                response = self.current_room.get_description()
            case _ if command_lower in self._JOKE_COMMANDS:
                if self.current_room == self.loo:
                    if len(self.jokes_temp) < 1:
                        self.reread_jokes = True
                        return "You've read them all. Go again? ;)"
                    return self.jokes_temp.pop(0)
                else:
                    response = "There is no joke in this room."
            case _ if command_lower in self._YES_COMMANDS:
                if self.reread_jokes:
                    self.jokes_temp = copy.deepcopy(self.jokes)
                    self.reread_jokes = False
                    return self.jokes_temp.pop(0)
                else:
                    return self.current_room.handle_command(command)
            case _ if command_lower in self._NO_COMMANDS:
                if self.reread_jokes:
                    self.reread_jokes = False
                    return "Ok, suit yourself."
                else:
                    return self.current_room.handle_command(command)
            case _ if command_lower in self._LOOK_AROUND_COMMANDS:
                response = self.current_room.get_detailed_description()
            case "count":
                self.counter += 1
                response = "The counter is at {}".format(self.counter)
            case _ if command_lower in self._WASHROOM_COMMANDS:
                self.current_room = self.washroom
                response = self.current_room.get_description()
            case _ if command_lower in self._LOO_COMMANDS:
                self.loo.reset_counter()
                self.current_room = self.loo
                response = "You are on the loo again. Still smelly."
            case _ if command_lower in self._HALLWAY_COMMANDS:
                if self.current_room == self.washroom:
                    self.current_room = self.hallway
                    response = self.current_room.get_description()
                else:
                    response = "There is no door to the hallway"
            case _ if command_lower in self._HELP_COMMANDS:
                response = self.current_room.get_help()
                if response is None or len(response) <= 0:
                    response = "There is no help for you!"
            case _ if command_lower in self._INVENTORY_COMMANDS:
                response = self.current_room.open_inventory()
            case _:
                return self.current_room.handle_command(command)
        self.last_response = response
        return response

    def begin(self):
        self.last_response = self.current_room.get_description()
        return self.current_room.get_description()
