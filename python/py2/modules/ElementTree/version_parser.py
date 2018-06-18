import xml.etree.ElementTree as ET

class Engine:
	def __init__(self):
		self.version = 0
	def set_version(self, v):
		self.version = v
	def get_version(self):
		return "13", "15", self.version

engine = Engine()
engine.set_version("5.6.9.15")
min_version, max_version, engine_version = engine.get_version()
print(min_version, max_version, engine_version)

engine_version = engine_version.split(".")
print(engine_version)



tree = ET.parse("product_all_version.xml")
root = tree.getroot()

for product in root.findall("support/product_name"):
	if product.attrib["name"] == "foo":
		for version in product.findall("production_vesrion"):
			if version.attrib["bigversion"] == "5.6.9":
				min_version = version.find("min_version").text
				max_version = version.find("max_version").text
				dataversion = version.find("dataversion").text
				break
		break

print(min_version, max_version, dataversion)
