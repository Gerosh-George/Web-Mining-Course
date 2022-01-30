import numpy as np
from numpy import linalg

trial = np.matrix((
                    [0,1,1,0,0],
                    [1,0,1,1,0],
                    [1,0,0,1,1],
                    [1,0,0,0,1],
                    [0,0,0,0,0]
                ))

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
             [0,1,1,0],
             [1,0,0,1],
             [1,1,0,1],
             [0,0,1,0],
            ))



# logic

print("Enter the matrix")

m1 = []
row = list(map(int,input().split()))
m1.append(row)
for i in range(len(row)-1):
	row = list(map(int,input().split()))
	m1.append(row)

m1 = np.matrix(m1)

adjac_grp = m1 # select the adjacency matrix

M = adjac_grp.T

s = np.sum(M,axis=0) # sum along the column
s = np.where(s==0,1,s) # changing any value of sum if it is zero to 1 so that we can divide

M = M / s

k = 3
d = 0.95


print("Value of d:")
d = float(input())

print("Number of iterations? :")
k = int(input())

print("\nInlink matrix: ")  # row will be authority and show the inlinks for the node
print(np.round(M,2))
print()

rank = [(1/len(M))] * len(M)

rank = np.transpose([rank])


for i in range(k):

    rank = np.dot(M,rank)
    #rank = rank / np.linalg.norm(rank)    
    rank = (1-d) + d * rank 
    print(f"[ITR No: {i+1}] Rank of the pages are: {[r for r in np.round(rank,3).T[0]]}")
    
    
rank = np.round(rank,3)

print(f"\nRank after {k} iterations")
#print(f"Rank of the pages are: {[r for r in rank.T[0]]}")
print("Rank of the pages are:")
for i,r in enumerate(rank.T[0]):
    print(f"D{i} : {r}")
