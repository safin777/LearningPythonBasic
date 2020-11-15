import sys

A=[12,2,7,3,19,15]

for i in range (len(A)):
  min_index = i

  for j in range(i+1,len(A)):
    if A[min_index] > A[j]:
      min_index = j
  
  temp=A[i]
  A[i]= A[min_index]
  A[min_index]= temp

print("sorted element")
for i in range(len(A)):
  print("%d" %A[i])

