from bs4 import BeautifulSoup
import requests
import pandas as pd 

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
url = 'https://de.wikipedia.org/wiki/Liste_von_Serienm%C3%B6rdern'
source  = requests.get(url).text

#if source.status_code is 200, the html has been correctly downloaded
#print(source.status_code)



soup = BeautifulSoup(source, 'lxml')

my_table = soup.find('table', {'class':'wikitable sortable'})
link = my_table.findAll('a')
killers = []
for name in link:
    if name.get('title') == None:
        pass
    else:
        killers.append(name.get('title'))


df = pd.DataFrame()
df['serial killers'] = killers

KillerFile=open('serial_killers.txt','w')

for element in killers:
    KillerFile.write(element)
    KillerFile.write('\n')

KillerFile.close()


    
    


