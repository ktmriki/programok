import random

A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
done = []
random.shuffle(A)
print(A, "- Kezdeti tömb")
length = len(A)

while len(done) < length:
    done.append(min(A))
    A.remove(min(A))
    print(done)

print("A", done, "tömb a végső, rendezett tömb")
