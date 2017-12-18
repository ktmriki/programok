i = int(input("Mekkora alapú legyen: "))
x = 1

for a in range(0, i - 1):
    y = i - 2
    print(" " * y, "*" * x)
    i = i - 1
    x = x + 2
