data = "From stephen.marquard@uct.ac.az Sat Jan 5 09:14:26 2008"
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1:sppos]
print(host)
