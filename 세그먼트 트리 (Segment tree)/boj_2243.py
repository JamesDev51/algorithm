import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def put_in(start,end,node,index,diff_value):
    if index<start or end<index: return tree[node]
    if start==end: tree[node]+=diff_value; return tree[node]
    mid=(start+end)//2
    tree[node]=put_in(start,mid,node*2,index,diff_value)+put_in(mid+1,end,node*2+1,index,diff_value)
    return tree[node]

def get_out(start,end,node,rank):
    if start==end: return start
    pivot=tree[node*2]
    mid=(start+end)//2
    if rank<=pivot: return get_out(start,mid,node*2,rank)
    else: return get_out(mid+1,end,node*2+1,rank-pivot)

if __name__=="__main__":
    limit=pow(10,6)+1
    tree=[0]*4*limit
    for _ in range(int(input())):
        inputs=map(int,input().split())
        a=next(inputs)
        b=next(inputs)
        if a==1:
            ret=get_out(0,limit-1,1,b)
            print(ret)
            put_in(0,limit-1,1,ret,-1)
        else:
            c=next(inputs)
            put_in(0,limit-1,1,b,c)