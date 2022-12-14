bigdf = pd.read_excel('allvideos.xlsx') # created in All Videos Sheet

urls = []
for vidid in list(bigdf.videoId): # converting this column of the df to list 
    urls.append("https://www.youtube.com/watch?v="+vidid) # appending url to file

bigdf['urls'] = urls # adding this column to the df 
bigdf.to_excel('allvideos.xlsx')


urlsf = open('urls.txt', 'x')
urlsf.write('\n'.join(urls))
urlsf.close()
