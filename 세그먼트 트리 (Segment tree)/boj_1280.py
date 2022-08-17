import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def update(start,end,node,index):
    if index<start or end<index: return
    cnt_tree[node]+=1; sum_tree[node]+=index
    if start!=end:
        mid=(start+end)//2
        update(start,mid,node*2,index); update(mid+1,end,node*2+1,index)
def sub_cnt_sum(tree,start,end,node,left,right):
    if end<left or right<start: return 0
    if left<=start<=end<=right: return tree[node]
    mid=(start+end)//2
    return sub_cnt_sum(tree,start,mid,node*2,left,right)+sub_cnt_sum(tree,mid+1,end,node*2+1,left,right)

if __name__=="__main__":
    mod=1000000007; max_val=pow(10,5)*2
    n=int(input())
    cnt_tree=[0]*(4*max_val+1); sum_tree=[0]*(4*max_val+1)
    res=1
    for idx in range(1,n+1):
        tree_idx=int(input())
        update(0,max_val,1,tree_idx) 
        if idx==1: continue
        left=(tree_idx*sub_cnt_sum(cnt_tree,0,max_val,1,0,tree_idx-1)-sub_cnt_sum(sum_tree,0,max_val,1,0,tree_idx-1))%mod
        right=(sub_cnt_sum(sum_tree,0,max_val,1,tree_idx+1,max_val)-tree_idx*sub_cnt_sum(cnt_tree,0,max_val,1,tree_idx+1,max_val))%mod
        res=(res*(left+right)%mod)%mod
    print(res%mod)
