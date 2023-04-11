#Find duplicate in an array of N+1 Integers in Python
def find(arr):
    l=[]
    count=0
    for i in arr:
        if arr.count(i) > 1:
            count=count+1
            if i not in l:
              l.append(i)
    return l
arr=[1,2,1,2,3,4]
print(find(arr))