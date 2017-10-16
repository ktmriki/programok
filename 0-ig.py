n = int(input("Szám: "))                #Bemenet
x = []                                  #Lista
y = int(0)                              #Összeg
z = int(0)                              #Pozitív számok száma
zs = int(0)                             #Negatív számok száma

while n != 0:                           #A számok listája
    x.append(n)
    n = int(input("Szám: "))

x.append(0)

print ("A számok listája: ",x)

for element in list(x):                 #A számok összege
    y = y + element

print ("A számok összege: ",y)

for element in list(x):                 #A pozitív számok száma
    if element > 0:
        z = z + 1

print ("A pozitív számok száma: ",z)

for element in list(x):                 #A negatív számok száma
    if element < 0:
        zs = zs + 1

print ("A negatív számok száma: ",zs)
