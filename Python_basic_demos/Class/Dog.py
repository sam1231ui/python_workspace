class Dog:
    name = "pug"

    def __init__(self, name):
        self.name = name


marshal = Dog("oreo")

tom = Dog("tommy")

# original
print(marshal.__class__.name)
# marshal passed name
print(marshal.name)
# tom passed name
print(tom.name)
