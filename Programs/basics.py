import requests
import re
import json

url = input('Enter the url: ')

link_graph_dict={}
link_graph_dict['main'] = url
link_graph_dict['extras'] = [] 
link_graph_dict['/'] = {} 

resp = requests.get(url)


if not resp.ok:
    exit('Error in accessing the url')

document = resp.text

embedded_urls = re.findall(r'href=[\'"]?([^\' ";]+)',document)

print(f'Main url : {url}')

print(f'Total number of urls extracted: {len(embedded_urls)}')
print("Showing the first 5 urls: ")

print( "\n".join([url for url in embedded_urls[:5]]))

for url_i in embedded_urls:    
    
    if url_i.startswith("#") or url_i == "javascript:void(0)":
        link_graph_dict['extras'].append(url_i)
        continue
    
    pages = re.findall(r'/?([^:/]+)',url_i)
    
    temp_dict = {}
    
    if not (url_i.startswith("http") or url_i.startswith('https')):        
        temp_dict = link_graph_dict['/']
    
    else:        
        temp_dict = link_graph_dict        
        
    for page in pages:
        if page not in temp_dict.keys():
            temp_dict[page]={}
        temp_dict = temp_dict[page]
            
    #print(url_i) 
            
with open('urls.json','w') as fp:
    json.dump(link_graph_dict,fp,indent=4)
    print('File saved')