from Szek import Szek


def peldanyositas():
    peldany1 = Szek("kék", 13)
    peldany2 = Szek("piros", 4)
    peldany3 = Szek("zöld", 5)
    szekek = [peldany1, peldany2, peldany3]
    return szekek

def listakiiras(atvevendoLista):
    for index in range(0, len(atvevendoLista), 1):
        print(atvevendoLista[index])
# rövid verzió
# listakiiras(peldanyositas())

# hosszú verzió:
szekekLista = peldanyositas()
listakiiras(szekekLista)

def osszegzesTetele(atvevendoLista):
    # összegzés tétel
    # sorozat - székek lista elemei
    # érték a lábak összege
    print("Összesen hány székláb van a teremben: ", end="")
    ossz=0
    for index in range(0, len(atvevendoLista),1):
        ossz += atvevendoLista[index].labszam
    print(f"{ossz}db")
osszegzesTetele(peldanyositas())


def maximumKivalasztas(atvevendoLista):
    # maximum kiválasztás
    maxLabIndex = 0
    for index in range(1, len(atvevendoLista), 1):
        if atvevendoLista[maxLabIndex].labszam > atvevendoLista[index].labszam:
            maxLabIndex=index
    print(f"A legtöbb lábú szék színe: {atvevendoLista[maxLabIndex].szin}")
    return maxLabIndex
maximumKivalasztas(peldanyositas())


def megszamlalasTetele(atvevendoLista):
    # megszámlálás
    db = 0
    print("Hány négynél több lábú szék van: ", end="")
    for index in range(0, len(atvevendoLista), 1):
        if atvevendoLista[index].labszam > 4:
            db += 1
    print(f"{db}db")
    return db
megszamlalasTetele(peldanyositas())


def eldontesTetele(atvevendoLista):
    print("Van piros színű, négy lábú szék: ", end="")
    van = False
    index = 0
    while (index < len(atvevendoLista)) and (van ==  False):
        if (atvevendoLista[index].szin == "piros") and (atvevendoLista[index].labszam == 4):
            van = True

        index += 1
    if van == True:
        print("van")
    else:
        print("nincs")

eldontesTetele(peldanyositas())

def beolvasas(atvevendoLista):
    veglegesLista = []
    beFajl = open("szekAdatok.txt", "r", encoding="utf-8")
    beFajl.readline()
    soraim = beFajl.readlines()
    for index in range(0, len(soraim), 1):
        daraboltTisztitott = soraim[index].strip().split("-")
        peldanyom =Szek(daraboltTisztitott[0], daraboltTisztitott[1])
        veglegesLista.append(peldanyom)
        print(veglegesLista[index])

beolvasas(peldanyositas())

