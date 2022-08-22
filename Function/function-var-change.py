def change(value):
    value=2
def changeDic(value):
    value["name"]="r"
val=3
newValue={"name":"Raihan"}
change(val)
# dic is mutable
changeDic(newValue)
print(val)
print(newValue)