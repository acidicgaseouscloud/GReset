import bitchute as bc
import pandas as pd
from glob import glob

b = bc.Crawler()        
videos = b.search("great reset", top=130)

df.to_excel("BitChuteTop130.xlsx")
df.to_csv("BitChuteTop130.csv")

df = pd.read_csv("BitChuteTop130.csv")

# URL list
urls = []
for vidid in list(df.id): 
    urls.append("https://www.bitchute.com/video/"+vidid)
  
df['urls'] = urls  

textBCurls = '\n'.join(urls)
f = open('BCurls.txt', 'x')
f.write(textBCurls)
f.close()

# wget the url list: wget -i BCurls.txt gives html files

# find the actual location of video 

sourceURLs = []
for file in glob("html/*"):
    text = read_file(file)
    text = text.split('\n')
    for line in text: 
        if "video/mp4" in line:
            linelisted = line.split()
            srcline = linelisted[1]
            finalurl = srcline[5:-1]
            sourceURLs.append(finalurl)
            break
            
df['sourceURLS'] = sourceURLs

def WriteListTxt(list, name):
    text = '\n'.join(list)
    f = open(name, 'x') 
    f.write(text)
    f.close()
    
WriteListTxt(sourceURLs, "SourceURLs.txt")

# wget the above list to get the videos 
