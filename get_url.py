import pandas as pd

urls = pd.read_excel("附件2：疫情通报网址.xlsx").values.tolist()
import requests

for i in urls:
    wb_data = requests.get(i[0])
    print(i[0])
    wb_data.encoding = 'utf-8'
    print(wb_data.text)
