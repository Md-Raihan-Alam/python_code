# Creates a sorted dictionary (sorted by key)
from collections import OrderedDict

dict = {'ravi': 10, 'rajnish': 9,
		'sanjeev': 15, 'yash': 2, 'suraj': 32}
print(dict)

sorted_value_index = np.argsort(dict.values())
dictionary_keys = list(dict.keys())
sorted_dict = {dictionary_keys[i]: sorted(
	dict.values())[i] for i in range(len(dictionary_keys))}

print(sorted_dict)
