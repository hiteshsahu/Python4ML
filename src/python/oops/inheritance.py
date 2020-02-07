"""
 -class C(A, B):   # subclass of A and B

 Checking
 - issubclass(sub, sup): check if sub is a subclass of the superclass sup.
 - isinstance(obj, Class): check if obj is an instance of Class or instance of a subclass of Class

"""


class Animal:
    """Animal Super Class"""
    def __init__(self):
        print("Animal Parent Constructor")

    def makeSound(self):
        pass


class Bird:
    """Bird Super Class"""
    def __init__(self):
        print("Bird Parent Constructor")

    def fly(self):
        print("Flying")


class Dog(Animal):
    """Dog extends Animal and Override methods"""
    def __init__(self):
        print("Child Constructor")  # Override Parent Constructor

    def makeSound(self):  # Override Parent Method
        print("Bark")


class Fox(Animal):
    """Fox extends Animal and extend methods"""
    def __init__(self, color):
        self.color= color
        super().__init__()  # Call Super Method


puppy = Dog()
puppy.makeSound()

fox = Fox("Red")
fox.makeSound()
print(fox.color)


class Bat(Animal, Bird):
    """Multiple Parent Inheritance"""
    def __init__(self):
        print("Child Constructor")  # Override Parent Constructor

    def makeSound(self):  # Override Parent Method
        print("Scream")


bat = Bat()
bat.fly()
bat.makeSound()