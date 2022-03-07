# Python code to sort the tuples using second element 
# of sublist Inplace way to sort using sort()
def Sort(sub_li):
  
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of 
    # sublist lambda has been used
    sub_li.sort(key = lambda x: x[1])
    return sub_li
  
# Driver Code
sub_li =[['a', 10], ['b', 5], ['c', 20], ['d', 15]]
print(Sort(sub_li))