
#Libraries
import requests
import urllib
from bs4 import BeautifulSoup
import regex


base_url = 'https://ctftime.org/event/list/?year=2024&online=-1&format=0&restrictions=-1'

headers = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

page = requests.get(base_url, headers=headers)

print(page.text)

#no headers returns 403 forbidden

soup = BeautifulSoup(page.content, "html.parser")