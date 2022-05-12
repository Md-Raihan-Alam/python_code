def mygenerator():
    yield 1
    yield 2
    yield 3

g=mygenerator()
# might stop iteration if printed
# print(g)   
# for i in g:
#     print(i)

# gets value once at a time with next function
value=next(g)
print(value)
value=next(g)
print(value)
value=next(g)
print(value)
# more than limit will create stopiteration