num=1234
rev=0
while num > 0:
  rev=(rev*10) + num%10
  num1=rev
if num1==num:
  print("palindrome")
else:
  print("not palindrome")