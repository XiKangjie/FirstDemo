from lxml import etree

doc = etree.parse('home.xml')
root = doc.getroot()

title = root.find('head/title')
print title.text
title.text = 'Your page title'
print title.text

# write as it is, space, tab, empty line ...
# may change CRLF to CR
doc.write('home.xml', encoding='utf-8')
