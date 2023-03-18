arr=[6,5,4,4]
x,y=[],[]
x.extend(arr)
y.extend(arr)
x.sort()
y.sort(reverse=True)
for i in range(len(arr)):
  if (arr==x) or (arr==y):
    print("montomanic")
print("not montomanic")