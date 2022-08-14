import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def sub_max(start,end,node,left,right):
    if end<left or right<start: return 0
    if left<=start<=end<=right: return tree[node]
    mid=(start+end)//2
    return max(sub_max(start,mid,node*2,left,right),sub_max(mid+1,end,node*2+1,left,right))

def update(start,end,node,index,lis):
    if index<start or end<index:return tree[node]
    if start==end: tree[node]=lis+1; return tree[node]
    mid=(start+end)//2
    tree[node]=max(tree[node],update(start,mid,node*2,index,lis),update(mid+1,end,node*2+1,index,lis))
    return tree[node]
if __name__=="__main__":
    try:
        while True:
            n=int(input())
            arr=list(map(int,input().split()))
            tree=[0]*(4*n)
            sorted_arr=[]
            for idx,val in enumerate(arr): sorted_arr.append((val,idx))
            sorted_arr=sorted(sorted_arr, key=lambda x:(x[0],-x[1]))
            res=float('-inf')
            for val,idx in sorted_arr:
                if idx==0: sub_max_val=0
                else: sub_max_val=sub_max(0,n-1,1,0,idx-1)

                res=max(res,update(0,n-1,1,idx,sub_max_val))
            print(res)
            
    except Exception: pass
    