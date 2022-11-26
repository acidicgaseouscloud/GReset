from glob import glob
from os.path import splitext, basename
import json
#https://www.freecodecamp.org/news/loading-a-json-file-in-python-how-to-read-and-parse-json/

for file in glob('json/*'): 
    name = 'text/' + splitext(basename(file))[0] + '.txt'
    f = open(file)
    data = json.load(f)
    f.close()
    counter = 0 
    text = ''
    while counter != (len(data)-1):
        line = data[counter].get("content")
        text += (line + ' ')
        counter +=1
    ft = open(name, 'x')
    ft.write(text)
    ft.close()
        
