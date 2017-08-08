import json

with open('download/file1.json', 'r') as f:
    data = json.load(f)

chatters = data['chatters']


viewers = chatters['viewers']
global_mods = chatters['global_mods']
admins = chatters['admins']
moderators = chatters['moderators']

viewers.extend(global_mods)
viewers.extend(admins)
viewers.extend(moderators)

if debug == 1:

