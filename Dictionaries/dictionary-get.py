from itertools import count


counts = {'name': 0, 'a': 2, 'c': 3}
if 'name' in counts:
    x = counts['name']
else:
    x = 12
print(x)
x = counts.get('name', 0)
print(x)
# another
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqin', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0)+1
print(counts)
