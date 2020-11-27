import xml.etree.ElementTree as ET

def writeXml(xmlRoot, path):
    import xml.dom.minidom as md
    encode = "utf-8"
    xmlFile = open(path, "w")
    document = md.parseString(ET.tostring(xmlRoot, encode))
    document.writexml(
        xmlFile,
        encoding = encode,
        newl = "\n",
        indent = "",
        addindent = "\t"
    )

inFile = 'testScripts\country_data.xml'

def testWriteXml():
    title = ET.Element('object')
    node = ET.SubElement(title, 'node', {'name':'pCube'})
    attribute = ET.SubElement(node, 'attribute', {'string' : 'rotateX', 'value' : '0.0'})
    attribute = ET.SubElement(node, 'attribute', {'string' : 'rotateY', 'value' : '0.0'})
    attribute = ET.SubElement(node, 'attribute', {'string' : 'rotateZ', 'value' : '0.0'})

    ET.dump(title)
    writeXml(title, 'D:/Maya/scripts/testScripts/xmlRun.xml')

def testReadXml():
    tree = ET.parse(inFile) 
    root = tree.getroot()

    for country in root:
        print country.attrib
        for neighbor in country:
            print neighbor.attrib

testWriteXml()
#testReadXml()