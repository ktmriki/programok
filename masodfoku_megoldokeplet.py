a = float(input("x2: "))
b = float(input("x: "))
c = float(input("konstans: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Az egyenletnek végtelen sok megoldása van (azonosság).")

        else:
            print("Az egyenletnek nincs megoldása (csak konstans).")

    else:
        print("Elsőfokú az egyenlet, a megoldása: ", -c/b)

else:
    if b == 0:
        if c == 0:
           print("Az egyenletnek nincs megoldása.")

        else:
            print("A megoldás: ", -c ** 0.5)

    else:
        if c == 0:
            print("Az egyenletnek nincs megoldása (nincs konstans).")

        else:
            if (b ** 2 - 4*a*c) < 0:
                print("Az egyenletnek nincs valós gyöke.")

            else:
                print("Az egyik megoldás: ", round((-b+((b*b-4*a*c) ** 0.5)) / (2*a), 2))
                print("A másik megoldás: ", round((-b-((b*b-4*a*c) ** 0.5)) / (2*a), 2))
    
