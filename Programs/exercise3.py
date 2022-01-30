import requests
from bs4 import BeautifulSoup as bs
import re

url=input('Enter the url: ')

resp = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

page = resp.text
soup= bs(page,'html.parser')

# items = soup.findAll('ul',{'class':'menu'})
# print(f"Number of items of class menu: {len(items)}")
 
# print("\nItems inside class Menu with classes 'first leaf', 'leaf' and 'last leaf'")
# for item in items:
#     elements = item.findAll('li',{'class':['leaf','last leaf','first leaf']})
#     for elem in elements:
#         print(elem)
#     print("\n")

# items = soup.findAll(id=re.compile("menu"))
# print("\nAll elements with id containing  'menu':\n",*items,sep="\n")

# articles = soup.find_all("article")
# print("\nAll article tags:\n",*articles,sep="\n")



