from bs4 import BeautifulSoup
import requests


#url = 'https://realpython.github.io/fake-jobs/'
url = 'https://www.vit.ac.in'
print(f"URL: {url}","\n")

resp =  requests.get(url)

page= resp.text

soup= BeautifulSoup(page,'html.parser')

print(soup.text)

print("Showing a part of html document in formatted manner: ")
print(soup.prettify()[:258])
print(f"\nTitle: {soup.title.string}")  
print(f"\nParent of title tag: {soup.title.parent.name}") 

print("\nShowing first 5 links: ")
for link in soup.findAll('a')[:5]:
    print(link['href'])

print(f"\nChecking for p tag: {soup.p} [{soup.p.name}]")
print(f"Checking for style attribute in p tag: {soup.p['style']} ")
print(f"Attribute dictionary of p tag: \n{soup.p.attrs}")

print(soup.p.get_attribute_list("style"))

print("\nTried string and contents on p tag 👇")
print(soup.p.a.span.string.replace(" ",""))
print("\n",soup.p.contents)


menu = soup.find('ul',{"class":'vc-nav-on-desktop vc-mm-menu'})
print("\n", menu.name + " " + menu['class'][0])
print("Priniting all the children in the menu")
for i,child in enumerate(menu.children):
    if(child!='' and child!='\n'):
        print(f"Class attribute of child {i+1}: ",child['class'])
        if child.a:
            print(child.a.string)

print(f"\nNumber of descendants of this webpage: {len(list(soup.descendants))}")


div_tag = soup.find('div',{'class':'ful_wid_col gal_imgs video_gal_col'})
print("\nDiv Tag: ",div_tag)
print("\nNext sibling of ☝ div tag: ",div_tag.next_sibling.next_sibling)
print("\nPrevious Sibling of above div tag: ",div_tag.previous_sibling.previous_sibling)

print("\nPrinting ids of all the div present in the page: ")

for div in soup.find_all('div',{'id':True}):
    print(div['id'])
        

    
    
    