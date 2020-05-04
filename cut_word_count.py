import json
import jieba
with open("data_context_list.json", encoding="utf-8") as f:
    words = json.load(f)
word_count = {}
for index, i in enumerate(words):
    print(index, i)
    for j in i["context"]:
        word = j.strip()
        cut_words = jieba.lcut(word)
        for k in cut_words:
            if k in word_count.keys():
                word_count[k] += 1
            else:
                word_count[k] = 1
export = []
for i, j in word_count.items():
    export.append([i, j])
import pandas as pd

pd.DataFrame(export).to_csv("cut_word_count.csv", index=False)
