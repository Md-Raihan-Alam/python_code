from collections import Counter
a="aaaaabbbbbcccc"
my_counter=Counter(a)
print(my_counter.elements())
print(list(my_counter.elements()))