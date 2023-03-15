def non_rep(arr,n):
    visited=[False for i in range (n)]
    for i in range(n):
        if visited==True:
            continue
    count=1
    for j in range(i+1,n,1):
        if arr[i]==arr[j]:
            visited[j]=True
            count=count+1
    if count==1:
        print(arr[i])
arr=[23,2,45,45,10,20,20,30]
n=len(arr)
non_rep=(arr,n)