from abc import ABC, abstractmethod

# abstract class
class QuackBehavior(ABC):
    @staticmethod
    @abstractmethod
    def quack():
        pass

# concrete classes
class Quack(QuackBehavior):
    @staticmethod
    def quack():
        print('Quack')

class Squeak(QuackBehavior):
    @staticmethod
    def quack():
        print('Squeak')
        
class Mute(QuackBehavior):
    @staticmethod
    def quack():
        print('...')
