fHand = input("Enter file Name:")
try:
    fOpen = open(fHand, "r")
    print(fOpen)
except:
    print("File"+fHand+" is missing")
