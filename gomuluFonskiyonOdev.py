# HW1
print(list(map(lambda x: x[0] * x[1], [(3,4),(10,3),(5,6),(1,9)])))

print("") #Empty line

# HW2
import math

def tria(arg):
    firstOne = arg[0]
    secondOne = arg[1]
    thirdOne = arg[2]
    min = math.fabs(secondOne - firstOne)
    max = secondOne + firstOne
    if (thirdOne > min and thirdOne < max):
        return True
    else:
        return False

print(list(filter(tria,[(3,4,5),(6,8,10),(3,10,7)])))

print("") #Empty line

# HW3
from functools import reduce
def evenTest(arg):
    if arg % 2 == 0: return True
    else: return False

print(reduce(lambda x,y: x+y, list(filter(evenTest, [1,2,3,4,5,6,7,8,9,10]))))


print("") #Empty line

# HW4
names = list(zip(["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"],
["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]))
for i,j in names:
    print("Adı: {}\nSoyadı: {}\n".format(i, j), end="---------------\n")
