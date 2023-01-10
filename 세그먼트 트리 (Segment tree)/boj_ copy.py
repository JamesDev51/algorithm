import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def init(start,end,node):
    if start==end: 
        if start<n:tree[node]=1
        return tree[node]
    mid=(start+end)//2
    tree[node]=init(start,mid,node*2)+init(mid+1,end,node*2+1)
    return tree[node]

def sub_sum(start,end,node,left,right):
    if end<left or right<start:return 0
    if left<=start<=end<=right: return tree[node]
    mid=(start+end)//2
    return sub_sum(start,mid,node*2,left,right)+sub_sum(mid+1,end,node*2+1,left,right)

def update(start,end,node,idx,new_value):
    if idx<start or end<idx: return tree[node]
    if start==end: tree[node]=new_value; return tree[node]
    mid=(start+end)//2
    tree[node]=update(start,mid,node*2,idx,new_value)+update(mid+1,end,node*2+1,idx,new_value)
    return tree[node]

def solve():
    global last_idx
    for i in range(m):
        movie=movies[i]
        answer.append(sub_sum(0,tree_size,1,pos[movie]+1,tree_size))

        update(0,tree_size,1,pos[movie],0) #기존 있던 곳을 0으로 바꿈
        pos[movie]=i+n #새로운 인덱스 할당
        update(0,tree_size,1,pos[movie],1) #새로운 곳을 1로 바꿈xxx


if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().split())
        movies=list(map(int,input().split()))
        pos=[0]*(n+1)
        for i in range(1,n+1):pos[i]=n-i
        tree_size=n+m
        tree=[0]*(4*tree_size)
        init(0,tree_size,1)

        answer=[]
        solve()
        print(*answer)