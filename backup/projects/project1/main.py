import requests
from lxml import html
import os

url = 'https://news.google.com/news/?ned=pt-BR_br&hl=pt-BR&gl=BR'

response = requests.get(url)

if response.status_code == 200:
    print('Response OK')
    page = html.fromstring(response.text)
    if page is not None:
        """
            [a]   
            class="nuEeue hzdq5d ME7ew"
            role="heading"
        """
        lines = page.cssselect('a.nuEeue.hzdq5d.ME7ew')
        if lines:
            f = open('news.csv', 'w')
            for line in lines:
                if line is not None:
                    f.write(line.text_content().encode('utf-8').replace(',',' ').replace(';',' ') + ",\n")    

            f.close()
            print('Process finished!')
else:
    print('Response Failed!')