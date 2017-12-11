from lxml import etree

xmlschema_doc = etree.parse('valid.xsd')
xmlschema = etree.XMLSchema(xmlschema_doc)

doc = etree.parse('valid.xml')
print xmlschema.validate(doc)
# True

print type(doc)
# <type 'lxml.etree._ElementTree'>
root = doc.getroot()
print type(root)
# <type 'lxml.etree._Element'>
print xmlschema.validate(root)
# True
