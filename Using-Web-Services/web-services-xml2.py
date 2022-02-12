import xml.etree.ElementTree as ET
tree = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Raihan</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Alcurd</name>
        </user>
    </users>
</stuff>
'''
stuff = ET.fromstring(tree)
lst = stuff.findall('users/user')
print("User count=", len(lst))
for item in lst:
    print("Name", item.find('name').text)
    print('Id=', item.find('id').text)
    print("Attribute=", item.get("x"))
