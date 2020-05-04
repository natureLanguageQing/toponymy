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
        for k in range(len(cut_words) - 1):
            word = cut_words[k] + cut_words[k + 1]
            if word in word_count.keys():
                word_count[word] += 1
            else:
                word_count[word] = 1
export = []
for i, j in word_count.items():
    export.append([i, j])
import pandas as pd

pd.DataFrame(export).to_csv("bigram_cut_word_count.csv", index=False)
