import time

timeLeft = 3
l= ["Hello","this","is","some", "text"]

def main(a):
    """funktionen tager en åben textfil som parameter og printer 
    hver linje ved brug af rekursion.
    """

    line = a.readline()

    if line:
        print(line)
        return main(a)
    
def wl(a):
    """Itererer over input og skriver det til en tekstfil
    """
    for o in a:

        f.write(o + "\n")

    f.close()

f = open("test.txt", "w")

wl(l)
f = open("test.txt")
main(f)

while timeLeft > 0:

    print(timeLeft, end= " ")
    time.sleep(1)
    timeLeft = timeLeft - 1