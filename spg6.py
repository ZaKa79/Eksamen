class p(object):
    def x(self, n):
        return n * 2
    def y(self):
        print("Parent y")
    def z(self, foo : str = "not given" , bar: int = 999):
        return f"{foo} \n {chr(bar)}"
    
class c(p):
    def x(self, n):
        return n / 2
    def y(self):
        print(self.x(15))
        super(c, self).y()
        print ("super duper")

d = p()
s = c()
d.y()
s.y()
d.x(10)
s.x(20)
print(d.z("char enc:", 127773))
print(s.z("nember ?? is:", 127774))