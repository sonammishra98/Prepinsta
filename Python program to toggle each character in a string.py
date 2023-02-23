string="SonAmMishRa"
string1=str()
for i in string:
    if i.isupper():
        i=i.lower()
        string1=string1+i
    else:
        i.upper()
        string1=string1+i
print(string +" after change "+ string1)
