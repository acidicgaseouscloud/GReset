from glob import glob
from os.path import splitext, basename

newindex = []
for filepath in glob('lists/*.csv'): # iterate over all the YT ctry csvs in folder
    newindex.append(splitext(basename(filepath))[0]) # remove file path and extension to use as name

CtryName = [] # Empty list to store country names by looking up using ISO codes
ISOdf = pd.read_excel('allctriesnisocodes.xlsx') 
for ctry in newindex: 
    tempdf = ISOdf.loc[ISOdf['Code']==ctry]
    CtryName.append(tempdf['Country name (using title case)'].item())

for i in range(50):
    CtryName = [] #empty list to store country names by looking up using ISO codes
    posdf = pd.DataFrame()
    for filepath in glob('lists/*.csv'): 
        ctrydf = pd.read_csv(filepath)
        pos_i_df = ctrydf.iloc[i:i+1]
        posdf = pd.concat([posdf,pos_i_df])
    posdf['position'] = CtryName
    posdf.rename(columns = {'position':'Country'}, inplace = True) 
    posdf.to_excel('positions/combined' + str(i) + '.xlsx')
