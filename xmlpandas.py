import pandas as pd
import xml.etree.ElementTree as et
import os

def intr_docs(xml_doc):
    attr = xml_doc.attrib

    for xml in xml_doc.iter('document'):
        doc_dict = attr.copy()
        doc_dict.update(xml.attrib)
        doc_dict['data'] = xml.text

        yield doc_dict

etree = et.parse('C:\\Users\\pykcian\\Desktop\\py\\xml\\reed.xml')
doc_df = pd.DataFrame(list(intr_docs(etree.getroot())))


print(doc_df.iloc[0, 10])

'''
with open("xml\\reed.xml", "r") as f:
    data = f.read()
    print(data)

    '''