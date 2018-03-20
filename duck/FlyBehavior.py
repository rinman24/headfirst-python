from abc import ABC, abstractmethod

# abstract class
class FlyBehavior(ABC):
    @staticmethod
    @abstractmethod
    def fly():
        pass

# Concrete implementations
class FlyWithWings(FlyBehavior):
    @staticmethod
    def fly():
        print("I'm flying!!")

class FlyNoWay(FlyBehavior):
    @staticmethod
    def fly():
        print("I can't fly.")

class FlyWithRockets(FlyBehavior):
    @staticmethod
    def fly():
        print("I'm flying with rockets!!")
