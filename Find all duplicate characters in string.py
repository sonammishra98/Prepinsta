str="uncountable"
s=list(str)
x=[]
for i in str:
    if str.count(i) > 1:
      print(i,end=" ")