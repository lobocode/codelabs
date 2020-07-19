import json

lista = []
new_list = []


content1 = [{'Name': 'Fulano',
         'Age': '34',
         'Job': 'SRE'
          }]

content2 = [{'Name': 'Fulano',
         'Age': '34',
         'Job': 'SRE'
          }]


content = content1 + content2

for item in content:
    if item not in new_list:
        new_list.append(item)

# if content is empty, don't write file
if not content1 or content2:
    with open('finalFile.json', 'w') as f:
        json.dump(new_list, f, indent=4)
