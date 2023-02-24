string="earth"
string2="heart"
string=sorted(string.lower())
string2=sorted(string2.lower())
for i in range(0,len(string)-0,len(string2)):
  if string[i]==string2[i]:
        print("yes,wrd is anagram")
  else:
        print("no,wrd isnt")
