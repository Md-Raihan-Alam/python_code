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
"""
pattern=re.compile(r"(Mr|Ms|Ms)\.?\s\w+") # condition |
matches=pattern.finditer(myString)
for match in matches:
    print(match.group())