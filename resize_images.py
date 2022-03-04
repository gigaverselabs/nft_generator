from PIL import Image
import json

f = open('input.json')
data = json.load(f)
f.close()

props = {}

# Loading data about props
for item in data['props']:
    for val in data['props'][item]:
        val['image'] = item+'/'+val['image']
        print("Resizing: "+val['image'])
        img = Image.open('data/'+val['image'])
        img = img.resize((1600, 1600))
        img.save('data/'+val['image']+"_resized.png", "PNG")