import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

'''
왼쪽 비용 = 왼쪽 나무 갯수 * 현재 idx - 왼쪽 나무들의 합
오른쪽 비용 =  오른쪽 나무들의 합 - 오른쪽 나무 갯수 * 현재 idx
'''
def update_cnt(start,end,node,index,new_value):
    if index<start or end<index: return cnt_tree[node]
    if start==end: cnt_tree[node]+=new_value; return cnt_tree[node]
    mid=(start+end)//2
    cnt_tree[node]=update_cnt(start,mid,node*2,index,new_value)+update_cnt(mid+1,end,node*2+1,index,new_value)
    return cnt_tree[node]

def update_sum(start,end,node,index,new_value):
    if index<start or end<index: return sum_tree[node]
    if start==end: sum_tree[node]+=new_value; return sum_tree[node]
    mid=(start+end)//2
    sum_tree[node]=update_sum(start,mid,node*2,index,new_value)+update_sum(mid+1,end,node*2+1,index,new_value)
    return sum_tree[node]

def sub_cnt(start,end,node,left,right):
    if end<left or right<start: return 0
    if left<=start<=end<=right: return cnt_tree[node]
    mid=(start+end)//2
    return sub_cnt(start,mid,node*2,left,right)+sub_cnt(mid+1,end,node*2+1,left,right)
def sub_sum(start,end,node,left,right):
    if end<left or right<start: return 0
    if left<=start<=end<=right: return sum_tree[node]
    mid=(start+end)//2
    return sub_sum(start,mid,node*2,left,right)+sub_sum(mid+1,end,node*2+1,left,right)
    

if __name__=="__main__":
    mod=1000000007; max_value=2*10^5
    n=int(input())
    arr=list(int(input()) for _ in range(n))
    cnt_tree=[0]*(4*max_value); sum_tree=[0]*(4*max_value)
    res=1
    for i in range(n):
        cost=0
        cost+=(sub_cnt(0,max_value,1,0,arr[i]-1)*arr[i]-sub_sum(0,max_value,1,0,arr[i]-1))
        cost+=(sub_sum(0,max_value,1,arr[i]+1,max_value)-sub_cnt(0,max_value,1,arr[i]+1,max_value)*arr[i])    
        print(cost)
        if i!=0:res*=(cost%mod)
        update_cnt(0,max_value,1,arr[i],1)
        update_sum(0,max_value,1,arr[i],arr[i])
    print(res%mod)