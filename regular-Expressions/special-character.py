import re
test_string="hello 123_ heyhoo honey"
pattern=re.compile(r"[a-zA-Z]")
matches=pattern.finditer(test_string)
for match in matches:
    print(match.group())