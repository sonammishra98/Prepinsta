#linear search 
def linearsearch(arr,key,n):
    flag=0
    for i in range(n):
        if arr[i]==key:
            flag=1
            pos=i+1
            break
    if flag==1:
        print("position",pos)
    else:
        print("element not found")
arr=[12,34,89,34,56,89,67]
key=int(input())
n=len(arr)
linearsearch(arr,key,n)

           