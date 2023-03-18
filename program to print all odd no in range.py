start=int(input("starting range"))
end=int(input("ending range"))
for i in range(start,end+1):
    if i % 2!=0:
        print(i,end=" ")