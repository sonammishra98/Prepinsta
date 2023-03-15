#for cheaking singl element

#l=[]
#n=int(input("enter size"))
#for i in range (0,n):
   # key=int(input("enter the element"))
   # l.append(key)
#g=0
#for i in range(len(l)):
 #if l.count(i) > 1:
    #g=g+i
#print(i,"having the count more than 1")

def non_rep(arr,n):
    visited=[False for i in range (n)]
    for i in range(n):
        if (visited[i]==True):
            continue
        count=1
        for j in range(i+1,n,1):
          if (arr[i]==arr[j]):
            visited[j]=True
            count=count+1
        if count != 1:
          print(arr[i],"having the more than 1")
arr=[23,2,45,45,10,20,20,30]
n=len(arr)
non_rep=(arr,n)