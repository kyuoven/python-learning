class Animal:
    def __init__(self, name, color=None):
        self.name = name
        self.color = color
        self.animal = None


class Dog(Animal):
    def __init__(self, name, color=None):
        super().__init__(name, color)
        self.animal = "dog"


class Pompompurin(Animal):
    def __init__(self, name):
        super().__init__(name, "yellow")
        self.animal = "pudding dog"


animals = {
    "dog": Dog("cactus"),  # key : value
    "pompompurin": Pompompurin("PP"),
}

for key, value in animals.items():
    print(f"key: {key}")
    print(f"name: {value.name}")
    print(f"animal: {value.animal}")
    print(f"color: {value.color}")
    print("/////////////////////////")
