class Flower:
    def __init__(self, name, color, height, smell):
        self.type = type(self).__name__
        self.name = name
        self.color = color
        self.height = height
        self.smell = smell

    def water(self):
        ...

    @property
    def short_story(self):
        return (
            f"{self.type} - {self.name} - {self.color} - {self.height} - {self.smell}"
        )


class Cherry_Blossom(Flower):
    def __init__(self, name):
        super().__init__(name, "pink", "2 cm", "Soapy")


class Tulip(Flower):
    def __init__(self, name, color):
        super().__init__(name, color, "1 cm", "Grassy")


class Rose(Flower):
    def __init__(self, name, color):
        super().__init__(name, color, "0 cm", "Sweet")


if __name__ == "__main__":
    flowers = [
        Cherry_Blossom("Pompompurin"),
        Tulip("My Melody", "Pink"),
        Rose("Hello Kitty", "Red"),
    ]
    for flower in flowers:
        print(flower.short_story)
