from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def handle(self, command):
        pass


class CommandLister(ABC):

    @abstractmethod
    def list_commands(self):
        pass
