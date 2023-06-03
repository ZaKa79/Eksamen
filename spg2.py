from datetime import datetime
from time import sleep

l = []
d = {}

def c(b, tp=10):
    t = b*(1+0.1 * tp)
    t = round(t,2)
    print(f"t ={t}")
    return t

for i in range(1, 4):
    l.append(c(i+0.334546))
    print(l, "\n", i, "\n")
    for j in range(1, 4):
        d[str(datetime.now())] = 1
        print("j", j, "\n", d)
        sleep(0.1)
