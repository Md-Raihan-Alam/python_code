import re
hand = open("sample_three.txt")
for line in hand:
    line = line.rstrip()
    if re.search("^X.*", line):
        print(line)
