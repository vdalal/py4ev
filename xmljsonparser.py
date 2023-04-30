# https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody
# www.py4e.org

# web services (chapter 13)
import xml.etree.ElementTree as ET
data = '''<person>
            <name>Chuck</name>
            <phone type="intl">
                +1 734 303 4456
                </phone>
                <email hide="yes"/>
        </person>
        '''

tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)
print('Attrib: ', tree.find('email').get('hide'))


# import xml.etree.ElementTree as ET
#input = '''<stuff>
#                <users>
#                    <user x="2">
#                        <id>001</id>
#                        <name>Chuck</name>
#                    </user>
#                   <user x="7">
#                        <id>009</id>
#                        <name>Alice</name>
#                    </user>
#                </users>
#        </stuff>'''

#stuff = ET.fromstring(input)
#lst = stuff.findall('users/user')
#print('User count:', len(lst))
#for item in lst:
#    print('Name: ', item.find('name').text)
#    print('Id: ', item.find('id').text)
#    print('Attribute: ', item.get('x'))

import json
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 714 123 4567"
        },
        "email" : {
            "hide" : "yes"
        }
    }'''

info = json.loads(data)
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])
print('Email:',info["email"])

#import json
#input = '''[
#    { "id" : "001",
#      "x" : "2",
#      "name" : "Chuck"
#    } ,
#    { "id" : "009",
#      "x" : "7",
#      "name" : "chuck"
#    }
#]'''

#info = json.loads(data)
#print('User count:', len(info))
#for item in info:
#    print('Name',item['name'])
#    print('Id',item['id'])
#    print('Attribute',item['x'])