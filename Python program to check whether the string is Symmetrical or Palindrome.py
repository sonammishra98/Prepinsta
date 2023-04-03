def palindrome_symmetrical(string):
  half=int(len(string)/2)
  str_first=string[half:]
  str_sec=string[:half]
  if str_first==str_sec:
    print("symmetrical and ")
  else:
    print("not symmetrical")
  rev=string[::-1]
  if string==rev:
    print("palindrome")
  else:print("not palindrome")
string="amaamaaa"
palindrome_symmetrical(string)