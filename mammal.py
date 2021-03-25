from abc import ABC, abstractmethod


class Mammal(ABC):
    @abstractmethod
    def walk(self):
        pass