def subset(arr1,arr2,m,n):
    i=0
    j=0
    for i in range(m):
        for j in range(n):
            if(arr2[j]==arr1[i]):
                break
        if(j==n):
            return 0
    return 1
arr1=[2,4,5,3,1,6,9,34,67,5,90,24,]
arr2=[3,4,5,6]
m=len(arr1)
n=len(arr2)
if(subset(arr1,arr2,m,n)): 
    print("arr2[]  is subset of arr1[]")
else:
    print("arr2[] is not subset of arr1[]")
    