import json
data = '''
{
"name":"Raihan",
"Phone":{
    "type":"int1",
    "number":"01321814174"
    },
"email":{
    "hide":"yes"
    }
}
'''
info = json.loads(data)
print("Name=", info["name"])
print("Hide=", info["email"]["hide"])
