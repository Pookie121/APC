class Demo:
    def add(self, a, b=0):
        print(a + b)

d = Demo()
d.add(5)
d.add(5, 3)
