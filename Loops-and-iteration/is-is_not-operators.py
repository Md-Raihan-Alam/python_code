# "is" and "is not" operators are not recommended
x=5
if x is 5:# is means as same as or "=="
    print("x value is 5")
if x is not 6:#is not means as not same as or "!="
    print("x value is not 6")
#another example
smallest=None
for value in [3,41,12,9,74,15]:
    if smallest is None:
        smallest=value
    elif smallest<value:
        smallest=value
print(smallest)
