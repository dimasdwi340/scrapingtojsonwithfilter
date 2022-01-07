import json

list = ['aku', 'kamu', 'kita']
with open ('coba.json', 'w') as f:
    json.dump([list], f)
    print ("done")

with open('coba.json','r') as f:
    data = f.read()

data = "[" + data.replace("}", "},", data.count("}")-1) + "]"
json_data = json.loads(data)
