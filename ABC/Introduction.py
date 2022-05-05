# Abstract Classes: the ABC

# Abstract classes are classes that contain one or more abstract methods, which is a method
# that is declared but isn't implemented.
# Abstract classes cannot be instantiated and require subclasses to provide implementations for the abstract methods.
# Moreover, each method defined in the AbstractClass must be implemented inside the child class, otherwise
# an error would be raised.

# From the data scientist point of view, an abstract class is useful in order to define classes that are the same implemented methods.

from abc import ABC, abstractmethod


class AbstractClassexample(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    # questo metodo è stato definito ma non implemenatto:
    # o meglio, io posso anche implementarlo ma verrà sovrascritto
    # dal metodo che verrà scritto nella classe figlia.
    @abstractmethod
    def do_something(self):
        pass

class Add42(AbstractClassexample):

    def do_something(self):
        return self.value + 42

class Add45(AbstractClassexample):

    def do_something(self):
        return self.value + 45


my_class = Add42(3)
new_value = my_class.do_something()
print(f"My value: {new_value}")

# In questo modo ho sempre obbligo la classe figlia ad avere la stessa logica implementata nella classe madre.
my_class = Add45(3)
new_value = my_class.do_something()
print(f"My value: {new_value}")

