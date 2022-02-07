import re
x = "From stephen.marquare@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('\S+@\S+', x)
print(y)
z = re.findall("^From (\S+@\S+)", x)
print(z)
m = re.findall("@([^ ]*)", x)
print(m)
