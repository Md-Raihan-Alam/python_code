myDict2=dict(name="Mary",age=26,city="Boston")
# one way
if "name" in myDict2:
    print(myDict2["name"])
# two way
try:
    print(myDict2('age'))
except:
    print("Error")