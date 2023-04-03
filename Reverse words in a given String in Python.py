def reverse(string):
    s=string.split()[::-1]
    l=[]
    for i in s:
        l.append(i)
    print(l)
string="good works return"
reverse(string)