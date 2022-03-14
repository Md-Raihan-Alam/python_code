myDict2=dict(name="Mary",age=26,city="Boston")
# both will be effected if one is changed
myDict=myDict2
print(myDict)
myDict["email"]="maz@gamil.com"
print(myDict)
print(myDict2)
# better way
myDict_copy=myDict2.copy()
myDict_copy["sprit"]="water"
print(myDict2)
print(myDict_copy)
# another way
myDict_copy2=dict(myDict2)