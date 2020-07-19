import json
import glob

lista = []
new_list = []


with open('file1.json') as f1, open('file2.json') as f2:
    content1 = json.load(f1)
    content2 = json.load(f2)


content = content1 + content2

for item in lista:
    if item not in new_list:
        new_list.append(item)

#tosqueira = lista[0] + lista[1]


with open('finalFile.json', 'w') as f:
    json.dump(new_list, f, indent=4)
