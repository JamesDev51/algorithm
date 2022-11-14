import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def dfs(deleted):
    global leaf_flag
    stack=[]; stack.append(deleted)
    ch=[0]*(n); ch[deleted]=1

    if deleted>0 and leaf_flag[deleted] and len(tree[tree_rev[deleted]])==1:
        leaf_flag[tree_rev[deleted]]=1
    leaf_flag[deleted]=0
    while stack:
        node=stack.pop()
        for child in tree[node]:
            if not ch[child]:
                if deleted>0 and leaf_flag[deleted] and len(tree[tree_rev[deleted]])==1:
                    leaf_flag[tree_rev[deleted]]=1
                ch[child]=1
                leaf_flag[child]=0
                stack.append(child)
    return sum(leaf_flag)
    

if __name__=="__main__":
    n=int(input())
    tree_rev=list(map(int,input().split()))
    deleted=int(input())
    tree=[[] for _ in range(n)] 
    for child in range(n): 
        if tree_rev[child]!=-1:tree[tree_rev[child]].append(child)
    leaf_flag=[0]*n
    for node in range(n):
        if not tree[node]:leaf_flag[node]=1
    
    print(dfs(deleted))