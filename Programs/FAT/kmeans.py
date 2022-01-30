
import numpy as np

datasets = {}

def load_dataset():
    
   
    datasets[1]={}
    filename = "documents" + ".txt"
    documents = []
    content_words = []

    with open(filename,"r") as fp:

        for line in fp.readlines():
            if len(line)> 1:

                if not line.startswith('CW:'):
                    documents.append((line.replace(".\n","")).lower())
                else:
                    content_words = line.split()
                    content_words = content_words[1:]
                    content_words = [ w.lower() for w in content_words]
    
    documents_vsm = []
  
    for doc in documents:
        vsm = VSM(doc,content_words)
        documents_vsm.append(vsm)

    datasets[1]['VSM'] = documents_vsm    
    datasets[1]['cluster'] = [0] * len(documents)     

    return datasets


def VSM(document,content_words):
    vsm = []
    for word in content_words:
        vsm.append(document.count(word))
    return vsm

def Euclid_Dist(VSM):

    dist_mat = []
    dist_row = []

    for i in range(len(VSM)):

        x = np.array(VSM[i])
        dist_row = [0] * (i+1)

        for j in range(i+1,len(VSM)):
            
            y = np.array(VSM[j])
            dist = np.round(np.linalg.norm(x-y),3)
            dist_row.append(dist)
        dist_mat.append(dist_row)
    
    return np.matrix(dist_mat)



def calculate_new_centroids(VSM,K,clusters):

    unique = [ i for i in range(K) ]
    centroids = []
        
    for cid in unique:
        centroid = np.zeros(len(VSM[0]))
        for index,c in enumerate(clusters):
            if cid == c:
                point = np.array(VSM[index], dtype='int64')
                centroid = centroid + point
        count = clusters.count(cid)
        if count == 0:
            count = 1
        centroid = centroid / count
        centroids.append(centroid)
    
    return centroids

def list_equal(l1,l2):
    
    for i in range(len(l1)):
        if l1[i]!=l2[i]:
            return False
    
    return True

def Kmeans(VSM,K):

    centroids = [VSM[0],VSM[1],VSM[2],VSM[3]] # using first 4 docs as initial centroids

    print("[INFO] Initial Centroids [Taking VSM of first 4 documents]:")
    for row in centroids:
        print(row)
    print("\n")
    

    final_clusters = [-1]*len(VSM)

    print(f"[INFO] Initial Clusters: {final_clusters}")
    
    while(True):

        clusters = []        

        for i,vec in enumerate(VSM):
        
            distances=[]

            for centroid in centroids:
                x = np.array(vec)
                y = np.array(centroid)
                dist = np.round(np.linalg.norm(x-y),3)
                distances.append(dist)

            print(f"[INFO] Doc{i+1} Distance centroid vector: {distances}")
            clusters.append(np.argmin(distances,axis=0))
            
        
        print(f"[INFO] Clusters formed: {clusters}")

        if list_equal(final_clusters,clusters):
            print("\n[INFO] Clusters formed in this iteration is same to one before so terminating")
            break

        final_clusters = clusters

        print("\nNext Iteration\n")

        # calculate new centroids
        unique = set(clusters)
        centroids = []

        centroids = calculate_new_centroids(VSM,K, clusters)

        print("[INFO] New Centroids:")
        for row in centroids:
            row = np.array(row)
            print(list(np.round(row,3)))
        print("\n")

    return final_clusters


def init(K=2):

    if K==1:
        K=2

    datasets = load_dataset()

    
    doc = 1

    print(f"\nVSM of all 12 documents: \n")
    for row in datasets[doc]['VSM']:
        print(row)
    print("\n")

    print("Euclidean Distance Matrix:\n")
    m = Euclid_Dist(datasets[doc]['VSM'])
    print(m)
    print("\n")

   
    clusters = Kmeans(datasets[doc]['VSM'],K)

    print(f"\nResult of Kmeans cluster with K ({K}): ",end="")
    print(clusters)
    print("\n")


K = int(input('Enter the value of K: '))
print()
init(K)
