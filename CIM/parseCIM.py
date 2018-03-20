import xml.etree.ElementTree as ET
tree = ET.parse('C:/Users/omahmed/Documents/mvp/server/hana/src/deloitte/innovation/ls/safety/models/common/cv_cim_core.calculationview')
root = tree.getroot()
calcViews = root.find('calculationViews')
nodeID = "id"
nodeType = "{http://www.w3.org/2001/XMLSchema-instance}type"
column = 'CASE_NBR'
props = {
    "projection": "Calculation:ProjectionView",
    "join": "Calculation:JoinView"
}
for child in calcViews:
    print(child.attrib[nodeID],"---", child.attrib[nodeType])
    if child.attrib[nodeType] == props["projection"]:
        viewAttributes = child.find("viewAttributes")
        for viewattr in viewAttributes: 
            if True or viewattr.attrib[nodeID] == column:
                print ("\t", viewattr.attrib[nodeID])
        inputs = child.findall('input')
        for inp in inputs:
            print(inp.attrib["node"])
            for mapping in inp:
                if True or mapping.attrib["target"] == column or mapping.attrib["source"] == column:
                    print ('\t',"target",mapping.attrib["target"], "-:-" ,"source",mapping.attrib["source"]) 
