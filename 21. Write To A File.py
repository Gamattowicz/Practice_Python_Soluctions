import requests
from bs4 import BeautifulSoup

base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(base_url)
soup = BeautifulSoup(r.content, "html.parser")

article = soup.find_all("p")

a = [i.get_text() for i in article[7:]]

name = input('Enter a name of file: ')

with open(name, 'w', encoding='utf-8') as open_file:
    for b in a:
        open_file.write(b)
