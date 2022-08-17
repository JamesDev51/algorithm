import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


def init(start,end,node):
    if start==end:tree[node]=arr[start]; return tree[node]
    mid=(start+end)//2
    tree[node]=init(start,mid,node*2)+init(mid+1,end,node*2+1)
    return tree[node]

def sub_sum(start,end,node,left,right):
    if end<left or right<start: return 0
    if left<=start<=end<=right: return tree[node]
    mid=(start+end)//2
    return sub_sum(start,mid,node*2,left,right)+sub_sum(mid+1,end,node*2+1,left,right)

def update(start,end,node, index, new_value):
    if index<start or end<index: return tree[node]
    if start==end: tree[node]=new_value; return tree[node]
    mid=(start+end)//2
    tree[node]=update(start,mid,node*2,index,new_value)+update(mid+1,end,node*2+1,index,new_value)
    return tree[node]

if __name__=="__main__":
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    tree=[0]*(4*n)
    init(0,n-1,1)
    for _ in range(q):
        x,y,a,b=map(int,input().split())
        if x<=y: print(sub_sum(0,n-1,1,x-1,y-1))
        else: print(sub_sum(0,n-1,1,y-1,x-1))
        update(0,n-1,1,a-1,b)
        