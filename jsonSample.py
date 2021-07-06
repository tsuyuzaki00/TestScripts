import json
from collections import OrderedDict as od
import pprint

#filePass = 'C:/Users/tsuyuzaki.tatsuya/Desktop/test/output.json'
filePass = 'testScripts/jsonRun.json'

def test_write_json():
    s =  {'name' : 'joint1', 'pos' : 'C', 'node': 'geo', 'num': str(1)}
    #s = {"object": { "node" : [{ "name" : "pCube", "attrbute": [ {"string": "rotateX", "value": "0.0"},{"string": "rotateY", "value": "0.0"},{"string": "rotateZ", "value": "0.0"} ]}]}}
    with open(filePass, 'w') as f:
        json.dump(s, f, indent = 4, ensure_ascii =False)

def test_read_json():
    with open(filePass, 'r') as f:
        roots = json.load(f)
        for root in roots:
            print (root)
            print (root['name'])
            #pprint.pprint(root, width=40)
            #name = root['body']['name']

#test_write_json()
test_read_json()