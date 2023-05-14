import re

from src.loo.items.Command import Command, CommandLister


class CoffeeMaker(CommandLister):

    __commands = []
    power_available = None
    coffee_in_the_machine = None
    cup_in_the_machine = None
    water_in_the_machine = None
    error = ""

    def __init__(self):
       self.__commands.append(AddBeans(self))

    def brew(self):
        return True

    def whats_wrong(self):
        return self.error

    def connect_power(self):
        self.power_available = True

    def add_coffee_beans(self):
        self.coffee_in_the_machine = True

    def put_cup_in(self):
        self.cup_in_the_machine = True

    def add_water(self):
        self.water_in_the_machine = True

    def make_coffee(self):
        if self.power_available:
            if self.coffee_in_the_machine:
                if self.cup_in_the_machine:
                    if self.water_in_the_machine:
                        return self.brew()
                    else:
                        self.error = "There is no water in the machine"
                        return False
                    return self.brew()
                else:
                    self.error = "There is no cup the machine"
                    return False
                return self.brew()
            else:
                self.error = "There are no coffee beans in the machine"
                return False
            return self.brew()
        else:
            self.error = "There is no power connected"
            return False

    def handle(self, incoming_command):
        for command in self.__commands:
            message = command.handle(incoming_command.lower())
            if message:
                return message
        return None

    def list_commands(self):
        available_commands = []
        for command in self.__commands:
            available_commands.append(command.list_commands)
        return available_commands


class AddBeans(Command, CommandLister):

    __coffeemaker = None

    def __init__(self, coffeemaker):
        self.__coffeemaker = coffeemaker

    def handle(self, command):
        if re.match("add beans", command):
            self.__coffeemaker.add_coffee_beans()
            return "Beans have been added to the coffee machine."
        return None

    def list_commands(self):
        return "add beans"
