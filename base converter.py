i = str(input("Szám: "))
x = int(input("Számrendszer: "))
y = 0

while True:
    y = y + 1
    z = str(y)
    if int(i, x) == int(z, 10):
        print("A szám:", z)
