import math
def osztok(osztando):
    osztokListaja = []
    for oszto in range(2, int(math.sqrt(osztando)+1)):
        if osztando % oszto == 0:
            osztokListaja.append(oszto)
    return osztokListaja


def kiiratas(osztokListaja):
    print(osztokListaja, end="")
kiiratas(osztok(10007))

"""
HA MINDEN OSZTÓJÁRA ,IVÁNCSIAK VAGYUNK!!!!
def osztok(osztando):
    for oszto in range(1, osztando+1):
        if osztando % oszto == 0:
            print(oszto)
osztok(36)

"""

"""
WHILE
def osztok(osztando):
    osztokListaja = []
    oszto = 2
    while oszto <= math.sqrt(osztando):
        if osztando % oszto == 0:
            osztokListaja.append(oszto)
        oszto += 1
    return oszto
osztok(25)
"""