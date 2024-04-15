from src.loo.rooms.abstract_room import AbstractRoom
from src.loo.items.item import Item


class Loo(AbstractRoom):

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

        if command_lower == "look at magazines":
            response = self.magazines.message
        elif command_lower == "look at the door":
            response = self.door.message
        elif command_lower == "look at toilet paper":
            self.__toilet_paper_count += 1
            if self.__toilet_paper_count == 1:
                response = "On the first piece is written: \"Scrum Master: Nobody ever comes to my retros... I need to get out of here.\" There are more pieces on the ground."
            elif self.__toilet_paper_count == 2:
                response = "On the second piece is written: \"Product Owner: My developers are way too slow.\" There is one more piece on the ground."
            elif self.__toilet_paper_count == 3:
                self.__toilet_paper_count = 0
                response = "On the last piece is written: \"Developers: We have too many meetings.\" I remember. I need to find my Scrum team to help them get out of here."
        elif command_lower == "pick up toilet paper":
            response = "Toilet paper is covered with diarrhea 💩. I am not going to pick that up >:("
        elif command_lower == "go through door":
            response = None  # Replace with your desired action for this command
        elif command_lower == "grab coin":
            response = self.coin.message
        else:
            response = "you wake up on the Loo" + "\n" + super().handle_command(command)
        return response

    def get_help(self):
        return super().get_help() + "try to 'look around', 'look at magazines' (better get your gloves), 'grab coin', 'look at toilet paper', 'pick up toilet paper', 'joke' or just 'use door to washroom' to escape the smell."
