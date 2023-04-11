def selectionsort(array):
    for i in range(0,len(array)-1):
        for j in range (i+1,len(array)):
           if array[i] > array[j]:
             temp=array[i]
             array[i]=array[j]
             array[j]=temp
    return array
array=[-2, 45, 0, 11, -9,88,-97,-202,747]
print(selectionsort(array))