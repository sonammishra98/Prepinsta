lst1=[3,4,5,6,12,10]
lst2=[3,4,5,11,12]
for i in range(len(lst1)):
    if i in lst2:
        lst1.remove(i)
print(lst1)