import re
test_string="123abc54343242abc543ABC"
pattern=re.compile(r"abc")
matches=pattern.finditer(test_string)
for match in matches:
    print(match.group()) #if you just want to string