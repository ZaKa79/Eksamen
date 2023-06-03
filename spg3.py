ucl = []
el = []
d = {"a" : "banana", "b":"apple", 
     "c":"orange", "d":"kiwi", "e":"lemon"}

for x in "abcde":
    ucl.append(d[x])

def e():
    for i in range(len(ucl)):
        a = ucl[i] [::-1]
        el.append(a)
    return el

def ue():
    for i in range(len(el)):
        a = el[i] [::-1]
        el[i] = a
    return el

class æ:
    def å(self, y, x):
        if d.get(y, 'Does Not Exist') == 'Does Not Exist':
            d[y] = str(x)

ins = æ()
ins.å("f", "coconut")
print(e())
print(ue())