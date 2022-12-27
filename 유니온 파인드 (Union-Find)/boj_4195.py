import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def getParents(node):
    if node==parents[node]: return node
    parents[node]=getParents(parents[node])
    return parents[node]

def unionParents(n1,n2):
    N1=getParents(n1)
    N2=getParents(n2)
    if N1>N2:
        parents[N1]=N2
        cnt[N2]+=cnt[N1]
        return N2
    elif N1<N2:
        parents[N2]=N1
        cnt[N1]+=cnt[N2]
        return N1
    else: return N1
    


if __name__=="__main__":
    for _ in range(int(input())):
        parents=dict()
        cnt=dict()
        for __ in range(int(input())):
            n1,n2=input().split()
            if n1 not in parents: parents[n1]=n1; cnt[n1]=1
            if n2 not in parents: parents[n2]=n2; cnt[n2]=1
            print(cnt[unionParents(n1,n2)])
            