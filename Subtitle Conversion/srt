import webvtt
from os.path import splitext, basename

for filepath in glob('vtt/*'):
    vtt = webvtt.read(filepath)
    counter = 1
    subs = ''
    while counter <= (len(vtt)-1): 
      subs += vtt[counter].text
      counter += 2
    for char in subs: 
      subs = subs.replace('\n', "")
      f = open((splitext(basename(filepath))[0]+'.txt', 'x') 
      f.write(text)
      f.close()
