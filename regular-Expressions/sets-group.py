import re
myString="""
hello world
12323
2020-05-20
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T
pythonengineer@gmail.com
Python-engineer@gmx.de
python-engineer123@my-domain.org
"""
pattern=re.compile(r"([a-zA-Z0-9-]+)@([a-zA-Z-]+)\.([a-zA-Z]+)") # sets [] group ()
matches=pattern.finditer(myString)
for match in matches:
    print(match.group()) # default 0
    print(match.group(1))
    # print(match.group(2))