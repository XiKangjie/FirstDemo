from lxml import etree

# get doc tree
doc = etree.parse('home.xml')
# get root element
root = doc.getroot()

print etree.tostring(root)
'''
<html>
  <head>
    <title>Your page title here</title>
    <link href="mystyle.css" rel="stylesheet" type="text/css"/>
  </head>
  <body>
    <p>this is first paragraph</p>
    <p>this is second paragraph</p>
  <body/>
  <foot/>
</html>
'''

# elements are a list
print len(root)
# 2

child = root[0]
print child.tag
# head

# node has no subnodes
print not root[-1]
# True

# node exists
print root[-1] is None
# False

print root[0].getnext().tag
# body

print root[1].getprevious().tag
# head

print child.getparent().tag
# html

# deprecated
for child in root.getchildren():
    print child.tag
# head
# body
# foot

for child in root:
    print child.tag
# head
# body
# foot

# find node's first child node
print len(root.find('head'))
2

for p in root.findall('body/p'):
    print p.text
# this is first paragraph
# this is second paragraph

# attributes are a dict 
link = root.find('head/link')
print link.keys()
# ['href', 'rel', 'type'] 
print link.items()
# [('href', 'mystyle.css'), ('rel', 'stylesheet'), ('type', 'text/css')]
print link.get('type')
# text/css
print link.attrib['type']
# text/css

# find the text inside a specific element
print root.findtext('body/p')
# this is first paragraph

# xpath expression
# find an Element anywhere in the tree
# (when searching on individual elements, the path must not start with a slash.
# you can add a leading period(.), if necessary)
print root.find('.//p').text
# this is first paragraph

print doc.find('//p').text
# this is first paragraph

for p in root.xpath('//p'):
    print p.text
# this is first paragraph
# this is second paragraph


# (Note that the text, tail and children of an Element are not necessarily there
# yet when receiving the start event. Only the end event guarantees that the Element
# has been parsed completely.)
for event, element in etree.iterparse('home.xml', events = ('start', 'end'), tag = 'body'):
    print event, element.tag 
# start body
# end body
