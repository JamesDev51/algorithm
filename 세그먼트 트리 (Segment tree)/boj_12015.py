import sys
sys.stdin = open("input.text",  "rt")
import sys

input=sys.stdin.readline

#start, end: 변화하는 시작, 끝
#node: 노드 번호
#left, right: 0~i-1
def sub_max(start,end,node,left,right):
    if end<left or right<start: return 0
    if left<=start<=end<=right: return tree[node]#범위가 전부 일치
    mid=(start+end)//2
    return max(sub_max(start,mid,node*2,left,right),sub_max(mid+1,end,node*2+1,left,right))
    

def update(start,end,node, index,lis):
    if index<start or end<index: return 0
    if start==end:
        tree[node]=lis+1
        return tree[node]
    mid=(start+end)//2
    tree[node]=max(tree[node],update(start,mid,node*2,index,lis),update(mid+1,end,node*2+1,index,lis))
    return tree[node]

def update_new(idx,lis):
    while idx:
        tree[idx]=lis
        parentIdx = idx//2
        idx = parentIdx if tree[parentIdx]<lis else 0


if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    sorted_a=[]
    for idx,val in enumerate(arr): sorted_a.append((val,idx))
    # sorted_a=sorted(sorted_a,key=lambda x:(x[0],-x[1]) )
    sorted_a.sort(key=lambda x:(x[0],-x[1]))
    
    tree=[0]*(n*4)
    for val,idx in sorted_a:
        prev_sub_max_value=sub_max(0,n-1,1,0,idx-1) if idx!=0 else 0
        update(0,n-1,1,idx,prev_sub_max_value)
    print(tree[1])

    '''

       static void update2(int idx, int num){
      while (idx != 0) {
         seg[idx] = num;
         int parentIndex = idx / 2;
         if (seg[parentIndex] < num) idx = parentIndex;
         else idx = 0;
      }
   }
    '''