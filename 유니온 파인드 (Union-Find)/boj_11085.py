import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

def getParents(node):
    if node==parents[node]: return node
    parents[node]=getParents(parents[node])
    return parents[node]

def unionParents(n1,n2):
    N1=getParents(n1)
    N2=getParents(n2)
    if N1<N2:parents[N2]=N1
    else: parents[N1]=N2

def checkParents(n1,n2):
    return getParents(n1)==getParents(n2)
                

def solve():
    for s,e,cost in paths:
        unionParents(s,e)
        if checkParents(c,v): return cost

if __name__=="__main__":
    p,w=map(int,input().split())
    c,v=map(int,input().split())
    paths=[list(map(int,input().split()))  for _ in range(w)]
    paths.sort(key=lambda x:-x[2])
    parents=list(range(p))
    print(solve())