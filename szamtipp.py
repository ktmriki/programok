import random

x = int(random.randint(0, 100))

print("Egy véletlen számot kell kitalálnod 0 és 100 között.")
y = int(input("Tipped: "))

while x != y:
    if x > y:
        print()
        print("A tipped kisebb a számnál.")
        print()
        y = int(input("Új tipped: "))

    elif x < y:
        print()
        print("A tipped nagyobb a számnál.")
        print()
        y = int(input("Új tipped: "))

print ("Eltaláltad a számot!")
