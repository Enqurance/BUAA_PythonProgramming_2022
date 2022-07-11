import random


class Animal:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.__age = age

    def getAge(self):
        return self.__age


class Dog(Animal):
    def bark(self):
        print(self.name + " : Wof wof wof...")

    def printAge(self):
        print(self.name + "'s age is " + str(self.getAge()))


if __name__ == "__main__":
    a = Animal("Random Name", "Random Breed", random.randint(1, 10))
    print(a.name)
    print(a.breed)
    dog_1 = Dog("John", "Kerky", 5)
    dog_1.bark()
    dog_1.printAge()
