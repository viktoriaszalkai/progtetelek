import math
prim = False
n = 9999
while prim == False:
    n += 1
    i = 2
    while i<= math.sqrt(n) and n % i != 0:
        i += 1
    if i > math.sqrt(n):
        prim = True
print(n)