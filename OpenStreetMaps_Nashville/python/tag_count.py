import xml.etree.cElementTree as ET

def count_tags(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    tag_list = {}
    for row in root.iter():
        if row.tag not in tag_list:
            tag_list[row.tag] = 1
        else:
            tag_list[row.tag] +=1
    return tag_list