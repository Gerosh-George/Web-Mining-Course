### "python.languageServer": "Pylance"

# hyperlink-Induced Topic Search

# Rows denote Hub links [Outlinks]
# Columns denote Authority links [Inlinks]

import numpy as np

# adjancency matrix for Q1 
ag1 = np.matrix((
             [0,0,1,0,0,0,0],
             [0,0,1,0,0,0,0],
             [1,0,0,1,0,0,0],
             [0,0,0,0,1,0,0],
             [0,0,0,0,0,0,1],
             [0,0,0,0,0,0,1],
             [0,0,0,1,1,0,0]
            ))

# adjancency matrix for Q2
ag2 = np.matrix((
             [0,0,1,0,0,0,0],
             [0,1,1,0,0,0,0],
             [1,0,1,1,0,0,0],
             [0,0,0,1,1,0,0],
             [0,0,0,0,0,0,1],
             [0,0,0,0,0,1,1],
             [0,0,0,1,1,0,1]
            ))

# adjancency matrix for Q3
ag3= np.matrix((
             [0,0,1,0,0,0,0],
             [0,1,1,0,0,0,0],
             [1,0,1,2,0,0,0],
             [0,0,0,1,1,0,0],
             [0,0,0,0,0,0,1],
             [0,0,0,0,0,1,1],
             [0,0,0,2,1,0,1]
            ))

ag4 = np.matrix((
             [0,1,1,1],
             [0,0,1,1],
             [1,0,0,1],
             [0,0,0,0],
            ))



# logic from here

adjac_grp = ag4 # equate to the required adjacency matrix

print("Adjacency Graph: ")

for row in adjac_grp:
    print(row)


hub_scores  = np.transpose([[1]* len(adjac_grp)])
auth_scores = np.transpose([[1]* len(adjac_grp)])

hub_scores  =  np.round(hub_scores / np.sum(hub_scores),2)
auth_scores = np.round(auth_scores / np.sum(auth_scores),2)


### for norm: np.linalg.norm(hub_scores)
#hub_scores = np.round(hub_scores / np.linalg.norm(hub_scores) ,3)
#auth_scores = np.round(auth_scores / np.linalg.norm(auth_scores) , 3)


adjac_grp_T = np.transpose(adjac_grp)

K=2

for i in range(K):
    new_hub_scores = np.dot(adjac_grp,auth_scores)   # Outlinks * authority rank or score
    new_auth_scores = np.dot(adjac_grp_T,hub_scores) # Inlinks * hub rank or score

    hub_scores = new_hub_scores
    auth_scores = new_auth_scores

    hub_scores  =  np.round(hub_scores / np.sum(hub_scores),2)
    auth_scores = np.round(auth_scores / np.sum(auth_scores),2)

    #hub_scores = np.round(hub_scores / np.linalg.norm(hub_scores) ,3)
    #auth_scores = np.round(auth_scores / np.linalg.norm(auth_scores) , 3)

print(f"\nScores after {K} iterations")
print(f"Authority Scores: {[s for s in auth_scores.T[0]]}")
print(f"Hub Scores: {[s for s in hub_scores.T[0]]}")






