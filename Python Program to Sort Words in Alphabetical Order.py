string="i am a girl"
w=string.split()
for i in range(len(w)):
   w[i]=w[i].lower()
string=sorted(w)
print(" ".join(string))


