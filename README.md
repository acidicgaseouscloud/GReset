# The Great Reset 
Code written for project on The Great Reset 

## Steps
### General 
1. Procure list of [World Economic Forum](https://www.weforum.org/) participants
2. Read PDF to procure country information [^1] [^1]: Fails at countries with multiple words in their name.
3. Retrieve [ISO](https://www.iso.org/iso-3166-country-codes.html) codes

### YouTube
1. Use country codes to procure YouTube data via [YouTube Data Tools](https://tools.digitalmethods.net/netvizz/youtube/) using keyword "great reset" [^2] [^2]: Doesn't account for multilingual names of the phenomenon. 
  - Provides search results till position 50 as .csv
2. Produce one excel sheet of unique videos from each country.
 
#### Thumbnail Grid
1. Rearrange the excel sheets for each country to see the videos at a specific position (videos in position one for each country and so on)
2. Procure thumbnails for each video [^3] [^3]: Some videos got deleted / moderated between data collection and thumbnail collection so thumbnails may be missing. 
3. Create new image and place thumbnails according to video position (+ labels for country name and positions)

#### SuperCut
1. Download the unique videos and their subtitles (if available)
2. Transcribe videos for which subtitles are unavailable.  [^4] [^4]: Used the English language model so there may be some errors in transcription. 
3. Use the timestamps from the subtitles for clipping "great reset" from the videos 
4. Concatenate the clips


### BitChute
Doesn't have varying results by country. 

1. Scrape BitChute for the search results
2. Use search results to download the videos






