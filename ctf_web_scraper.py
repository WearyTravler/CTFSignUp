
#Libraries
import requests
import urllib
from bs4 import BeautifulSoup
import regex


base_url = 'https://ctftime.org/event/list/?year=2024&online=-1&format=0&restrictions=-1'

headers = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

page = requests.get(base_url, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

ctf_table = soup.find_all('table')

def remove_tags(html):

    soup = BeautifulSoup(page.content, "html.parser")

    for data in soup(['style', 'script']):
        data.decompose()

    return ' '.join(soup.stripped_strings)

# print(remove_tags(ctf_table))


ctf_title = soup.find_all('title')

print(ctf_title)
