# Demonstrate single and multiple inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

class Pet(Dog, Cat):
    pass

pet = Pet()
pet.speak()
pet.bark()
pet.meow()
