import os
from xml.etree import ElementTree


full_file = os.path.abspath(os.path.join('xml', 'reed.xml'))
dom = ElementTree.parse(full_file)
courses = dom.findall('course')

for c in courses:
    title = c.find('title').text
    num = c.find('crse').text
    days = c.find('days').text

    print(' *  {}  [{}]  {} '.format(num, days, title))


'''
with open("xml\\reed.xml", "r") as f:
    data = f.read()
    print(data)
'''
