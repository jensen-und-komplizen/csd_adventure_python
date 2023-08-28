from src.loo.rooms.abstract_room import AbstractRoom
from src.loo.items.item import Item


class Loo(AbstractRoom):

    __toilet_paper_count = None

    def __init__(self):
        self.__toilet_paper_count = 0
        self.door = Item(name="door",
                         message="Oh, it looks like the door to the wash room!")
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
        return "You wake up on the loo. You have no idea where or who you are."

    def get_detailed_description(self):
        return f"""You see a pretty dirty {self.door}, with some nasty {self.jokes} on it. There are three pieces of {self.toilet_paper} on the ground. Next to you are a {self.coin} and a few {self.magazines}. \n
        In your pocket you find a card that says you are a pathetic scrum developer, PSD"""

    def handle_command(self, command):
        match command.lower():
            case "look at magazines":
                return self.magazines.message
            case "look at the door":
                return self.door.message
            case "look at toilet paper":
                self.__toilet_paper_count += 1
                match   self.__toilet_paper_count:
                    case 1:
                        return "On the first piece is written: \"Scrum Master: Nobody ever comes to my retros... I need to get out of here.\" There are more pieces on the ground."
                    case 2:
                        return "On the second piece is written: \"Product Owner: My developers are way too slow.\" There is one more piece on the ground."
                    case 3:
                        self.__toilet_paper_count = 0
                        return "On the last piece is written: \"Developers: We have too many meetings.\" I remember. I need to find my Scrum team to help them get out of here."
            case "go through door":
                return
            case "grab coin":
                return self.coin.message
            case _:
                return "you wake up on the Loo" + "\n" + super().handle_command(command)

    def get_help(self):
        return super().get_help() + "try to 'look around', 'look at magazines' (better get your gloves), 'grab coin', 'look at toilet paper', 'read a joke' or just 'use door to washroom' to escape the smell."
