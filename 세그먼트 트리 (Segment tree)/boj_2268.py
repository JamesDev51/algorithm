import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def sub_sum(start,end,node,left,right):
    if end<left or right<start: return 0
    if left<=start<=end<=right: return tree[node]
    mid=(start+end)//2
    return sub_sum(start,mid,node*2,left,right)+sub_sum(mid+1,end,node*2+1,left,right)
    

def update(start,end,node,index,diff):
    if index<start or end<index: return tree[node]
    tree[node]+=diff
    if start!=end:
        mid=(start+end)//2
        update(start,mid,node*2,index,diff)
        update(mid+1,end,node*2+1,index,diff)
        

if __name__=="__main__":
    n,m=map(int,input().split())    
    arr=[0]*n
    tree=[0]*(4*n)
    
    for _ in range(m):
        a,b,c=map(int,input().split())
        if a==0:
            if b<=c: print(sub_sum(0,n-1,1,b-1,c-1))
            else: print(sub_sum(0,n-1,1,c-1,b-1))
        else:
            diff=c-arr[b-1]
            arr[b-1]=c
            update(0,n-1,1,b-1,diff)
            
        