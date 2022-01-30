import requests
from bs4 import BeautifulSoup as bs


url=input('Enter the url: ')

resp = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})

page = resp.text
soup= bs(page,'html.parser')

def graph(value,size):
    if size>=12:
        return
    else:
        for i in value.findChildren(recursive=False):
            for j in range(-1,size,1):
                print("|",end=" ")
            print("->",i.name)
            graph(i,size+1)
            
graph(soup.html,0)