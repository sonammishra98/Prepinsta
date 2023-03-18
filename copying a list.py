lst1=[2,3,4,5,6,7]
lst2=[]
for i in lst1:
    if i not in lst2:
        lst2.append(i)
print("before : ",lst1)
print("after :",lst2)