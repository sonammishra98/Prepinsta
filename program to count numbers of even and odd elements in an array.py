arr=[23,24,25,26,27,28,40,12]
counteven=0
countodd=0
for i in range(len(arr)):
    if arr[i]%2==0:
        counteven+=1
    else:
        countodd+=1
print(counteven)
print(countodd)