a=list(map(int,input().split()))
ans=[]
for i in a:
    if i <0:
        ans.append(i)
for i in a:
    if i ==0:
        ans.append(0)
for i in a:
    if i > 0:
        ans.append(i)
print(ans)
