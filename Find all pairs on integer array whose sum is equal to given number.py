def function(arr,n,k):
    for i in range(0,n):
        for j in range(i,n):
            if (arr[i]+arr[j])==k:
              print(arr[i],arr[j])
arr=[3,4,1,6,5,2,5,6,9,8]
n=len(arr)
k=7
function(arr,n,k)