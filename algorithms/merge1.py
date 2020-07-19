import json
import glob

with open('file1.json') as f1, open('file2.json') as f2:
    file_1 = json.load(f1)
    file_2 = json.load(f2)

content = file_1 + file_2
with open('finalFile.json', 'w') as f:
    json.dump(content, f, indent=4)
