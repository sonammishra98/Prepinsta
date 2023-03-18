def swaplist(newlist):
    n=len(newlist)
    temp=newlist[0]
    newlist[0]=newlist[n-1]
    newlist[n-1]=temp
    return newlist
newlist=[4,3,2,51]
print(swaplist(newlist))
