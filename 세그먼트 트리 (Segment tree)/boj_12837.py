import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def sub_money(start,end,node,left,right):
    if end<left or right<start:return 0
    if left<=start<=end<=right: return tree[node]
    mid=(start+end)//2
    return sub_money(start, mid, node*2, left, right)+sub_money(mid+1, end, node*2+1, left, right)

def update(start,end,node,index,diff):
    if index<start or end<index: return
    tree[node]+=diff
    if start!=end:
        mid=(start+end)//2
        update(start,mid,node*2,index,diff);update(mid+1,end,node*2+1,index,diff)
        
if __name__=="__main__":
    n,q=map(int,input().split())
    tree=[0]*(4*n)
    arr=[0]*(n+1)
    for _ in range(q):
        a,b,c=map(int, input().split())
        if a==1:
            diff=c-arr[b]
            arr[b]+=c
            update(1,n,1,b,c)
        else:
            print(sub_money(1, n, 1, b, c))