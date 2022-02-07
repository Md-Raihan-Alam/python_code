import re
x = "From: Using the :character"
y = re.findall("^F.+:", x)  # take until the last :
print(y)
z = re.findall("^F.+?:", x)  # take until the first :
print(z)
