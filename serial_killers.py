# pip install google_images_download
# https://google-images-download.readthedocs.io/en/latest/arguments.html
# https://www.geeksforgeeks.org/how-to-download-google-images-using-python/

import requests
from bs4 import BeautifulSoup
from google_images_download import google_images_download 
import yaml
from random import shuffle

def save(file_name, yaml_data):
    with open(file_name, 'w') as yaml_file:
        yaml.dump(yaml_data, yaml_file)
        
def load(file_name):
    with open(file_name, 'r') as yaml_file:
        return yaml.load(yaml_file)
    
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
url = 'https://de.wikipedia.org/wiki/Liste_von_Serienm%C3%B6rdern'
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
    #print(killer_dict)

#file_name = 'serial_killers.yaml'
#save(file_name, killer_data)
#killer_data = load(file_name)

"""
parameter:
    format: jpg, gif, png, bmp, svg, webp, ico, raw
    size: medium, icon, >400*300, >640*480, >800*600, >1024*768, >2MP, >4MP, >6MP, >8MP, >10MP, >12MP, >15MP, >20MP, >40MP, >70MP
    color: red, orange, yellow, green, teal, blue, purple, pink, white, gray, black, brown
    color_type: full-color, black-and-white, transparent
    aspect_ratio: tall, square, wide, panoramic
    output_directory: default is 'downloads'
    image_directory: default is the keyword
"""

shuffle(killer_data)
for killer in killer_data[:10]:
    
    print(killer)
    
    q = 'killer ' + killer['Name'] # google query
    query = {'keywords': q,
             'format': 'jpg',
             'limit': 10,
             'print_urls': False,
             'size': 'large',
             'aspect_ratio': 'square',
             'output_directory': 'serial_killers',
             'image_directory': killer['Name']}    
    response = google_images_download.googleimagesdownload()
    response.download(query) 



