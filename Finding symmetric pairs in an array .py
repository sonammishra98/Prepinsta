def findpair(pairs):
    s=set()
    for (x,y) in pairs:
        s.add((x,y))
        if(y,x) in s:
            print(x,y)
pairs=[(2,3),(3,4),(4,3),(3,2),(5,6)]
findpair(pairs)