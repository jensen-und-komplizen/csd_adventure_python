from src.loo.rooms.abstract_room import AbstractRoom


class Loo(AbstractRoom):

    __toilet_paper_count = None

    def __init__(self):
        self.__toilet_paper_count = 0

    def reset_counter(self):
        self.__toilet_paper_count = 0

    def get_description(self):
        return "You wake up on the loo. You have no idea where or who you are."

    def get_detailed_description(self):
        return "You see a pretty dirty door, with some nasty jokes on it. There are three pieces of toilet paper on the ground. Next to you are a coin and a few magazines." + "<br/>" + "In your pocket you find a card that says you are a pathetic scrum developer, PSD"

    def handle_command(self, command):
        match command.lower():
            case "look at magazines":
                return "You see a very much used Micky Mouse magazine, a very old and unusable playboy and what seems to be a scrum guide 2009 in mint condition."
            case "look at toilet paper":
                self.__toilet_paper_count += 1
                match self.__toilet_paper_count:
                    case 1:
                        return "On the first piece is written: \"Scrum Master: Nobody ever comes to my retros... I need to get out of here.\" There are more pieces on the ground."
                    case 2:
                        return "On the second piece is written: \"Product Owner: My developers are way too slow.\" There is one more piece on the ground."
                    case 3:
                        self.__toilet_paper_count = 0
                        return "On the last piece is written: \"Developers: We have too many meetings.\" I remember. I need to find my Scrum team to help them get out of here."
            case "go through door":
                return
            case _:
                return "you wake up on the Loo" + "\n" + super().handle_command(command)

    def get_help(self):
        return super().get_help() + "try to 'look around', 'look at magazines' (better get your gloves), 'look at toilet paper' or just 'use door to washroom' to escape the smell."
