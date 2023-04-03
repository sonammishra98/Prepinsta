#find mx sum from the subarray
def max_sum_subarray(arr,n):
  sum=-1
  max_so_far=arr[0]
  st=0 ;end=0; s=0
  for i,num in enumerate(arr):
    sum=sum+num
    if (sum < 0):
       sum=0
       s=i+1
    if (max_so_far < sum):
        max_so_far=sum
        st=s
        end=i
  print("Maximum sum Subarray is",max_so_far)
  print("Start Index of window is",st)
  print("End Index of window is",end) 

  
arr= [-1, 8, 1, -7, -1, 5, 1, -3]
n=len(arr)
max_sum_subarray(arr,n)