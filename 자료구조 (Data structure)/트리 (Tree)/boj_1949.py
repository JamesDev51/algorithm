import sys
sys.stdin = open("input.text",  "rt")
import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

def good_town(prev_node,isGoodTown):
    
    if memo[prev_node][isGoodTown]!=-1:return memo[prev_node][isGoodTown]
    res=0
    
    for nextNode in tree[prev_node]:
        if not ch[nextNode]:
            sub_res=0
            ch[nextNode]=1
            sub_res=max(sub_res,good_town(nextNode,0))
            if not isGoodTown: 
                sub_res=max(sub_res,good_town(nextNode,1)+p[nextNode-1])
            res+=sub_res
            ch[nextNode]=0
    
    memo[prev_node][isGoodTown]=res
    return res

if __name__=="__main__":
    n=int(input())
    p=list(map(int,input().split()))
    tree=[[] for _ in range(n+1)]
    for _ in range(n-1):
        n1,n2=map(int,input().split())
        tree[n1].append(n2)
        tree[n2].append(n1)
    memo=[[-1,-1] for _ in range(n+1)]
    ch=[0]*(n+1)
    ch[1]=1
    print(max(good_town(1,1)+p[0], good_town(1,0)))