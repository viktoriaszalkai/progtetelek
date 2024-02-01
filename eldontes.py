import math

n = int(input("n = "))
prim = bool
i = 0
if n < 2:
    prim = False
else:
    i = 2
    while i <= math.sqrt(n) and n % i != 0:
        i += 1
    prim = i > math.sqrt(n)
    if prim:
        print("prim")
    else:
        print("nem prim")


