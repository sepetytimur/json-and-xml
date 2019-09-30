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
    word_lower = word.lower()
    if word_lower in dict:

        dict[word_lower] += 1
    else:

        dict[word_lower] = 1

sorted_x = sorted(dict.items(), key=operator.itemgetter(1))
print(sorted_x[-10:])

