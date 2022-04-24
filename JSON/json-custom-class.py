import json
# 1st Method
class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

user=User("Max",27)

def encode_user(o):
    if isinstance(o,User):
        return {'name':o.name,'age':o.age,o.__class__.__name__:True}
    else:
        raise TypeError('Objecct of type User is not JSON serialiable')

# 2nd method

from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self,o):
        if isinstance(o,User):
            return {'name':o.name,'age':o.age,o.__class__.__name__:True}
        return JSONEncoder.default(self,o)
# userJSON=json.dumps(user,default=encode_user)
# userJSON=json.dumps(user,cls=UserEncoder)

# 3rd method
userJSON=UserEncoder().encode(user)
print(userJSON)