string=input("enter character")
string1=""
vowel=["a","e","i","o","u"]
for i in range(len(string)):
    if string[i] not in vowel:
       string1=string1+string[i]
print(string1)
     
     