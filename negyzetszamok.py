i = int(input("Hány négyzetszámot: "))
x = []

if i == 0:
    print("Ennél nagyobb számot adj meg!")

else:
    if len(x) < i:
        for a in range(0, 99999999999999):
            if (a * a) % 1 == 0 and len(x) < i:
                x.append(a * a)
                print(x)

            else:
                break

