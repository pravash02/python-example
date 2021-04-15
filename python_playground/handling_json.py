import json


with open('json_file/json_set1.json') as f1:
  file1 = json.load(f1)

with open('json_file/json_set2.json') as f2:
  file2 = json.load(f2)

print(file1)
print(file2)

for key1, val2 in file1.items():
  for key2, val2 in file2.items():
     if key1 in file2[key2]:
       file1[key1].update({'subset': key2})

print(file1)
