l=[]
n=int(input("neter size: "))
for i in range(0,n):
    key=int(input("enter no.: "))
    l.append(key)
l.sort()
print("max no is: ",l[n-1])
print("2nd max is: ",l[n-2])