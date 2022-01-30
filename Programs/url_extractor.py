import requests
import re
import json


url = input('Enter the url: ')
url = url if url[-1] != '/' else url[:-1]

count = int(input('Max #urls to be extracted: '))
depth = int(input('Max depth to consider: '))

unique_links=set()

data={
    url:{}    
}

def get_links(url,url_dict,c_depth):
    
    if url in unique_links:
        return
    
    unique_links.add(url) 
    
    if depth == c_depth:
        return  
    
    temp=url_dict[url]   
    
    resp=requests.get(url)

    if not resp.ok:
        print("Error URL: ",url)
        print("Status code: ",resp.status_code)
        return True

    document = resp.text

    ext_urls=re.findall(r'href=[\'"](https://[^\'"]+|http://[^\'"]+)',document)    
    
    for url_i in ext_urls:
        url_i = url_i.strip()
        url_i = url_i if url_i[-1] != '/' else url_i[:-1]
        
        if url_i in unique_links:
            continue
        
        temp[url_i]={}
        err_flag = get_links(url_i,temp,c_depth+1)
        
        if err_flag is True:
            temp.pop(url_i)            
        
        if len(temp.keys()) == count:
            break
    
    temp['total']=len(ext_urls)    
    

if get_links(url,data,0):
    exit('The url is bad or cant be accessed!')

print("Total unique urls extracted: %d"%len(unique_links))
            
with open('links.json','w') as fp:
    json.dump(data,fp,indent=4)
    print('Json File saved (filename: %s)'%fp.name)
    
    

import networkx as nx
import matplotlib.pyplot as plt
    

unique_links=list(unique_links)

edges=[]
node_list={}

def make_edges(url,data,node_list):
    
    temp=data[url]    
    
    if len(temp.keys()) < 1:
        return

    for url_i in temp.keys():
        if url_i == "total": continue
        edges.append((node_list[url],node_list[url_i]))
        make_edges(url_i,temp,node_list)
    
    
def make_plot_set():
        
    for index,url_i in enumerate(unique_links):
        node_list[url_i]=index+1    
  
    make_edges(url,data,node_list)
    
    print(node_list)
    print(edges)      
        

make_plot_set()
        
        
G=nx.DiGraph()
 
G.add_edges_from(edges) 

labels= {value:key for (key,value) in node_list.items()}

G=nx.relabel_nodes(G,labels)

pos=nx.spring_layout(G)

plt.figure(figsize =(10, 15))

nx.draw(G,pos,node_color ='blue') 

for node,(x,y) in pos.items():  
    print(node)
    
    plt.text(x,y,node, fontsize=10,ha='center',va='center')

plt.show()




