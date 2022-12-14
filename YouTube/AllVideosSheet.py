bigdf = pd.DataFrame()
for filepath in glob('lists/*.csv'): 
        tempdf = pd.read_csv(filepath)
        bigdf = pd.concat([bigdf,tempdf])
bigdf = bigdf.drop_duplicates(subset=['videoId']) # removing repeated entries based on videoId

bigdf.to_excel('allvideos.xlsx')
