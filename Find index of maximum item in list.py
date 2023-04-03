l=[23,45,3,4,90]
max=l[0]
idx=0
for i in range(len(l)):
    if max < l[i]:
        max=l[i]
        idx=i
print(idx)