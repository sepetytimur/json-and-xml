import xml.etree.ElementTree as ET
from pprint import pprint
import operator
tree = ET.parse('newsxml.xml')
# print(tree)
root = tree.getroot()
xml_items = root.findall('channel/item')
news_list = []
dict = {}
for item in xml_items:
    news_list += item.find('description').text.split(' ')

    for word in news_list:
        if len(word) <= 6:
            continue

        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
sorted_x = sorted(dict.items(), key=operator.itemgetter(1))
print(sorted_x[-10:])
