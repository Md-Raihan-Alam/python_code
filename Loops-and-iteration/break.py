n=0
while n<=10:
    if n==5:
        break
    print(n)
    n=n+1
print("break stop the loop")
# another example
while True:
    line=input(">")
    if line=="done":
        break
    print(line)
print("'Done' has been typed")
