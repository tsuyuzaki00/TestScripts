import xml.etree.ElementTree as ET

def make_xml(dc):
    roots = ET.Element('root', {'ttl':'test_root'})
    p = ET.SubElement(roots, 'p1') 
    t = ET.SubElement(p, 'fld1', {'atr1':'1.1','atr2':'1.5'}) 
    t.text = dc["fld1"] 
    t = ET.SubElement(p, 'fld2', {'atr1':'2.2','atr2':'2.5'}) 
    t.text = dc["fld2"] 
    p = ET.SubElement(roots, 'p3') 
    t = ET.SubElement(p, 'fld3', {'atr1':'3.3','atr2':'3.5'}) 
    t.text = dc["fld3"] 

    ET.dump(roots)

    tree = ET.ElementTree(roots) 
    fl = 'testScripts/xmlRun.xml'  
    tree.write(fl)

    return fl 

def read_xml(fl):
    tree = ET.parse(fl) 
    root = tree.getroot() 

    for c1 in root:
        print(c1.tag)
        for c2 in c1:
            tg = c2.tag
            atr1 = c2.attrib.get("atr1") 
            atr2 = c2.attrib.get("atr2") 
            txt  = c2.text
            print(atr1,atr2,txt)


dc = {'fld1': 'test1', 'fld2': 'test2', 'fld3': 'test3'}

fl = make_xml(dc)                        
print( fl )

read_xml( fl )   