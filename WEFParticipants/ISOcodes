# pandas==1.3.4
import pandas as pd

with open('ParticipantsWEF2022.txt', encoding='utf8') as infile: # see creation of this file from listCtries
        contents = infile.read()
        ParticipantsWEF2022 = contents.split('\n')

ISOdf = pd.read_excel('allctriesnisocodes.xlsx') # open excel sheet with all countries and ISO codes as pd dataframe

isocodes = [] # empty list initialised to store relevant ISO codes 

for ctry in ParticipantsWEF2022:
    isolate_ISOdf = ISOdf.loc[ISOdf['Country name (using title case)']==ctry]
    isocodes.append(isolate_ISOdf['Code'].item())
# ISO codes for countries in WEF
    
selectISOcodes = '\n'.join(isocodes) # convert to string 
ISOf = open('SelectISOcodes.txt', 'x')
ISOf.write(selectISOcodes)
ISOf.close()
# write to file 
