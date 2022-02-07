import re
x = input("Enter any sentence with number:")
y = re.findall('[0-9]+', x)
print(y)
