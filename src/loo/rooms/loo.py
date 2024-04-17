from src.loo.rooms.abstract_room import AbstractRoom
from src.loo.items.item import Item


class Loo(AbstractRoom):

    _MAGAZINES_COMMANDS = ["look at magazines", "magazines", "look magazines"]
    _LOOK_DOOR_COMMANDS = ["look at the door", "look door", "view door"]
    _LOOK_TOILET_PAPER_COMMANDS = ["look at toilet paper", "look toilet paper"]
    _PICK_TOILET_PAPER_COMMANDS = ["pick up toilet paper", "pick toilet paper"]
    _DOOR_COMMANDS = ["go through door", "go door"]
    _COIN_COMMANDS = ["grab coin", "coin"]


    __toilet_paper_count = None

    def __init__(self):
        self.__toilet_paper_count = 0
        self.door = Item(name="door",
                         message="It looks like the door to the washroom. Oh yes, lets flush out some bugs!")
        self.jokes = Item(name="jokes",
                          message="")
        self.toilet_paper = Item(name="toilet paper", 
                                 message="")
        self.magazines = Item(name="magazines", 
                                 message="You see a very much used Micky Mouse magazine, a very old and unusable playboy and what seems to be a scrum guide 2009 in mint condition.")
        self.coin = Item(name="coin", 
                        message="Eww, that wasn't a coin?!")

    def reset_counter(self):
        self.__toilet_paper_count = 0

    def get_description(self):
        return "You wake up on the loo. You have no idea where or who you are, but at least you have your inventory."

    def get_detailed_description(self):
        return f"""You see a pretty dirty {self.door}, with some nasty {self.jokes} on it. There are three pieces of {self.toilet_paper} on the ground. Next to you are a {self.coin} and a few {self.magazines}. \n
        In your pocket you find a card that says you are a pathetic scrum developer, PSD"""

    def handle_command(self, command):
        command_lower = command.lower()
        match command_lower:
            case _ if command_lower in self._MAGAZINES_COMMANDS:
                return self.magazines.message
            case _ if command_lower in self._LOOK_DOOR_COMMANDS:
                return self.door.message
            case _ if command_lower in self._LOOK_TOILET_PAPER_COMMANDS:
                self.__toilet_paper_count += 1
                match   self.__toilet_paper_count:
                    case 1:
                        return "On the first piece is written: \"Scrum Master: Nobody ever comes to my retros... I need to get out of here.\" There are more pieces on the ground."
                    case 2:
                        return "On the second piece is written: \"Product Owner: My developers are way too slow.\" There is one more piece on the ground."
                    case 3:
                        self.__toilet_paper_count = 0
                        return "On the last piece is written: \"Developers: We have too many meetings.\" I remember. I need to find my Scrum team to help them get out of here."
            case _ if command_lower in self._PICK_TOILET_PAPER_COMMANDS:
                return "Toilet paper is covered with diarrhea 💩. I am not going to pick that up >:("
            case _ if command_lower in self._DOOR_COMMANDS:
                return
            case _ if command_lower in self._COIN_COMMANDS:
                return self.coin.message
            case _:
                return "you wake up on the Loo." + "\n" + super().handle_command(command)

    def get_help(self):
        return super().get_help() + "try to 'look around', 'look at magazines' (better get your gloves), 'grab coin', 'look at toilet paper', 'pick up toilet paper', 'read a joke' or just 'use door to washroom' to escape the smell."
