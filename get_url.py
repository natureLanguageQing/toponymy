import random

import pandas as pd
import json

urls = pd.read_excel("附件2：疫情通报网址.xlsx").values.tolist()
import requests
import re

headers_pool = [{
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'},
]
data_list = []
word_encoding = []
ISO = []
for i in urls:
    data_dict = {}

    wb_data = requests.get(i[0], headers=random.choice(headers_pool))
    print(i[0])
    print("wb_data.encoding", wb_data.encoding)
    if wb_data.encoding not in word_encoding:
        word_encoding.append(wb_data.encoding)
    if wb_data.encoding == "ISO-8859-1":
        data_dict["encoding"] = wb_data.encoding

        wb_data.encoding = 'utf-8'
        data_dict["url"] = i[0]
        pat = re.compile('>(.*?)<')
        data_dict["context"] = (pat.findall(wb_data.text))
        ISO.append(data_dict)
    else:
        data_dict["encoding"] = wb_data.encoding

        wb_data.encoding = 'utf-8'
        data_dict["url"] = i[0]
        pat = re.compile('>(.*?)<')
        data_dict["context"] = (pat.findall(wb_data.text))
        data_list.append(data_dict)

with open('data_context_list.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data_list, ensure_ascii=False))
with open('data_context_ISO.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(ISO, ensure_ascii=False))
import pandas as pd

pd.DataFrame(word_encoding).to_csv("word_encoding.csv")
