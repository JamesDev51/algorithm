import sys
sys.stdin = open("input.text",  "rt")
import sys
sys.setrecursionlimit(10000000)
input=sys.stdin.readline

def getParents(node):
    if node==parents[node]: return node
    parents[node]=getParents(parents[node])
    return parents[node]

def unionParents(n1,n2):
    N1=getParents(n1)
    N2=getParents(n2)
    if N1>=N2: parents[N1]=N2
    else: parents[N2]=N1

def checkParentsEqual(n1,n2):
    return getParents(n1)==getParents(n2)

if __name__=="__main__":
    n,m=map(int,input().split())
    parents=list(range(n+1))
    for _ in range(m):
        com,a,b=map(int,input().split())
        if not com: unionParents(a, b)
        else:print("YES" if checkParentsEqual(a,b) else "NO")
        