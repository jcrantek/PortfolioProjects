import xml.etree.ElementTree as ET

#!/usr/bin/env python

OSM_FILE = "nashville.osm"  # Replace this with your osm file
SAMPLE_FILE = "nashville_sample.osm"

k = 15 # Parameter: take every k-th top level element
def get_element(osm_file, tags=('node', 'way', 'relation')):
    context = iter(ET.iterparse(osm_file, events=('start', 'end')))
    _, root = next(context)
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            yield elem
            root.clear()
            
with open(SAMPLE_FILE, 'wb') as output:
    output.write(bytes('<?xml version="1.0" encoding="UTF-8"?>\n', encoding='utf-8'))
    output.write(bytes('<osm>\n  ', encoding = 'utf-8'))

    # Write every kth top level element
    for i, element in enumerate(get_element(OSM_FILE)):
        if i % k == 0:
            output.write(ET.tostring(element, encoding='utf-8'))

    output.write(bytes('</osm>', encoding = 'utf-8'))