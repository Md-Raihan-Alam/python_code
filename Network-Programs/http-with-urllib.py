import urllib.request
import urllib.parse
import urllib.error
browserHand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in browserHand:
    newLine = line.decode().rstrip()
    print(newLine)
