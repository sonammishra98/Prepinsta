def find(n):
    ans=1
    while n > 1:
      ans=ans * n
      n=n-1
    return ans
n=5
print(find(n))