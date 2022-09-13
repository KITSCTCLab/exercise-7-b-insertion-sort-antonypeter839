from typing import List
def swap(arr,j,k):
  temp=arr[j]
  arr[j]=arr[k]
  arr[k]=temp
             
def insertionSort(array) -> List[int]:
  for i in range(0,len(array)-1):
    temp=i
    execution=0
    for j in range(i,-1,-1):
      if execution==0:
        if array[i]<array[j]:
          swap(array,i,j)
          execution=1
        else:
          array[j+1]=array[j]
  return array

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
