from src.loo.rooms.loo import Loo
from src.loo.rooms.wash_room import WashRoom
from src.loo.rooms.hallway import Hallway


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

    def tell(self, command):
        response = ""
        print(command)
        match command.lower():
            case "commit suicide":
                self.loo.reset_counter()
                self.current_room = self.loo
                response = self.current_room.get_description()
            case "read a joke":
                if self.current_room == self.loo:
                    response = "Why do we tell actors to 'break a leg?' - Because every play has a cast ;)"
                else:
                    response = "There is no joke in this room."
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
                    response = "You are on the hallway, a dark one without light."
                else:
                    response = "There is no door to the hallway"
            case "help":
                response = self.current_room.get_help()
                if response is None or len(response) <= 0:
                    response = "There is no help for you!"
            case _:
                return self.current_room.handle_command(command)
        self.last_response = response
        return response

    def begin(self):
        self.last_response = self.current_room.get_description()
        return self.current_room.get_description()