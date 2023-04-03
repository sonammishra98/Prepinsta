list=[23,45,90,45,78]
res=[]
for i in list:
  sum=0
  for digit in str(i):
    sum=sum+int(digit)
  res.append (sum)
print(res,end=" ")