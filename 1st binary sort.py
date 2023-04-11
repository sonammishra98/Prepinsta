#binary search in python    : recursive process
def binarysearch(arr,low,high,x):
    if high >=low:
        mid=(high+low)//2
        if arr[mid]==x:
          return mid
        elif arr[mid] > x:
          return binarysearch(arr,low,mid-1,x)
       
        else:
          return binarysearch(arr,mid+1,high,x)
    else:
       return -1
arr=[10,20,40,36,56]
x=int(input())
result=binarysearch(arr,0,len(arr)-1,x)
if result != -1:
   print("element is:",str(result))
else:
   print("element is not present")

    