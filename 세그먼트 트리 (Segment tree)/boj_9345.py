import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def init(start,end,node,div):
    if start==end:
        if div:max_tree[node]=start 
        else: min_tree[node]=start
        return start
    mid=(start+end)//2
    if div:max_tree[node]=max(init(start,mid,node*2,div),init(mid+1,end,node*2+1,div));return max_tree[node]
    else: min_tree[node]=min(init(start,mid,node*2,div),init(mid+1,end,node*2+1,div));return min_tree[node]

def update(start,end,node,index,new_value,div):
    if index<start or end<index: return max_tree[node] if div else min_tree[node]
    if start==end:
        if div: max_tree[node]=new_value; return max_tree[node]
        else: min_tree[node]=new_value; return min_tree[node]
    mid=(start+end)//2
    if div:max_tree[node]=max(update(start,mid,node*2,index,new_value,div),update(mid+1,end,node*2+1,index,new_value,div)); return max_tree[node]
    else :min_tree[node]=min(update(start,mid,node*2,index,new_value,div),update(mid+1,end,node*2+1,index,new_value,div)); return min_tree[node]

def find(start,end,node,left,right,div):
    if end<left or right<start: return float('-inf') if div else float('inf')
    if left<=start<=end<=right: return max_tree[node] if div else min_tree[node]
    mid=(start+end)//2
    return max(find(start,mid,node*2,left,right,div),find(mid+1,end,node*2+1,left,right,div)) if div else min(find(start,mid,node*2,left,right,div),find(mid+1,end,node*2+1,left,right,div)) 

if __name__=="__main__":
    for _ in range(int(input())):
        n,k=map(int,input().split())
        book=list(range(n))
        max_tree=[0]*4*n
        min_tree=[0]*4*n
        init(0,n-1,1,1)
        init(0,n-1,1,0)
        for _ in range(k):
            q,a,b=map(int,input().split())
            if q==0:
                book[a],book[b]=book[b],book[a]
                update(0,n-1,1,a,book[a],1)
                update(0,n-1,1,b,book[b],1)
                update(0,n-1,1,a,book[a],0)
                update(0,n-1,1,b,book[b],0)
                
            else:
                largest=find(0,n-1,1,a,b,1)
                smallest=find(0,n-1,1,a,b,0)
                print("YES" if largest==max(a,b) and smallest==min(a,b) else "NO")