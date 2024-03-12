import csv
import pandas as pd

annotations = pd.read_csv("annotations_metadata.csv")
print(annotations.head())

# id = annotations["file_id"][0]
# file = open(f"all_files/{id}.txt")
# text = file.read()
# print(text)

text = []
for id in annotations["file_id"]:
    with open(f"all_files/{id}.txt", encoding='utf-8') as file:
        text.append(file.read())
        print(f"{id}.txt done")

annotations["text"] = text
annotations.to_csv("annotations_metadata_full.csv", index=False)