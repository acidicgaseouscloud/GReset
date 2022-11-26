import pandas as pd
from glob import glob
import requests
import time
from random import random
from PIL import Image 
from os.path import splitext, basename
import sys
from PIL import Image, ImageDraw, ImageFont
import csv
import copy

# Creating an Excel Grid

df = pd.DataFrame()

## creating an index

indf = pd.read_excel('combined00.xlsx')
df.index = indf['Country'].tolist()

## VideoID grid
counter = 0

while counter != 50:
    for filepath in glob('*.xlsx'): # Position Excel sheets (video in position one for each country)
        if int(filepath[-7:-5]) == counter: # Files include position number
            tempdf = pd.read_excel(filepath)
            df[str(counter+1)] = tempdf['videoId'].tolist() # positions in sheets start from 1 but file names start from 0 
            counter +=1
            
df = df.sort_index() # alphabetical order of country names      

df.to_excel('VidIDgrid.xlsx') 

# Getting thumbnails

allVidsdf = pd.read_excel('allvideos.xlsx')
videoIDs = allVidsdf['videoId'].to_list() # getting all videoIDs in dataset

def exponentialbackoff(num): # artificially buffer to avoid making too many requests at once
    return (2**num) + random()
 
## Requesting YT for thumbnails 
# Default location for thumbnails on YT: "https://img.youtube.com/vi/<VIDID>/hqdefault.jpg"    

DefYTurl = "https://img.youtube.com/vi/" 

counter = 0 
for vid in videoIDs: 
    tempurl = DefYTurl + vid + '/hqdefault.jpg'
    counter+=1
    img_data = requests.get(tempurl).content
    img_name = 'GridCreation/' + vid + '.png'
    with open(img_name, 'wb') as handler:
        handler.write(img_data)
    time.sleep(exponentialbackoff(counter%5))
    
    
# Removing White Space
for img in glob('GridCreation/*.png'): 
    temp = Image.open(img)
    left = 0 # numbers manually measured
    top = 45
    right = 480
    bottom = 315
    img_res = temp.crop((left, top, right, bottom)) 
    newname = 'GridCreation/cropped' + splitext(img)[1]
    img_res.save(newname) 
    
    
# Pasting the images acc. to the VideoID Grid

vidf = pd.read_excel('VidIDgrid.xlsx')
vidf.set_index('Unnamed: 0') # column with country names

vidf.to_csv('VidIDgrid.csv')

with open('VidIDgrid.csv') as f: 
    reader = csv.reader(f)
    RefVideoIDGridListed = list(reader)
    
WorkingVideoIDGridList = copy.deepcopy(RefVideoIDGridListed)

## Creating Country Name Labels
    
for imglist in WorkingVideoIDGridList:
    del imglist[0:1] # the first item is the index number 
    img = Image.new('RGB', (480, 270), color = (255,255,255))
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 80)
    d.text((10,85), imglist[0], font = fnt, fill=(0,0,0))
    name = 'ctryim/' + imglist[0] + '.png'
    img.save(name)    
    
## Creating Position Number Labels    

for i in range(50):
    img = Image.new('RGB', (480, 270), color = (255,255,255))
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 80)
    d.text((200,85), str(i+1), font = fnt, fill=(0,0,0))
    name = 'thcr/' + str(i+1) + '.png'
    img.save(name)   
    
    
## Pasting Everything

new_im = Image.new('RGB', (480*51, len(WorkingVideoIDGridList)*270))
y_offset = 0 
for imglist in WorkingVideoIDGridList:
    x_offset = 0
    for im in imglist:
        name = 'thcr/' + im +'.png'
        new_im.paste(Image.open(name), (x_offset,y_offset))
        x_offset += 480
    y_offset += 270
new_im.save('grid.jpg')
