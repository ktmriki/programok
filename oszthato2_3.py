n = int(input("Szám: "))
x = 0
y = 0
element = 1

if n % 3 == 0 and n % 2 == 0:
    print ("A szám 3-al és 2-vel is osztható")

else:
    for element in range(1,n + 1):
        if element % 3 == 0:
            x = x + element

    for element in range(1,n + 1):
        if element % 2 == 0:
            y = y + element

    print ("Az eredmény: ",x+y)
