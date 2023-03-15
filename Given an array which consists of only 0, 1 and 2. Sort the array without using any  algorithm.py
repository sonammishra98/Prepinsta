arr=[0,1,2,1,2,1,2,1,2,0,0,1,2]
count0=arr.count(0)
count1=arr.count(1)
count2=arr.count(2)
new_arr=[]
for i in range(count0):
    new_arr.append(0)
for i in range(count1):
    new_arr.append(1)
for i in range(count2):
    new_arr.append(2)
print(new_arr)