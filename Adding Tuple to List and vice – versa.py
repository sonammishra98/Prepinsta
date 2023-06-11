lst=[3,5,7]
t=(9,10)
lst += t
print(str(lst))
#add lst to tpl
res=tuple(list(t) + lst)
print(str(res))
