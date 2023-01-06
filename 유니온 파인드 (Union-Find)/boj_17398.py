import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def getParents(node):
    if parents[node]<0: return node
    parents[node]=getParents(parents[node])
    return parents[node]

def union(n1,n2):
    N1=getParents(n1)
    N2=getParents(n2)
    if N1==N2: return
    parents[N1]+=parents[N2]
    parents[N2]=N1

def init():
    elimCh=[0]*(m+1)
    for i in range(q):
        e=int(input())
        elimCh[e]=1
        elim.append(e)
    for i in range(1,m+1):
        if not elimCh[i]:
            n1,n2=edges[i]
            union(n1,n2)
            
def solve():
    answer=0
    for e in reversed(elim):
        n1,n2=edges[e]
        N1=getParents(n1)
        N2=getParents(n2)
        if N1!=N2:
            answer+=(parents[N1]*parents[N2])
        union(n1,n2)
    return answer        

if __name__=="__main__":
    n,m,q=map(int,input().split())
    parents=[-1]*(n+1)
    edges=[[0,0]]+[list(map(int,input().split())) for _ in range(m)]
    elim=list()
    init()
    print(solve())