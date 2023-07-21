import os
import requests
from googlesearch import search
import time
from dotenv import load_dotenv
load_dotenv()

site_names = str(os.getenv('SITE_NAMES', default='')).split(',')


def send_message(msg):
    if os.system(f"python message_sender_v2.py {msg}") == 0:
        return True
    else:
        return False


def google_search(query: str):
    results = search(query)
    urls = []
    for result in results:
        urls.append(str(result))
    return urls


def find_movies(movie_name):

    founds = []
    urls = []

    for site_name in site_names:
        results = google_search(site_name)
        urls.append(results[0])

    for url in urls:

        url2 = '{url}?s={query}'
        html_cont_1 = requests.get(url).text
        html_cont_2 = requests.get(url2.format(
            url=url, query=movie_name[:-1])).text


        if movie_name.lower() in html_cont_1.lower():
            founds.append(url)

        if movie_name.lower() in html_cont_2.lower():
            founds.append(url2.format(url=url, query=movie_name))

    return founds


def ms(movie_name):
    
    founds = find_movies(movie_name)
    if len(founds) > 0:
        formatted_msg = ''
        for found in founds:
            formatted_msg += f'{movie_name} found @ {found}, '
        send_message(formatted_msg[:-1])
    else:
        send_message(f'Still seaching for {movie_name}')
            
