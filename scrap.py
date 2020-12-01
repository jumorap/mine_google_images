import re
from urllib import parse, request
from urllib.request import Request, urlopen
import urllib3
import requests
from bs4 import BeautifulSoup
import time


def to_scrap(waifu_type, n_images, width, height, path, name_to_save):
    counter = 0
    search = f'{waifu_type} faces {width}x{height}'
    query_str = parse.urlencode({'': search})
    html_cont = f'https://www.google.com.co/search?hl=es&tbm=isch&q{query_str}'
    page = requests.get(html_cont)
    print(html_cont)
    print(page)

    search_res = BeautifulSoup(page.content, 'html.parser')
    to_return = search_res.find_all('img', class_='t0fcAb')
    print(search_res)

    for i in to_return[:n_images]:
        counter += 1
        my_file = requests.get(i['src'])

        open(f'{path}/{name_to_save}%d.png' % int(counter), 'wb').write(my_file.content)

    return to_return[:n_images]


waifu_type = "yandere"
n_images = 10
width = 100
height = 100


path = "results"
name_to_save = "yandere_proof"


print(to_scrap(waifu_type, n_images, width, height, path, name_to_save))
