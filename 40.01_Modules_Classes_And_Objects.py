import mystuff

mystuff.apple()
print(mystuff.tangerine)
print(mystuff.pears)

mystuff = {"apple": "I AM APPLES!"}
print(mystuff["apple"])


class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thoudsand years between"

    def apple(self):
        print("I  AM CLASSY APPLES!")
