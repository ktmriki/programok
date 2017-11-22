import random

A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
random.shuffle(A)
print(A, "- Starting list")
sorted = False

if sorted == False:
  sorted = True
  for passnum in range(len(A)-1,0,-1):
    for i in range(passnum):
      if A[i] > A[i+1]:
        sorted = False
        temp = A[i]
        A[i] = A[i+1]
        A[i+1] = temp
        print(A)
        
print(A, "- Sorted list")
