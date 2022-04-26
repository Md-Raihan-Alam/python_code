# use for pws or auth or account auth
# disadvantages takes time
import secrets
# Return a random int in the range [0, n).
a=secrets.randbelow(10)
print(a)
b=secrets.randbits(4)
# Return an int with k random bits.
print(b)
mylist=list('abcdefghij')
# Return a randomly-chosen element from a non-empty sequence.
c=secrets.choice(mylist)
print(c)