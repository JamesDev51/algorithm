import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def init(start,end,node):
    if start==end: tree[node]=arr[start]; return tree[node]
    mid=(start+end)//2
    tree[node]=(init(start,mid,node*2)*init(mid+1,end,node*2+1))%mod
    return tree[node]

def sub_mul(start,end,node,left,right):
    if end<left or right<start: return 1
    if left<=start<=end<=right: return tree[node]
    mid=(start+end)//2
    return (sub_mul(start,mid,node*2,left,right)*sub_mul(mid+1, end, node*2+1, left, right))%mod

def update(start,end,node,index,new_val):
    if index<start or end<index: return tree[node]
    if start==end: tree[node]=new_val; return tree[node]
    mid=(start+end)//2
    tree[node]=(update(start,mid,node*2,index,new_val)*update(mid+1,end,node*2+1,index,new_val))%mod
    return tree[node]

if __name__=="__main__":
    mod=1000000007
    n,m,k=map(int,input().split())
    arr=list(int(input()) for _ in range(n))
    tree=[0]*(4*n)
    init(0,n-1,1)
    for _ in range(m+k):
        a,b,c=map(int,input().split())
        if a==1:update(0,n-1,1,b-1,c)
        else:print(sub_mul(0,n-1, 1, b-1, c-1)%mod)