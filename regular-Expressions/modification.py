import re
testString="123abc456789abc123ABC"
pattern=re.compile(r"abc")
#split
splitted=pattern.split(testString)
print(splitted)
#sub
testStringTwo="Hello world, What a wonderful day in this world"
patternTwo=re.compile(r"world")
subbed_string=patternTwo.sub("planet",testStringTwo)
print(subbed_string)