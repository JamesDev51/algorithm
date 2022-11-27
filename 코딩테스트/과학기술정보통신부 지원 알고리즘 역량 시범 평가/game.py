# import sys
# sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

def getParents(node):
    if node==parents[node]: return node
    parents[node]=getParents(parents[node])
    return parents[node]

def findParents(n1,n2):
    if getParents(n1)==getParents(n2):return True
    return False

def arrangeParents():
    for node in range(1,n+1): parents[node]=getParents(node)

def unionParents(n1,n2):
    N1=getParents(n1)
    N2=getParents(n2)
    
    if not prime[N1] and not prime[N2]:
        if N1<N2: parents[N2]=N1
        else: parents[N1]=N2
    elif prime[N1] and prime[N2]:
        if N1>N2: parents[N2]=N1
        else: parents[N1]=N2
    else:
        if not prime[N1]: parents[N2]=N1
        else: parents[N1]=N2
        
    if parents[N2]==N1:
        unionSize[parents[N1]]+=unionSize[N2]
        unionSize[N2]=0
    else:
        unionSize[parents[N2]]+=unionSize[N1]
        
    

    
def initPrime():
    prime[1]=1
    for i in range(2,n+1):
        if prime[i]: continue
        flag=True
        for j in range(2,i):
            if i%j==0:
                flag=False
                prime[i]=1
                break
        if flag: 
            for k in range(i+i,n+1,i): prime[k]=1
            

n,k=map(int,input().split())
parents=list(range(n+1))
unionSize=[1]*(n+1)
prime=[0]*(n+1) #소수는 0 아니면 1
initPrime()
for _ in range(k):
    p1,p2=map(int,input().split())
    if findParents(p1,p2):print(0)
    else:
        unionParents(p1,p2)
        arrangeParents()
        print(parents[p1],unionSize[parents[p1]])
