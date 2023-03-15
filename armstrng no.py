num=int(input())
temp=num
order=len(str(num))
sum=0
while num > 0:
    digit=num %10
    sum=sum+digit ** order
    num=num//10
if sum==temp:
    print("armstrong")
else:
    print("not armstrng")