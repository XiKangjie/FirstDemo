from lxml import etree

# create the root element
page = etree.Element('html')
# make a new document tree
doc = etree.ElementTree(page)
# add child elements
headElt = etree.SubElement(page, 'head')
bodyElt = etree.SubElement(page, 'body')
# and text
title = etree.SubElement(headElt, 'title')
title.text = 'Your page title here'
# and attributes
linkElt = etree.SubElement(headElt, 'link', 
        rel = 'stylesheet', href = 'mystyle.css', type = 'text/css')
# add two same child elements
etree.SubElement(bodyElt, 'p').text = 'this is first paragraph'
etree.SubElement(bodyElt, 'p').text = 'this is second paragraph'
# add a empty element
etree.SubElement(page, 'foot')
# write to a file
outFile = open('home.xml', 'w')
doc.write(outFile, pretty_print = True)
