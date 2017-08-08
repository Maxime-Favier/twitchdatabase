try:
    import json

except ImportError:
    raise ImportError('unable to find json package')

# open and load data in dictionary
try:
    with open('download/file1.json', 'r') as f:
    data = json.load(f)

except FileNotFoundError:
    raise FileNotFoundError('unable to find the downloaded file')

# recover the list of viewers
chatters = data['chatters']

# recover the list of viewer and all type of moderator
viewers = chatters['viewers']
global_mods = chatters['global_mods']
admins = chatters['admins']
moderators = chatters['moderators']

# add all type of moderator in the viewer list
viewers.extend(global_mods)
viewers.extend(admins)
viewers.extend(moderators)

if debug == 1:
    print(viewers)
