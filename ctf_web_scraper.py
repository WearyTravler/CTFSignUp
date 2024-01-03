
#Libraries
import requests
import urllib
from bs4 import BeautifulSoup
import regex


base_url = 'https://ctftime.org/event/list/?year=2024&online=-1&format=0&restrictions=-1'

page = requests.get(base_url)

print(page.text)

#no headers returns 403 forbidden

soup = BeautifulSoup(page.content, "html.parser")