import re

documents =['doc1','doc2','doc3']
index={}

for id,doc in enumerate(documents):
    filename = doc+".txt"

    with open(filename,'r') as fp:
        data = "".join(fp.readlines())
        data = data.lower()
        ext_words = re.findall(r"([a-z0-9-]+)",data)
        for pos,word in enumerate(ext_words):

            if word[-1]=='s':
                if word[:-1] in index:
                    word = word[:-1]
                elif word[:-2] in index:
                    word = word[:-2]

            if word not in index:
                index[word]={   "freq":1,
                                "listing": [(id+1,pos)]
                            }
            else:
                index[word]['freq']+=1
                index[word]['listing'].append((id+1,pos))        


from collections import OrderedDict
index = OrderedDict(sorted(index.items()))
with open("inverted.txt",'w') as fp:
    for key in index:
        print(f"{key} : {index[key]}")
        fp.write(f"{key} : {index[key]}\n")  
        



