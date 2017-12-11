import random

x = int(random.randint(-50, 100))

i = 0 #Hány tipp volt eddig

print("Egy véletlen számot kell kitalálnod 0 és 100 között.")
y = int(input("Tipped: "))

while x != y:
    if x > y:
        print()
        print("A tipped kisebb a számnál. Tippelj nagyobbat.")
        print()
        y = int(input("Új tipped: "))

    elif x < y:
        print()
        print("A tipped nagyobb a számnál. Tippelj kisebbet.")
        print()
        y = int(input("Új tipped: "))

    i = i + 1

print()
print ("Eltaláltad a számot", i, "tippel.")
