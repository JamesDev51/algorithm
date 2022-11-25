import sys
sys.stdin = open("input.text",  "rt")
import sys
sys.setrecursionlimit(1000000001)
input=sys.stdin.readline

def earlyAdapter(prevNode, isEarlyAdapater):
    if dp[prevNode][isEarlyAdapater]!=-1: return dp[prevNode][isEarlyAdapater]
    
    res=0
    for nextNode in tree[prevNode]:
        if not ch[nextNode]:
            ch[nextNode]=1
            if isEarlyAdapater: res+=min(earlyAdapter(nextNode, 0),earlyAdapter(nextNode, 1))
            else: res+=earlyAdapter(nextNode, 1)
            ch[nextNode]=0
    dp[prevNode][isEarlyAdapater]=res+1 if isEarlyAdapater else res
    
    return dp[prevNode][isEarlyAdapater]

if __name__=="__main__": 
    n=int(input())
    tree=[[] for _ in range(n+1)]
    ch=[0]*(n+1)
    for _ in range(n-1): 
        u,v=map(int,input().split())
        tree[u].append(v)
        tree[v].append(u)

    ch=[0]*(n+1)
    dp=[[-1]*2 for _ in range(n+1)]

    ch[1]=1
    print(min(earlyAdapter(1,0), earlyAdapter(1,1)))
    
    