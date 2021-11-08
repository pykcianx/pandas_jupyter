import xml.etree.ElementTree as ET
import pandas as pd
import codecs


with codecs.open('nasadata.xml', 'r', encoding='utf8') as f:
    tt = f.read()


def xml2df(xml_data):
    root = ET.XML(xml_data)
    all_records = []
    for i, child in enumerate(root):
        record = {}
        for sub_child in child:
            record[sub_child.tag] = sub_child.text
        all_records.append(record)
    return pd.DataFrame(all_records)


df_xml1 = xml2df(tt)
print(df_xml1)