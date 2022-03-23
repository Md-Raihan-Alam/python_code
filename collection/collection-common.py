from collections import Counter
a="aaaaabbbbbcccc"
my_counter=Counter(a)
print(my_counter.most_common(1)) # (N)=> HOW MANY
print(my_counter.most_common(1)[0])
print(my_counter.most_common(1)[0][0])
print(my_counter.most_common(1)[0][1])