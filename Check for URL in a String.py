def find(string):
    x=string.split()
    l=[]
    for i in x:
        if i.startswith("https:") or i.startswith("http:"):
          l.append(i)
    return(l)
string="my profile : http://support.google.com/google-ads"
print("url",find(string))