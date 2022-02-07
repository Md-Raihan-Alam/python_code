import urllib.request
import urllib.parse
import urllib.error
webFile = urllib.request.urlopen('https://www.dr-chuck.com/page1.htm')
for line in webFile:
    currentLine = line.decode().rstrip()
    print(currentLine)
