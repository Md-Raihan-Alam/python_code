# Comparison operators is same but identical '===' is missing
data = input("Enter a real number:")
num = int(data)
if num == 5:
    print("Equal 5")
if num >= 6:
    print("Greater than 5")
if num <= 4:
    print("Lesser than 5")
if num != 6:
    print("User didn't enter 6")
else:
    print("User enter some number")
