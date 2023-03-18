arr=[3,4,2,6,7]
k=2
n=len(arr)
for i in range(0,k):
    x=arr[0]
    for j in range(0,n-1):
        arr[j]=arr[j+1]
    arr[n-1]=x
for i in range(n):
    print(arr[i],end=' ')