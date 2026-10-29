class Demo:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

    def __del__(self):
        print("Object deleted:", self.name)


a = Demo("A")
b = Demo("B")
c = Demo("C")

a.display()
b.display()
c.display()

del a
del b
del c
