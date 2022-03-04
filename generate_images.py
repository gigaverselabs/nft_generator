from PIL import Image
import json
import time
import threading

from multiprocessing.pool import ThreadPool as Pool

start = time.time()

# print("Loading assets: ... ", end='')

f = open('output.json')
items = json.load(f)
f.close()

# print("OK")

def process_image(pos, data, props):
    try:
        res = None

        item = data['props']

        for prop_name in item:
            prop = item[prop_name]
            prop_val = props[prop_name+'_'+prop]
            if res == None:
                res = prop_val['img_data'].copy()
            else:
                res.paste(prop_val['img_data'], (0, 0), prop_val['img_data'])

        res.save("output/"+str(data['tokenId'])+".jpg", "JPEG")
        # print('output/'+str(pos)+".jpg")
    except Exception as e:
        print('error with item '+str(pos)+" "+str(e))

def generate_images(start, count):
    print("Generating images from: "+str(start)+", count: "+str(count-start))

    f = open('input.json')
    data = json.load(f)
    f.close()

    props = {}

    # Loading data about props
    for item in data['props']:
        for val in data['props'][item]:
            val['image'] = item+'/'+val['image']
            img = Image.open('data/'+val['image']+"_resized.png")
            val['img_data'] = img
            props[item+"_"+val['name']] = val

    for pos in range(start, count):
        process_image(pos, items[pos], props)

    print("Finished images from: "+str(start)+", count: "+str(count))

def run_pool():
    pool_size = 6
    pool = Pool(pool_size)
    for pos in range(0, 100):
        pool.apply_async(generate_images, (pos*100, pos*100+100,))

        # pool.apply_async(process_image, (pos, items[pos],))


    pool.close()
    pool.join()


if __name__ == '__main__':
    run_pool()
    # process_image(4004,items[4004])
    # p1 = threading.Thread(target=generate_images, args=(0,1000,))
    # p1.start()
    # p2 = threading.Thread(target=generate_images, args=(1000,1000,))
    # p2.start()
    # p3 = threading.Thread(target=generate_images, args=(2000,1000,))
    # p3.start()
    # p1.join()
    # p2.join()
    # p3.join()

# counter = 0
# # Generating output images
# for item in items:
#     res = None

#     for prop_name in item:
#         prop = item[prop_name]
#         prop_val = props[prop_name+'_'+prop]
#         if res == None:
#             res = prop_val['img_data'].copy()
#         else:
#             res.paste(prop_val['img_data'], (0, 0), prop_val['img_data'])

#     res.save('output/'+str(counter)+".jpg", "JPEG")
#     print(str(counter))
#     counter = counter+1
#     # base = Image.open("data/background/background.png")




end = time.time()
print("The time of execution of above program is :", end-start)