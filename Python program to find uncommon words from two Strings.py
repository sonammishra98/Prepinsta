string1="geeks for geeks"
string2="learning from geeks for geeks"
string1=string1.split() 
string2=string2.split()
x=[]
for i in string1:
    if i not in string2:
      x.append(i)
for i in string2:
    if i not in string1:
      x.append(i)
x=list(set(x))
print(x)
 