"""
* author: dick und doof und dick
*
*
"""

# pip install google_images_download
# https://google-images-download.readthedocs.io/en/latest/arguments.html
# https://www.geeksforgeeks.org/how-to-download-google-images-using-python/

import requests
from bs4 import BeautifulSoup
from google_images_download import google_images_download 
from random import shuffle
from data_manager import YamlManager

url = 'https://de.wikipedia.org/wiki/Liste_von_Serienm%C3%B6rdern'
image_folder = 'serial_killers'
yaml_file = 'serial_killers.yml'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
source  = requests.get(url).text

#if source.status_code is 200, the html has been correctly downloaded
#print(source.status_code)

soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

soup = soup.find('table', {'class':'wikitable sortable'})
killers = soup.findAll('tr')

titles = killers[0].findAll('th')
titles = [title.text.strip() for title in titles]

killer_data = []
for killer in killers[1:]:
    specs = killer.findAll('td')
    specs = [spec.text.strip().split('[')[0] for spec in specs]
    killer_dict = dict(zip(titles, specs))
    killer_data.append(killer_dict)
    #print(killer)
    #print(specs)
    print(killer_dict)

YamlManager.save(yaml_file, killer_data)

error_killers = []

shuffle(killer_data)

for killer in killer_data[:10]:
    
    try:
        
        q = '{} {} killer'.format(killer['Name'], killer['Pseudonym']) # google query
        """
        format: jpg, gif, png, bmp, svg, webp, ico, raw
        size: medium, icon, >400*300, >640*480, >800*600, >1024*768, >2MP, >4MP, >6MP, >8MP, >10MP, >12MP, >15MP, >20MP, >40MP, >70MP
        color: red, orange, yellow, green, teal, blue, purple, pink, white, gray, black, brown
        color_type: full-color, black-and-white, transparent
        aspect_ratio: tall, square, wide, panoramic
        output_directory: default is 'downloads'
        image_directory: default is the keyword
        """
        query = {'keywords': q,
                 'format': 'jpg',
                 'limit': 10,
                 'print_urls': False,
                 'size': 'large',
                 'aspect_ratio': 'square',
                 'output_directory': image_folder,
                 'image_directory': killer['Name']}    
        response = google_images_download.googleimagesdownload()
        response.download(query)

    except UnicodeDecodeError as ex:
        error_killers.append(killer)
        print(ex)

[print('\n\n=> Error:', error_killer) for error_killer in error_killers]
    


