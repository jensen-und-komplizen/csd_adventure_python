import copy

from src.loo.rooms.hallway import Hallway
from src.loo.rooms.loo import Loo
from src.loo.rooms.wash_room import WashRoom


class Adventure:

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
            "close eyes",
            "read a joke",
            "look around",
            "count",
            "use door to washroom",
            "use door to loo",
            "use door to hallway",
            "help",
            "open inventory"
        ]
        self.jokes_temp = copy.deepcopy(self.jokes)
        self.reread_jokes = False

    def tell(self, command):
        response = ""
        # keep your print statements to yourself.
        match command.lower():
            case "close eyes":
                self.loo.reset_counter()
                self.current_room = self.loo
                response = self.current_room.get_description()
            case "read a joke" | "read joke":
                if self.current_room == self.loo:
                    if len(self.jokes_temp) < 1:
                        self.reread_jokes = True
                        return "You've read them all. Go again? ;)"
                    return self.jokes_temp.pop(0)
                else:
                    response = "There is no joke in this room."
            case "yes":
                if self.reread_jokes:
                    self.jokes_temp = copy.deepcopy(self.jokes)
                    self.reread_jokes = False
                    return self.jokes_temp.pop(0)
                else:
                    return self.current_room.handle_command(command)
            case "no":
                if self.reread_jokes:
                    self.reread_jokes = False
                    return "Ok, suit yourself."
                else:
                    return self.current_room.handle_command(command)
            case "look around":
                response = self.current_room.get_detailed_description()
            case "count":
                self.counter += 1
                response = "The counter is at {}".format(self.counter)
            case "use door to washroom":
                self.current_room = self.washroom
                response = self.current_room.get_description()
            case "use door to loo":
                self.loo.reset_counter()
                self.current_room = self.loo
                response = "You are on the loo again. Still smelly."
            case "use door to hallway":
                if self.current_room == self.washroom:
                    self.current_room = self.hallway
                    response = self.current_room.get_description()
                else:
                    response = "There is no door to the hallway"
            case "help":
                response = self.current_room.get_help()
                if response is None or len(response) <= 0:
                    response = "There is no help for you!"
            case "open inventory":
                response = self.current_room.open_inventory()
            case _:
                return self.current_room.handle_command(command)
        self.last_response = response
        return response

    def begin(self):
        self.last_response = self.current_room.get_description()
        return self.current_room.get_description()
