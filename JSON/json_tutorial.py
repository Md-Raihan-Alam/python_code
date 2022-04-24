import json
# // https://www.python-engineer.com/courses/advancedpython/11-json/
person={"name":"John","age":30,"city":"New York","hasChildren":False,"titles":["engineer"]}
# personJSON=json.dumps(person)
# personJSON=json.dumps(person,indent=4,separators=('; ','= '))
personJSON=json.dumps(person,indent=4,sort_keys=True)
print(personJSON)
with open('person.json','w') as file:
    # json.dump(person,file)
    json.dump(person,file,indent=4)