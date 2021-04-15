item = [
  {
   'Clothes': [
               {
                 'id': '32705111',
                 'describes': 'no problem'
               }
             ]
  },
  {
   'Dress': [
               {
                 'id': '32705111',
                 'describes': 'no outfit'
               }
           ]
  }
]


for d in item:
    for name, array in d.items():
        globals()[name] = array
new_lst = []

for i in item:
    for name, array in i.items():
       value = ''.join(str(array))
       result = name+value
       new_lst.append(result)

print(new_lst)