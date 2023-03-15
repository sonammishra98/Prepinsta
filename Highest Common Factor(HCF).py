num1=int(input())
num2=int(input())
if num1 > num2:
    min=num2
else:
    min=num1
for i in range(1,min+1):
    if i % num1==0 and i % num2==0:
      hcf=i
print(f"hcf is {hcf}")
