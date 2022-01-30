import requests
from bs4 import BeautifulSoup

url=input('Enter the url: ')

resp = requests.get(url)

page = resp.text
soup= BeautifulSoup(page,'html.parser')

print(f'\nTitle of page: {soup.title.text}\n')

a_tags = soup.findAll(name='a', attrs={'class':'nav-link'})

for a in a_tags:
    print(a) 