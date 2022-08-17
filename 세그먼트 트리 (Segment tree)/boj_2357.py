import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def init_max(start,end,node):
    if start==end: max_tree[node]=arr[start]; return max_tree[node] #자기 자신이 최대값
    mid=(start+end)//2
    max_tree[node]=max(init_max(start,mid, node*2), init_max(mid+1, end, node*2+1))
    return max_tree[node]

def sub_max(start,end,node,left,right):
    if end<left  or right<start: return -1e9 #범위가 아니면 최소값을 리턴하기
    if left<=start<=end<=right: return max_tree[node] #범위 안이면 노드 값 리턴
    mid=(start+end)//2
    return max(sub_max(start,mid,node*2,left,right),sub_max(mid+1, end, node*2+1, left, right))

def init_min(start,end,node):
    if start==end: min_tree[node]=arr[start]; return min_tree[node] #자기 자신이 최소값
    mid=(start+end)//2
    min_tree[node]=min(init_min(start,mid, node*2), init_min(mid+1, end, node*2+1))
    return min_tree[node]

def sub_min(start,end,node,left,right):
    if end<left or right<start: return 1e9 #범위가 아니면 최대값을 리턴하기
    if left<=start<=end<=right: return min_tree[node] #범위 안이면 노드 값 리턴
    mid=(start+end)//2
    return min(sub_min(start,mid,node*2,left,right),sub_min(mid+1, end, node*2+1, left, right))


if __name__=="__main__":
    n,m=map(int,input().split())
    arr=list(int(input()) for _ in range(n))
    max_tree=[0]*(4*n); min_tree=[0]*(4*n)
    init_max(0,n-1,1); init_min(0,n-1,1)
    for _ in range(m):
        a,b=map(int,input().split())
        print(sub_min(0, n-1, 1, a-1, b-1),sub_max(0, n-1, 1, a-1, b-1))
        