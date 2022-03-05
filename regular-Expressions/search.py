import re
test_string="123abc54343242abc543ABC"
pattern=re.compile(r"abc")
matches=pattern.search(test_string)
print(matches)