from abc import ABC, abstractmethod

class Place(ABC):
    @abstractmethod
    def get_person(self, place):
        pass

class AntagonistFinder():
    def get_antagonist(self, place):
        place.get_person()
       
