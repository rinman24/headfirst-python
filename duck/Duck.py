from abc import ABC, abstractmethod
import FlyBehavior
import QuackBehavior

class Duck(ABC):
    """Duck abstract base class."""
    def __init__(self):
        self._fly_behavior = None
        self._quack_behavior = None
    
    def fly(self):
        self._fly_behavior.fly()
    
    def quack(self):
        self._quack_behavior.quack()
    
    def set_fly_behavior(self, fb):
        self._fly_behavior = fb
    
    def set_quack_behavior(self, qb):
            self._quack_behavior = qb
    
    @staticmethod
    def swim():
        print('All ducks float, even decoys!')
    
    @staticmethod
    @abstractmethod
    def display():
        pass

class MallardDuck(Duck):
    def __init__(self):
        self._fly_behavior = FlyBehavior.FlyWithWings
        self._quack_behavior = QuackBehavior.Quack
    
    @staticmethod
    def display():
        print("I'm a mild malard.")

class RedheadDuck(Duck):
    def __init__(self):
        self._fly_behavior = FlyBehavior.FlyWithWings
        self._quack_behavior = QuackBehavior.Quack
    
    @staticmethod
    def display():
        print("I'm a rambunctious redhead.")

class RubberDuck(Duck):
    def __init__(self):
        self._fly_behavior = FlyBehavior.FlyNoWay
        self._quack_behavior = QuackBehavior.Squeak
    
    @staticmethod
    def display():
        print("I'm a real rubber ducky.")

class DecoyDuck(Duck):
    def __init__(self):
        self._fly_behavior = FlyBehavior.FlyNoWay
        self._quack_behavior = QuackBehavior.Mute
    
    @staticmethod
    def display():
        print("I'm a dull decoy.")

if __name__ == '__main__':
    mallard_duck = MallardDuck()
    redhead_duck = RedheadDuck()
    rubber_duck = RubberDuck()
    decoy_duck = DecoyDuck()

    mallard_duck.display()
    mallard_duck.quack()
    mallard_duck.fly()
    mallard_duck.swim()
    print()

    redhead_duck.display()
    redhead_duck.quack()
    redhead_duck.fly()
    redhead_duck.swim()
    print()
    
    rubber_duck.display()
    rubber_duck.quack()
    rubber_duck.fly()
    rubber_duck.swim()
    print()

    decoy_duck.display()
    decoy_duck.quack()
    decoy_duck.fly()
    decoy_duck.swim()
    print()

    rubber_duck.set_fly_behavior(FlyBehavior.FlyWithRockets)
    rubber_duck.fly()
    rubber_duck.set_fly_behavior(FlyBehavior.FlyNoWay)
    rubber_duck.fly()
    print()

    decoy_duck.set_quack_behavior(QuackBehavior.Quack)
    decoy_duck.quack()
    decoy_duck.set_quack_behavior(QuackBehavior.Mute)
    decoy_duck.quack()
    print()
