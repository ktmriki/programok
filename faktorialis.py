n = int(input("Szám: "))
x = 1
y = 1

if n == 0:
	print ("A megadott szám faktoriális értéke 0")

for y in range(1,n + 1):
	x = x * y

print ("A megadott szám faktoriális értéke ", x)