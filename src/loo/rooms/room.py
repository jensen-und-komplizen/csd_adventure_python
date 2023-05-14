from abc import ABC, abstractmethod


class Room(ABC):

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_detailed_description(self):
        pass

    @abstractmethod
    def handle_command(self, command):
        pass

    @abstractmethod
    def get_help(self):
        pass
