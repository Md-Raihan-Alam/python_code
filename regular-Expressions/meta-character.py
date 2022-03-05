import re
test_string="123abc54343242abc543ABC"
pattern=re.compile(r"ABC$")
matches=pattern.finditer(test_string)
for match in matches:
    print(match.group())