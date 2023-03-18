lst1=[2,2,2,3,4,5,6,7,4,3]
count=0
key=int(input("enter element to count the occurence : "))
for i in range(len(lst1)):
    if lst1[i]==key:
        count=count+1
print("ocurence :",count)
