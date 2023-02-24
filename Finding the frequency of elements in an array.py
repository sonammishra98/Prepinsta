arr=[8,4,3,4,5,2,8,9]
key=int(input("enter the key to find the frequency"))
count=0
for i in range(len(arr)):
   if arr[i]==key:
    count=count+1
    print("frequency=",count)