#def swaaplist(newlist):
   # n=len(newlist)
    #newlist[0]=newlist[n-1]
    #newlist[n-1]=temp
    #temp1=newlist[1]
    #newlist[1]=newlist[n-2]
    #newlist[n-2]=temp1
    #return newlist
#newlist=[2,3,5,6]
#print(swaaplist(newlist))

def swaplist(list,pos1,pos2):
    list[pos1] ,list[pos2]= list[pos2],list[pos1]
    return list
list=[2,3,4,5]
pos=1,2

print(swaplist(list,pos1-1,pos2-1))