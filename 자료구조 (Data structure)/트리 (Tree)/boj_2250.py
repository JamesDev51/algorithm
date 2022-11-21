import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def inorder(node,depth):
    global cnt
    left,right=tree[node]

    if left!=-1:inorder(left,depth+1)

    depth_width[depth][1]=min(depth_width[depth][1], cnt)
    depth_width[depth][2]=max(depth_width[depth][2], cnt)
    cnt+=1

    if right!=-1: inorder(right,depth+1)

if __name__=="__main__":
    n=int(input())
    tail=[0]*(n+1)
    tree=[[] for _ in range(n+1)]
    for _ in range(n):
        node,left,right=map(int,input().split())
        tree[node]=[left,right]
        if left!=-1: tail[left]+=1; 
        if right!=-1:tail[right]+=1
    root=-1
    for node in range(1,n+1):
        if tail[node]==0:root=node;break
    depth_width=[[depth, float('inf'),float('-inf')] for depth in range(n+1)]
    cnt=1
    inorder(root,1)
    
    depth_width.sort(key=lambda x:(-(x[2]-x[1]), x[0]))
    

    print(depth_width[0][0],depth_width[0][2]-depth_width[0][1]+1)
    

        