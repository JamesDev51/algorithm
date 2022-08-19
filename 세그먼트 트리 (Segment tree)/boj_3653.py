import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def init(start,end,node):
    if start==end: tree[node]=1; return tree[node]
    mid=(start+end)//2
    tree[node]=init(start,mid,node*2)+init(mid+1,end,node*2+1)
    return tree[node]

def query(start,end,node,left,right):
    if end<left or right<start: return 0
    if left<=start<=end<=right: return tree[node]
    mid=(start+end)//2
    return query(start,mid,node*2,left,right)+query(mid+1,end,node*2+1,left,right)

def update(start,end,node,index,new_value):
    if index<start or end<index: return tree[node]
    if start==end: tree[node]=new_value; return tree[node]
    mid=(start+end)//2
    tree[node]=update(start,mid,node*2,index,new_value)+update(mid+1,end,node*2+1,index,new_value)
    return tree[node]

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int, input().split())
        movies=list(map(int,input().split()))
        movie_idx=list(range(n-1,-1,-1)); movie_idx.insert(0,0)
        tree=[0]*(4*(n+m))
        init(0,n-1,1)
        print(movie_idx)
        for i in range(m):
            now_movie=movies[i]
            now_movie_idx=movie_idx[now_movie]
            print(query(1,n+m,1,now_movie_idx+1,n+m),end=" ")
            update(1,n+m,1,now_movie_idx,0)
            movie_idx[now_movie]=n+i
            update(1,n+m,1,movie_idx[now_movie],1)
            print(movie_idx)
        print()
            