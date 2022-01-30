
t=int(input())

for _ in range(t):
    N,K,M = map(int,input().split())
    a=[0]*M
    s=0
    b=[]
    for _ in range(min(N+1,M)):
        index = s % M
        s+=K
        a[index]+=1
        b.append(index)

    d = N+1-M

     

    if d>=M:
        
        g1 = d//M
        g2 = d%M

        for i in range(M):
            a[i]+= int(g1)

        for i in range(g2):
            a[b[i]]+=1

    else:
        for i in range(d):
            a[b[i]]+=1


    for n in a:
        print(n,end=' ')
    print()


