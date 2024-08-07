import xml.etree.ElementTree as ET

file_path = "groceries.xml"

tree = ET.parse(file_path)
root = tree.getroot()

items_over_six = []

for item in root.findall("grocery_item"):
    name = item.find("name").text
    price = item.find("price").text
    if float(price) > 6.00:
        items_over_six.append(name)
    print(name, price)

print("items with price higher than 6.00:", items_over_six)