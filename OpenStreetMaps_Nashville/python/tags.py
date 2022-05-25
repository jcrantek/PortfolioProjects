#Count multiple patterns in the tags
import xml.etree.cElementTree as ET
import pprint
import re

#regular expressions
lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

#count the key types
def key_type(element, keys):
    if element.tag == "tag":
        if lower.search(element.attrib["k"]):
            keys["lower"] += 1
        elif lower_colon.search(element.attrib["k"]):
            keys["lower_colon"] += 1
        elif problemchars.search(element.attrib["k"]):
            keys["problemchars"] += 1
        else:
            keys["other"] +=1
        
    return keys

#locate the colon in the tag
def find_colon(element, c_list):
    if element.tag == 'tag':
        if lower_colon.search(element.attrib["k"]):
            if element.attrib["k"] not in c_list:
                c_list[element.attrib["k"]] = 1
            else:
                c_list[element.attrib["k"]] += 1
    return c_list

#save the tags into a couple of lists, one to count and one to list them all
def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    colon_list = {}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)
        colon_list = find_colon(element, colon_list)
    return keys, colon_list