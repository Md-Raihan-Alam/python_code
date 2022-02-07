# initialize
purse = dict()
# [key]=value
purse['money'] = 2000
purse['candy'] = 3
purse['tissue'] = 75
print(purse)
# call by key
print(purse['candy'])
# increament
purse['candy'] = purse['candy']+2
# overwrite
purse['money'] = 3000
print(purse)
