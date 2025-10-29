class Dog:
    # hardcoded variable for all dogs
    treat = False

    # init parameters allow for different values for each new instance
    def __init__(self, name):
        self.name = name
        self.setValues()

    # function to hardcode object attributes
    def setValues(self):
        self.age = 3
        self.breed = "Bully"

    def bark(self):
        print("woof")

    def sit(self):
        print(f"{self.name} the {self.age} year old {self.breed} is sitting")

new_dog = Dog("Barney")

new_dog.bark()

new_dog.sit()

print(new_dog.treat)

if new_dog.name == "Barney":
    print("Hello")
