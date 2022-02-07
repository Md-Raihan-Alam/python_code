# try except used for error
# if try fails except work, if try works except ignore
astr="Hello Bob"
try:
    istr=int(astr)
    print("This got ignore because previous line is error")
except:
    istr=1
print("First :",istr)
astr='123'
try:
    istr=int(astr)
    print("It is working because previous line is not error")
except:
    istr=2
print("second :",istr)
# Second example
astr="Bob"
try:
    print("Hello")
    istr=int(astr)
    print("There")
except:
    istr=10
print("Done ",istr)
#final example
rawstr=input("Enter a number:")
try:
    ival=int(rawstr)
except:
    ival=-1
if ival!=-1:
    print("You have entered ",ival)
else:
    print("Not a number")
