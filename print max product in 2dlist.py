list=[[1,2,3],[4,5,6],[7,8,9]]

l=[]
for i in list:
    mul=1
    for x in i:
        mul=mul*x
    l.append(mul)
print(l)
max=l[0]
for j in range(len(l)):
   if l[j] > max:
       max=l[j]
print(max)