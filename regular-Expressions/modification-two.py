import re
urls="""
http://pythonengineer.com
https://www.Python-engineer.com
http://www.python.com
"""
myString="Hello world"
pattern=re.compile(r"https?://(www\.)?([a-zA-Z-]+)(\.[a-zA-Z]+)")
matches=pattern.finditer(urls)
for match in matches:
    print(match)

subbed_urls=pattern.sub(r"\2\3",urls)
print(subbed_urls)
#compilation flags
newPattern=re.compile(r"world",re.IGNORECASE)
matches=newPattern.finditer(myString)
for match in matches:
    print(match.group())