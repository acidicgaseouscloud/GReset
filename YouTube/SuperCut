# Get Subtitles

!yt-dlp --write-auto-sub -a urls.txt # created in urls to txt


# Transcribe Subtitles
!videogrep --input *.mp4 --transcribe



# Rename Subtitles

from glob import glob
import os
from os.path import splitext, basename

## srt 
file_list = glob("*.srt")

for file in file_list:
    os.system(f"mv '{file}' '{file[:-7]}.srt'")
    
## vtt
file_list = glob("*.vtt")

for file in file_list:
    os.system(f"ffmpeg -i '{file}' '{file[:-4]}.srt'")
    
# Supercut 
## Multiple clips per video 
file_list = glob("*.mp4")

for file in file_list:
    os.system(f"videogrep --input '{file}' --search 'great reset' --search-type sentence  --output output/'{file}'")
  
## One clip from each video 
!videogrep --input *.mp4 --search "great reset" --search-type fragment --padding 0.1  --output test.mp4

