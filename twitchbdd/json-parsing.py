import json

with open('download/file1.json', 'r') as f:
    data = json.load(f)

# print(data)
keys = data.keys()
print(keys)

chatters = data['chatters']
print(chatters)

viewers = chatters['viewers']
print(viewers)