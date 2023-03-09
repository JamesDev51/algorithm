import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def inorder(node,row):
    global col
    if tree[node][0]!=-1:inorder(tree[node][0],row+1)
        
    col_max[row]=max(col_max[row],col)
    col_min[row]=min(col_min[row],col)
    col+=1
    
    if tree[node][1]!=-1:inorder(tree[node][1],row+1)
        

if __name__=="__main__":
    n=int(input())
    tree=[[-1,-1] for _ in range(n+1)]
    tail=[0]*(n+1)
    for _ in range(n):
        node,left,right=map(int,input().split())
        if left!=-1:tree[node][0]=left;tail[left]+=1
        if right!=-1:tree[node][1]=right;tail[right]+=1
    col=1
    col_max=[float('-inf')]*(n+1)
    col_min=[float('inf')]*(n+1)
    
    root=-1
    for node in range(1,n+1):
        if tail[node]==0:root=node;break

    inorder(root,1)
    
    row=-1
    largest=float('-inf')
    for key in range(1,n+1):
        if col_max[key]-col_min[key]+1>largest:
            largest=col_max[key]-col_min[key]+1
            row=key
    print(row,largest)
        
    