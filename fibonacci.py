szam = int(input("Szám: "))
numbers = []

if szam == 0:
    print ("A számsorozat: ", numbers)

elif szam == 1:
    numbers.append(1)
    print ("A számsorozat: ", numbers)

else:
    numbers.append(1)
    numbers.append(1)
    for i in range(szam-2):
        numbers.append(numbers[i]+numbers[i+1])
        print (numbers)

