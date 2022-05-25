import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

osmfile = "nashville_sample.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Circle", "Lane", 
            "Road", "Trail", "Parkway", "Expressway", "Highway", "Tunnel", "Park", "Plaza", "Pike", "Bridge", "School"]

# This will look for the values on the left and ultimately replace with those on the right
mapping = { "St": "Street",
            "St.": "Street",
            "Hwy": "Highway",
            "Hwy.": "Highway",
           #This should rename Rosa L Parks Blvd => Rosa L Parks Boulevard
            "Blvd": "Boulevard",
            "Blvd.": "Boulevard",
            "Rd.": "Road",
            "Rd": "Road",
            "Pkwy": "Parkway",
            "PKWY": "Parkway",
            "Ave": "Avenue",
            "Ave.": "Avenue",
            "S": "South",
            "N": "North",
            "W": "West",
            "E": "East",
            "S.": "South",
            "N.": "North",
            "W.": "West",
            "E.": "East",
            }


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for _, elem in ET.iterparse(osmfile):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                audit_street_type(street_types, tag.attrib['v'])
                    
    osm_file.close()
    return street_types

def update_name(name, mapping):
    m = street_type_re.search(name)
    fixed_name = name
    if m:
        # check if the street type is a key in the mapping dictionary:
        if m.group() in mapping.keys():
            fixed_street_type = mapping[m.group()]
            fixed_name = street_type_re.sub(fixed_street_type, name)
    return fixed_name

def test():
    st_types = audit(osmfile)
    #pprint.pprint(dict(st_types))

    for st_type, ways in st_types.items():
        for name in ways:
            if name == "Rosa L Parks Blvd":
                fixed_name = update_name(name, mapping)
                print(name, "=>", fixed_name)
            
if __name__ == '__main__':
    test()