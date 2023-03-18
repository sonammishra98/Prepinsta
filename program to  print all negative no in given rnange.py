start=int(input("enter strting range: "))
end=int(input("enter ending range:"))
for i in range(start,end+1):
    if i < 0:
        print(i,end=" ")