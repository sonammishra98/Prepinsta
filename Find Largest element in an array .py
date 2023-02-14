a=[2,5,6,7,8,24]
max=a[0]
for i in range(len(a)):
    if max < a[i]:
        max=a[i]
print(max,"is the largest element in given array")