class Bear:
    def nap(self):
        return ["zzz zzz"]


class Rilakkuma(Bear):
    def __init__(self, color):
        self.color = color

    def nap(self):
        return super().nap() + ["mi mi mi"]


rilakkuma = Rilakkuma("brown")
print(rilakkuma.color)
for message in rilakkuma.nap():
    print(message)
