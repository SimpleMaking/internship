from antagonistfinder import AntagonistFinder
from abc import ABC, abstractmethod

class GiperHero(ABC):
    @abstractmethod
    def fire_a_gun(self):
        pass
    
    @abstractmethod
    def incinerate_with_lasers(self):
        pass
    
    
class UltraHero(ABC):
    @abstractmethod
    def incinerate_with_lasers(self):
        pass
        
    @abstractmethod
    def roundhouse_kick(self):
        pass


class SuperHero(GiperHero):
    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)
 
    def fire_a_gun(self):
        print('PIU PIU')

    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')
     
    def attack(self):
        self.fire_a_gun()

    def ultimate(self):
        self.incinerate_with_lasers()
        


class Superman(SuperHero):
    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)
    
    def getting_power(self):
        print("Brrrrrrraaaahhhh")

        
    def attack(self):
        self.getting_power()
    
    #переопределяем для каждого наследника SuperHero
    def ultimate(self):
        print("CRUNK!")
            
    
        
