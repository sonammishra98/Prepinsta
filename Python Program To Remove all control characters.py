string="Geeks\0\r for \n\bge\tee\0ks\f"
for i in string:
    if i in ("\n \0 \f \r \b \t"):
        string.replace(i," ")
print(string)