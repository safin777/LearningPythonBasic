def bubbleSort(arr):
  n= len(arr)

  for i in range(n):
    for j in range(0,n-i-1):

      if arr[j] > arr[j+1]:
        temp=arr[j]
        arr[j]=arr[j+1]
        arr[j+1]=temp
arr = [12,6,3,9,4,1]
bubbleSort(arr)

print("Sorted array is:")

for i in range (len(arr)):
  print(arr[i])