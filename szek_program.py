from Szek import Szek

peldany1 = Szek("kék", 3)
peldany2 = Szek("piros", 4)
peldany3 = Szek("zöld", 5)

print(peldany1.__str__())
print(peldany2.__str__())
print(peldany3.__str__())

szekek=[peldany1, peldany2, peldany3]

def labakSzama():
    print("Összesen hány székláb van a teremben: ", end="")
    ossz=0
    for index in range(0, len(szekek),1):
        ossz += szekek[index].labszam
    print(f"{ossz} db")

labakSzama()

def maxLabSzine():
    maxLabIndex = 0
    for index in range(1, len(szekek), 1):
        if szekek[maxLabIndex].labszam > szekek[index].labszam:
            maxLabIndex=index
    return szekek[maxLabIndex].szin

print(f"A legtöbb lábú szék színe: {maxLabSzine()}")
