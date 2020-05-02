import pandas as pd
import json

urls = pd.read_excel("附件2：疫情通报网址.xlsx").values.tolist()
import requests
import re

data_list = []
data_dict = {}

for i in urls:
    wb_data = requests.get(i[0])
    print(i[0])
    wb_data.encoding = 'utf-8'
    print(wb_data.text)
    data_dict["url"] = i[0]
    data_list.append(data_dict)
    pat = re.compile('>(.*?)<')
    data_dict["context"] = ''.join(pat.findall(wb_data.text))

with open('data_context.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data_list, ensure_ascii=False))
