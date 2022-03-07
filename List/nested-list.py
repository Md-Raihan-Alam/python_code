nested_list = [['blue', 'green'], ['red', 'black'], ['blue', 'white']]
print(len(nested_list))
# prints 3
print(nested_list[1])
# prints ['red', 'black']
print(nested_list[1][0])
# prints red
for inner in nested_list:
    for value in inner:
        print(value)