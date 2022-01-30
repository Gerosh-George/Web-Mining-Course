import requests
from bs4 import BeautifulSoup as bs
import re

url=input('Enter the url: ')

resp = requests.get(url)

page = resp.text
soup= bs(page,'html.parser')

items = soup.find_all(class_="nav-item text-uppercase px-0")
print('\nList items of class “nav-item text-uppercase px-0”: ',*items,sep='\n')

elements = soup.find_all(string=re.compile('Matías Kulfas'))
print("\nElements containing string 'Matías Kulfas'")
for elem in elements:
    print(elem.parent)

images = soup.find_all("img")
print("\nAll Images :",*images,sep="\n\n")
print(f"\n Total number of image tags: {len(images)}")
