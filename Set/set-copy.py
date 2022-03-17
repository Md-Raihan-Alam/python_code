setA={1,2,3,4,5,6}
# will affect the original
setB=setA # wrong
# better way
setC=setA.copy()
setD=set(setA)