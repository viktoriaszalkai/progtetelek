vege = 0
db = 0
min = 2147483648


while (szam := int(input("szám: "))) != vege:
    if szam < min:
        min = szam
    db += 1
print(f"Az {db} számból a legkisebb: {min}")