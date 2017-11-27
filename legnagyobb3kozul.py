szam1 = int(input("Első szám: "))
szam2 = int(input("Második szám: "))
szam3 = int(input("Harmadik szám: "))

if szam1 > szam2 and szam1 > szam3:
    print("A legnagyobb szám: ", szam1)

elif szam2 > szam1 and szam2 > szam3:
    print("A legnagyobb szám: ", szam2)

else:
    print("A legnagyobb szám: ", szam3)
