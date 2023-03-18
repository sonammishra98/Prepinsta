l=[]
n=int(input("neter size: "))
for i in range(0,n):
    key=int(input("enter no.: "))
    l.append(key)
l.sort()
print("3 max is:",[l[n-1],l[n-2],l[n-3]])