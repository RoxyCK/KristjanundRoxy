# pip install google_images_download
# https://google-images-download.readthedocs.io/en/latest/arguments.html
# https://www.geeksforgeeks.org/how-to-download-google-images-using-python/

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

from google_images_download import google_images_download 
response = google_images_download.googleimagesdownload()

query = {'keywords': 'mona lisa',
         'format': 'jpg',
         'limit': 10,
         'print_urls': True,
         'size': 'large',
         'aspect_ratio': 'square'}

response.download(query) 
    
