from collections import Counter
string="helloworld"
result=""
#for i in string:
    #result=string.count(i)
    #print(str(i)+":"+str(result))
result=Counter(string)
print(result)