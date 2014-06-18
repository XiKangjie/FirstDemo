import xml.etree.ElementTree as ET

tree = ET.parse("country_data.xml")
root = tree.getroot()

# get and set attribute
neighbor = root.find("country/neighbor")
print(neighbor.tag, neighbor.get("name"))
neighbor.set("name", "austria")
print(neighbor.tag, neighbor.get("name"))

# set text
for year in root.findall("country/year"):
	year.text = "2014"

tree.write("country_data.xml", "utf-8")
tree.write("country_data2.xml", "utf-8")

