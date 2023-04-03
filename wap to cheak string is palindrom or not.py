def palindrome(str):
    rev=str[::-1]
    if str==rev:
        print("palindrome")
    else:
        print("not")
str="malayalam"
palindrome(str)