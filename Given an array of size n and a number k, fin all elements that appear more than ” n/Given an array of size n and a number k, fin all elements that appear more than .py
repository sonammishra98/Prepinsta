arr=[4,4,4,5,5,2,5]
n=7; k =2
x=n/k
l=[]
for i in range(len(arr)):
    if arr.count(i) > x:
        l.append(i)
print(l)