def algo(arr):
    max_so_far=arr[0]
    sum=-1;s=0
    for i,num in enumerate(arr):
        sum=sum+1
        if sum < 0:
            sum=0
            s=i+1
        if max_so_far < sum:
            max_so_far=sum
    print("max so far is:",max_so_far)
arr=[-2, -3, 4, -1, -2, 1, 5, -3]
algo(arr)