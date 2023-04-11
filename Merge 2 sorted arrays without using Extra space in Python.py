def mergearray(arr1,arr2,n1,n2):
    for i in arr2:
        if i not in arr1:
            arr1.append(i)
    arr1.sort()
    arr2=arr1[len(arr1)-n2:]
    arr1=arr1[:len(arr1)-n2]
    print("array1",arr1 ,"\narray2",arr2)
arr1=[1, 2, 3, 5, 8, 9, 10, 13, 15, 20]
arr2=[2, 3, 8, 13]
mergearray(arr1,arr2,len(arr1),len(arr2))