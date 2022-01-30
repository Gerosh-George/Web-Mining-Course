import requests
from bs4 import BeautifulSoup

url=input('Enter the url: ')

resp = requests.get(url)

page = resp.text
soup= BeautifulSoup(page,'html.parser')

names = []
research=[]
print("Faculty names along with their research area: ")
for h3 in soup.findAll('h3',{'class':'title2'}):
    parent =  h3.parent
    p_tags = parent.find_all('p')
    if len(p_tags) == 3:
        if len(p_tags[2].text)==1:
            research.append('None')
        else:
            research.append(p_tags[2].text)
    else:
        research.append('None')
    names.append(h3.text)

for faculty,research in zip(names,research):
    print(f'{faculty}: {research}')

print("\nSocial Links: ")

links_span = soup.find('span',{'class':'soclia_links'})
links = links_span.find_all('a')
for link in links:
    print(f"{link['title']} : {link['href']}")
    print(f"class name: {link['class']}\n")