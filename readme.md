# How to use

Prepare input.json with data about parts of your NFTs.

amount - contains amount of nft to be generated
props - contains details about possible properties


Props is a dictionary which is composed of pairs "Property Name": "Property values". Property values is also a dictionary

eg.

`{ "name": "Beige Canvas", "image": "BeigeCanvas.jpeg", "rarity": 5 }`


IMPORTANT:

image must match file in folder data\property_name\file_name. For eg. data\background\BeigeCanvas.jpeg

rarity - the higher number the more common


# Generate Images

Process of NFT generation is splitted in to two parts: 

1. NFT data generation
2. Image generation

## Nft data generation
run `python generate_items.py` this will create output.json with specifics about each NFT in your collection

## Image generation
run `python generate_images.py` this will merge your images in to one and save the output to `output` folder

IMPORTANT!!

All images used in NFT generation must be in the same size, there is a tool resize_images.py that can be used to resize all images used in props to one size, you need to specify size in script

Image generation uses all cores of your machine (your fans will reach maximum ;), it is computation intensive and takes time, be patient! 
