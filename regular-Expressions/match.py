import re
test_string="123abc54343242abc543ABC"
pattern=re.compile(r"abc")
pattern2=re.compile(r"123")
matches=pattern.match(test_string)
matchesTwo=pattern2.match(test_string)
print(matches)
print(matchesTwo)