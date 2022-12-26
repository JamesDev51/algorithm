import sys
sys.stdin = open("input.text",  "rt")
import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

def getParents(node):
    if node==parents[node]: return node
    parents[node]=getParents(parents[node])
    return parents[node]

def unionParents(n1,n2):
    N1=getParents(n1)
    N2=getParents(n2)
    if N1>=N2: parents[N1]=N2; costs[N2]=min(costs[N1],costs[N2])
    else:parents[N2]=N1; costs[N1]=min(costs[N1],costs[N2])


if __name__=="__main__":
    n,m,k=map(int,input().split())
    costs=list(map(int,input().split()))
    costs.insert(0,0)
    parents=list(range(n+1))
    for _ in range(m):
        v,w=map(int,input().split())
        unionParents(v,w)
    totalCost=0
    for node in range(1,n+1):
        if node==getParents(node):totalCost+=costs[node]
    print(totalCost if totalCost<=k else "Oh no")