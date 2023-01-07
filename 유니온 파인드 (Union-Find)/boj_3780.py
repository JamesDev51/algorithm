import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def getParents(node):
    if node==parents[node]:return node
    parents[node]=getParents(parents[node])
    return parents[node]


def integrate(n1,n2):
    parents[n1]=n2
    distance[n1]+=(abs(n1-n2)%1000)

def getDistance(node):
    if node==parents[node]: return (node,0)
    ret=getDistance(parents[node])
    parents[node]=ret[0]
    distance[node]+=ret[1]
    return (parents[node],distance[node])

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        parents=list(range(n+1))
        distance=[0]*(n+1)
        while True:
            a=input().strip()
            if a=='O':break
            a=a.split()
            if a[0]=='E': print(getDistance(int(a[1]))[1])
            else:integrate(int(a[1]),int(a[2]))
            
            