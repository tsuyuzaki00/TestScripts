import json
from collections import OrderedDict as od
import pprint

s = r'{"C": "\u3042", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}'

print(s)

d = json.loads(s)

pprint.pprint(d, width=40)

print(type(d))



with open('testScripts/jsonRun.json') as f:
    df = json.load(f)

pprint.pprint(df, width=40)

print(type(df))


