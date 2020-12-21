#Python
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
clname=['name']
df = pd.read_csv('list.csv',names=clname,header=None)
font = ImageFont.truetype('arial.ttf',60)
for index,j in df.iterrows():
    img = Image.open('certificate.jpg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(725,760),text='{}'.format(j['name']),fill=(0,0,0),font=font)
    img.save('{}.jpg'.format(j['name']))
