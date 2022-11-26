# PyPDF2==2.10.0
# nltk==3.6.5

import PyPDF2
import nltk # need for tokenisation
nltk.download('punkt')

PDfobj = open('WEFPart22.pdf', 'rb') 
# opens pdf 

pdfReader = PyPDF2.PdfFileReader(PDfobj) 
#read file

numofPages = pdfReader.numPages  
#necessary because it works with individual pages

PDFtext = '' # empty string to store text in 
for num in range(numofPages): # iterate over pages
    pageObj = pdfReader.getPage(num) # find relevant page
    PDFtext += pageObj.extractText() # add text to empty string 

ctries = read_file('listofctries.txt') 
#read list of all ctries

listofctries = ctries.split('\n') 
#convert string to list for iterability 

wefctriesdoubled = [token for token in nltk.word_tokenize(PDFtext) if token in listofctries] 
#iterate over the WEF pdf text to see which words in the text are country names

ParticipantsWEF2022 = set(wefctriesdoubled) 
# getting list of countries without repetition

textParticipantsWEF2022 = '\n'.join(ParticipantsWEF2022) 
# convert to string 

f = open('ParticipantsWEF2022.txt', 'x')
f.write(textParticipantsWEF2022)
f.close()

# write to file 

# =============
# Issue that countries with multiple words in their names
# are not included like USA, UK, UAE, New Zealand. Probably 
# fixable if their names in the list of all countries files
# are shortened to a defining word. But is a hack way, figure
# out how to fix it.
