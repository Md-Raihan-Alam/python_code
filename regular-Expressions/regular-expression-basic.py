import re
hand = open("Sample.txt")
for line in hand:
    line = line.rstrip()
    if re.search('^Email:', line):
        print(line)
