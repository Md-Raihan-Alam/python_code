myList=["banana","cherry","apple"]
# list_cpy=myList will affect all of one is changed
# better way
list_copy=myList.copy()
list_copy_two=list(myList) # also possible
list_copy_three=myList[:] # also possible
print(list_copy)