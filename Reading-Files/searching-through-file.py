fHand = open("Sample.txt", "r")
for i in fHand:
    i = i.rstrip()
    if i.startswith("Email"):
        print(i)
