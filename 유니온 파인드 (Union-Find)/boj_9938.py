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
    if not closet[N1]:
        parents[N2]=N1
    elif not closet[N2]:
        parents[N1]=N2

def process(a,b):
    if not closet[getParents(a)]:
        closet[getParents(a)]=1
    elif not closet[getParents(b)]:
        closet[getParents(b)]=1
    else:
        return "SMECE"
    unionParents(a,b)
    return "LADICA"
        

if __name__=="__main__":
    n,l=map(int,input().split())
    parents=list(range(l+1))
    closet=[0]*(l+1)
    for i in range(n):
        a,b=map(int,input().split())
        print(process(a,b))