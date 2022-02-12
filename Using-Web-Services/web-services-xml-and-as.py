import xml.etree.ElementTree as ET  # as gives shortcut form
data = '''
<person>
    <name>Raihan</name>
    <phone type="intl">
    01321814174
    </phone>
    <email hide="yes"/>
</person>
'''
tree = ET.fromstring(data)
print("Name:", tree.find('name').text)
print("Attr:", tree.find("email").get("hide"))
