def insertionsort(arr,n):
    for i in range(1,n):
        t=arr[i]
        j=i-1
        while j >=0 and t < arr[j]:
           arr[j+1]=arr[j]
           j=j-1
        arr[j+1]=t
    return arr
arr=[4,3,9,2,5,6]
n=len(arr)
print(insertionsort(arr,n))
