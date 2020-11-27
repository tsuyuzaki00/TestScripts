import json
from collections import OrderedDict as od
import pprint

#filePass = 'C:/Users/tsuyuzaki.tatsuya/Desktop/test/output.json'
filePass = 'testScripts\jsonRun.json'

def testWriteJson():
    s = {"object": { "node" : [{ "name" : "pCube", "attrbute": [ {"string": "rotateX", "value": "0.0"},{"string": "rotateY", "value": "0.0"},{"string": "rotateZ", "value": "0.0"} ]}]}}
    with open(filePass, 'w') as f:
        json.dump(s, f, indent = 4, ensure_ascii =False)

def testReadJson():
    with open(filePass, 'r') as f:
        root = json.load(f)
        #pprint.pprint(root, width=40)
        node = root['object']['node']
        for attr in node:
            attr2 = attr['attrbute']
            for string in attr2:
                print attr.get('name')
                print string.get('string')
                print string.get('value')

#testWriteJson()
testReadJson()