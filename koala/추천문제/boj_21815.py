import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


def find_parents(node):
    if node==parents[node]:return node
    parents[node]=find_parents(parents[node])
    return parents[node]
def union_parents(n1,n2):
    N1=find_parents(n1)
    N2=find_parents(n2)
    if N1<=N2:parents[N2]=N1
    else:parents[N1]=N2
def is_same_parents(n1,n2):
    return find_parents(n1)==find_parents(n2)

if __name__=="__main__":
    n=int(input())
    a=[list(map(int,input().split())) for _ in range(n)]
    parents=list(range(2*n+1))
    for c,p1,p2,p3,p4 in a:
        union_parents(p1, p2)
        union_parents(p3, p4)
    a.sort(key=lambda x:x[0])
    res=0
    for c,p1,p2,p3,p4 in a:
        if not is_same_parents(p1, p3):union_parents(p1, p3);res+=c
    print(res)
                
            
    
    