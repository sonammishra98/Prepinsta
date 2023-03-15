arr=[4,5,6,3,9,90]
arr2=[89,34,67,23]
arr.sort()
arr2.sort()
n=len(arr)
product=0
for i in range(n):
    product=product+arr[i]*arr2[i]
    print(product)
    