a = int(input("Első szám: "))
b = int(input("Második szám: "))
y = 0

for element in range(a,b,1):
    if element % 3 == 0:
        y = y + 1

print (y, "db 3-al osztható szám van",a,"és",b,"számok között")
