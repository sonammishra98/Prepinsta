def bubblesort(arr,n):
    for i in range(n-1):
     for j in range(0,n-i-1):
        if arr[j] > arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
     return arr
arr=[2,3,9,5,7,89,34]
n=len(arr)
print(bubblesort(arr,n))