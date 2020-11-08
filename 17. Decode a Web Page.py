import requests
from bs4 import BeautifulSoup

main_url = 'https://www.nytimes.com/'
req = requests.get(main_url)
soup = BeautifulSoup(req.text, "html.parser")

for paragraph in soup.find_all("div", class_='css-debyuq e1voiwgp1'):
    print(paragraph.text)
