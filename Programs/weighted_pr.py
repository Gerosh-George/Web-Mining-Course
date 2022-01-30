import math

m1 = [[0, 1, 0, 0, 1], 
	  [0, 0, 0, 0, 1], 
	  [1, 0, 0, 1, 1], 
	  [0, 1, 0, 0, 0], 
	  [1, 0, 0, 1, 0]]

m2 = [[0, 1, 1, 0], 
	  [0, 0, 1, 0], 
	  [1, 0, 0, 0], 
	  [0, 0, 1, 0]]

m3 = [[0, 1, 1, 1, 0, 0, 0, 0], 
	  [1, 0, 0, 0, 0, 0, 0, 0], 
	  [1, 0, 0, 0, 0, 0, 0, 0], 
	  [1, 0, 0, 0, 1, 1, 1, 1],
	  [0, 0, 0, 0, 0, 0, 0, 0], 
	  [0, 0, 0, 0, 0, 0, 0, 0], 
	  [0, 0, 0, 0, 0, 0, 0, 0], 
	  [0, 0, 0, 0, 0, 0, 0, 0]]

def win(matrix, m, o):
	k = 0
	for i in range(0, n):
		if(int(matrix[i][o]) == 1):
			k = k+1
	l = 0
	for i in range(0, n):
		if(int(matrix[m][i] == 1)):
			for j in range(0, n):
				if(matrix[j][i] == 1):
					l = l+1
	
	#print(f"in ({m+1}-{o+1}) : {k}-{l-k}")
	#print(f"in ({m+1}-{o+1}) : {k}/{l}")
	print("in (%d-%d) : %d/%d"%(m+1,o+1,k,l))
	return float(k/l)


def wout(matrix, m, o):
	k = 0
	for i in range(0, n):
		if(int(matrix[o][i]) == 1):
			k = k+1
	if k==0:
		k=0.01
	l = 0
	for i in range(0, n):
		if(int(matrix[m][i] == 1)):
			
			flag = True
			for j in range(0, n):
				if(matrix[i][j] == 1):
					flag=False
					l = l+1
			
			if flag:
				l = l + 0.01 # no outlink present
				#print(f"[info] Node: {i+1} no outlink")

	#print(f"out ({m+1}-{o+1}) : {k}-{round(l-k,2)}")
	#print(f"out ({m+1}-{o+1}) : {k}/{round(l,2)}")
	print("out (%d-%d) : %d/%d"%(m+1,o+1,k,round(l,2)))
	return float(k/l)


def pagerank(matrix, o, n, p):
	a = 0
	for i in range(0, n):
		if(int(matrix[i][o]) == 1):
			k = 0
			for s in range(0, n):

				if(matrix[i][s] == 1):
					k=k+1
			
			win_v  = win(matrix, i, o)
			wout_v = wout(matrix, i, o)
			a = a+float((p[i])*win_v*wout_v)
			#print(f"[{o+1}]  in:{win_v}   out:{wout_v}   {i+1}={o+1}")
            

	return a


print("Enter the matrix")

m1 = []
row = list(map(int,input().split()))
m1.append(row)
for i in range(len(row)-1):
	row = list(map(int,input().split()))
	m1.append(row)


matrix = m1
n = len(matrix)



d = 0.85 # damping factor

o = 3

print("Value of d:")
d = float(input())

print("Number of iterations? :")
o = int(input())

print("\nNumber of iterations is:", o,"\n")

sum1 = 0
p = []

for i in range(0, n):
	p.append(1/n)
for k in range(0, o):
	update = p.copy()
	for u in range(0, n):
		g = pagerank(matrix, u, n, p)
		update[u] = (1-d)+d*g
	#print(f"[{k+1}] Updated rank: {[round(r,4) for r in update]}")
	p = update.copy()
	
	print("Iteration num: %d"%(k+1))
	for i in range(0, n):
		sum1 += p[i]		
		print("Page rank of node ", i+1, "is : ", round(p[i],3))
	print("Sum of all page ranks: ", sum1)
	print("\n\n")
