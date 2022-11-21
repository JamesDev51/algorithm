import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def postorder(node):
    if tree[node][0]:postorder(tree[node][0])
    if tree[node][1]:postorder(tree[node][1])
    print(node,end=" ")
    
def restore_tree(parents,p_idx,lt,rt):
    if lt==rt:return
    if lt<p_idx:
        smallest_left_idx=float('inf')
        for i in range(lt,p_idx):
            val=inorderd[i]
            io_idx=pidx_inorderd[val]
            smallest_left_idx=min(smallest_left_idx,io_idx)
        left=preorderd[smallest_left_idx]
        tree[parents][0]=left
        restore_tree(left, inorderd.index(left), lt, p_idx-1)
        
    if p_idx<rt:
        smallest_right_idx=float('inf')
        for i in range(p_idx+1,rt+1):
            val=inorderd[i]
            io_idx=pidx_inorderd[val]
            smallest_right_idx=min(smallest_right_idx,io_idx)
        right=preorderd[smallest_right_idx]
        tree[parents][1]=right
        restore_tree(right, inorderd.index(right), p_idx+1, rt)
    
    

def solve():
    root=preorderd[0]
    restore_tree(root,inorderd.index(root),0,n-1)
    postorder(root)
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        preorderd=list(map(int,input().split()))
        inorderd=list(map(int,input().split()))
        pidx_inorderd=dict()
        for i in range(n):
            val=inorderd[i]
            pidx_inorderd[val]=preorderd.index(val)
        tree=[[0,0]  for _ in range(n+1)]
        solve()