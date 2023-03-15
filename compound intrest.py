p= 1200   # principal amount 
t= 2      # time 
r= 5.4    # rate 
# calculates the compound inte
a=p*(1+(r/100))**t  # formula for calculating amount 
ci=a-p  # compound interest = amount - principal amount
# printing compound interest value
print(ci)