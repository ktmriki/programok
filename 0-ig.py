n = int(input("Szám: "))
x = []
y = int(0)
z = int(0)
zs = int(0)

while n != 0:                       #A számok listája
    x.append(n)
    n = int(input("Szám: "))

x.append(0)

print ("A számok listája: ",x)

for element in list(x):             #A számok összege
    y = y + element

print ("A számok összege: ",y)

for element in list(x):
    if element > 0:
        z = z + 1

print ("A pozitív számok száma: ",z)

for element in list(x):
    if element < 0:
        zs = zs + 1

print ("A negatív számok száma: ",zs)

