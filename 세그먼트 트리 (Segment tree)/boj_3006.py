import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def init(start,end,node):
    if start==end: tree[node]=1; return tree[node]
    mid=(start+end)//2
    tree[node]=init(start,mid,node*2)+init(mid+1,end,node*2+1)
    return tree[node]

def sub_sum(start,end,node,left,right):
    if end<left or right<start: return 0
    if left<=start<=end<=right: return tree[node]
    mid=(start+end)//2
    return sub_sum(start,mid,node*2,left,right)+sub_sum(mid+1,end,node*2+1,left,right)

def update(start,end,node,index,new_value):
    if index<start or end<index: return tree[node]
    if start==end: tree[node]=new_value; return tree[node]
    mid=(start+end)//2
    tree[node]=update(start,mid,node*2,index,new_value)+update(mid+1,end,node*2+1,index,new_value)
    return tree[node]

if __name__=="__main__":
    n=int(input())
    pos=[0]*(n+1)
    for i in range(n): pos[int(input())]=i
    tree=[0]*(4*n)
    init(0,n-1,1)
    lt,rt=1,n;flag=True
    while lt<=rt:
        if flag:
            print(sub_sum(0,n-1,1,0,pos[lt]-1))
            update(0,n-1,1,pos[lt],0)
            flag=False; lt+=1
        else:
            print(sub_sum(0,n-1,1,pos[rt]+1,n-1))
            update(0,n-1,1,pos[rt],0)
            flag=True; rt-=1
            