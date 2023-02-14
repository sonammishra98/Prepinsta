def disjoint(set1,set2,m,n):
 set1.sort()
 set2.sort()
 i=0
 j=0
 while(i<m and j<n):
    if (set1[i] < set2[j]):
        i=i+1
    elif (set2[j] < set1[i]):
        j=j+1
    else:
        return False
 return True
arr1=[6,7,8,9,10]
arr2=[1,2,3,4,]
m=len(arr1)
n=len(arr2)
print("yes") if disjoint(arr1,arr2,m,n) else print("no")