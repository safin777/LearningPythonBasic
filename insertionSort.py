def insertionSort(arr):
  n= len(arr)

  for i in range(0,n-1):
    indexMin = i
    for j in range (i+1,n):
      if arr[j]<arr[indexMin]:
        indexMin = j
    if indexMin != i:
        temp = arr[i]
        arr[i] = arr[indexMin]
        arr[indexMin] = temp

arr = [12,3,8,4,9,5,11,20,15]
insertionSort(arr)
print("the sorted list is:")
for i in range(len(arr)):
  print(arr[i])