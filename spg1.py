class o(object):
    def ca(self, foo):
        print(f"val is {foo * 10}")
        return foo * 10
    def i(self):
        print(f"""{3 != 0.33 or 
        ("func1" != "func2" and True == True)}""")
    def a(self):
        print("What is this?")

class c(object):
    def __init__(self):
        self.o = o()
    def i(self):
        self.o.i()
    def ca(self, a):
        return a**2 % 10
    def a(self):
        print(f"r = {self.ca(34)}")
        self.o.a()
        print("Composition \n some stuff after self.o.a()")

son = c()
son.i()
print(son.ca(7))
son.a()