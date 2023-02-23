exp=input()
str=""
ct=['{','}','[',']','(',')']
for i in range(len(exp)):
  if exp[i] not in ct:
    str=str+exp[i]
print(str)