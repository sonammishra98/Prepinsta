def find(arr):
    p=0
    b=0
    for i in range(0,len(arr)):
        if b==1:
            b -= 1
        elif (arr[i] < 0):
                c=arr[i]
                arr[i]=arr[p]
                arr[p]=c
                if p > i:
                   b=b+1
                p=p+2
    return arr
arr=[ 7, 5, -2, 1, -3 ]
print(find(arr))

    