setA={1,2,3,4,5,6,7,8,9}
setB={1,2,3,10,11,12}
diff=setB.symmetric_difference(setA) # missing in both sets
print(diff)
diffTwo=setA.symmetric_difference(setB)
print(diffTwo)