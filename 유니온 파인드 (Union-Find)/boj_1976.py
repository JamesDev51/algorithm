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
    if N1>=N2: parents[N1]=N2
    else: parents[N2]=N1

def checkParentsEqual(n1,n2):
    return getParents(n1)==getParents(n2)

if __name__=="__main__":
    n=int(input())
    m=int(input())
    parents=list(range(n+1))
    for node in range(1,n+1):
        nodes=list(map(int,input().split()))
        for i in range(n):
            if nodes[i]: unionParents(node, i+1)
    plans=list(map(int,input().split()))
    for i in range(m-1):
        if not checkParentsEqual(plans[i],plans[i+1]):
            print("NO")
            exit(0)
    print("YES")