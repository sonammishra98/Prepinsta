a=[34,34,35,56,78]
b=[78,98,78,34,23]
n=len(a)
a.sort()
b.sort(reverse=True)
product=0
for i in range(n):
 product =product + a[i]*b[i]
print(product)