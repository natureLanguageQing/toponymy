import csv
import json

with open("../data_context_list.json", encoding="utf-8") as f:
    words = json.load(f)
question_list = []
question_count = {}
for i in words:
    for j in i["context"]:
        question = j.strip()

        if not isinstance(question, str):
            continue
        if "&nbsp" in question:
            question = question.strip("&nbsp")

        if question not in question_list:
            question_list.append(question)
        print(question)
        if question in question_count.keys():
            question_count[question] += 1
        else:
            question_count[question] = 1
for question, count in question_count.items():
    print(question, count)
fp = open('question_entity_list.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(fp)
question_ner = {}
writer.writerow(("words", "entity"))
import pandas as pd

local_list = []
ICD_10 = pd.read_excel("../entity/d_330500.xls").values.tolist()
for j in question_list:
    for i in ICD_10:
        if i[1] not in local_list:
            local_list.append(i[1])
        if i[2] not in local_list:
            local_list.append(i[2])
        #         if i[1] == "":
#             continue
#         if i[2] == "":
#             continue
#         if i[1] in j:
#             if j in question_ner.keys():
#                 question_ner[j].append([i[1], "local_first"])
#             else:
#                 question_ner[j] = [[i[1], "local_first"]]
#         if i[2] in j:
#             if j in question_ner.keys():
#                 question_ner[j].append([i[2], "local_second"])
#             else:
#                 question_ner[j] = [[i[2], "local_second"]]
# for i, j in question_ner.items():
#     c = [i] + j
#     writer.writerow((c))
pd.DataFrame(local_list).to_csv("local_list.csv", index=False)
