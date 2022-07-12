from antagonistfinder import Place
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

    def find(self, place):
        Place.get_antagonist(Place, place)
 
    def fire_a_gun(self):
        print('PIU PIU')

    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')
     
    def attack(self):
        self.fire_a_gun()

    def ultimate(self):
        self.fire_a_gun()
        


class Superman(SuperHero):
    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)
    
    def getting_power(self):
        print("Brrrrrrraaaahhhh")
        
    def attack(self):
        self.getting_power()
    
    #переопределяем для каждого наследника SuperHero
    def ultimate(self):
        if 'Cl' in self.name:
            self.incinerate_with_lasers()
    
        
