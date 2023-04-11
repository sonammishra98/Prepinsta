import re
string="iem is best 239905554 bst 456 in kol56kata"
for i in string:
    number=re.findall(r'[0-9]+',string)
    alpha=re.findall(r'[a-zA-Z]+',string)
print(number)
print(alpha)
       
