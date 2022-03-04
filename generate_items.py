from PIL import Image
import json
import random

f = open('input.json')
data = json.load(f)
f.close()

images = []
count = 10000

def expand_props():
    data['new_props'] = {}
    for i in data['props']:
        props = data['props'][i]

        new_props = []

        for p in props:
            rarity = p['rarity']
            for y in range(0, rarity):
                new_props.append(p)

        data['new_props'][i] = new_props

expand_props()


def get_random_prop(props):
    prop_count = len(props)
    id = random.randint(0, prop_count-1)
    prop = props[id]
    return prop

# Prepare prop stats
prop_stats = {}
for i in data['props']:
    prop_stats[i] = {}

    sum = 0

    for x in data['props'][i]:
        sum += x['rarity']
        prop_stats[i][x['name']] = {
            "total": 0,
            "total_p": 0,
            "rarity": x['rarity'],
            "rarity_p": 0,
        }

    for x in data['props'][i]:
        prop_stats[i][x['name']]['rarity_p'] = format(prop_stats[i][x['name']]['rarity']/sum, '.2%')


for x in range(count):
    image = {}
    image['tokenId'] = x+1
    ip = {}

    for i in data['new_props']:
        props = data['new_props'][i]
        prop = get_random_prop(props)

        while (i == 'right' and ip['left']['class'] == prop['class']):
            prop = get_random_prop(props)
            

        prop_stats[i][prop['name']]['total'] = prop_stats[i][prop['name']]['total']+1
        ip[i] = prop

    for i in ip:
        ip[i] = ip[i]['name']

    image['props'] = ip

    images.append(image)
    # print(i)

for i in data['props']:
    for x in data['props'][i]:
        prop_stats[i][x['name']]['total_p'] = format(prop_stats[i][x['name']]['total']/count, '.2%')


raw = json.dumps(images)

f = open('output.json', 'w')
f.write(raw)
f.close()

f = open('prop_stats.json', 'w')
f.write(json.dumps(prop_stats))
f.close()