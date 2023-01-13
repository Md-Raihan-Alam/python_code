items=["Roger","Beaus","bob","Quency"]
itemsCopy=items
items.sort()
print(items)
# print by fixing lowercase
itemsCopy.sort(key=str.lower)
print(itemsCopy)
print(sorted(items)) # without chaning the original