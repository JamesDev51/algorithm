import sys
sys.stdin = open("input.text",  "rt")
import sys
sys.setrecursionlimit(100000000)
input=sys.stdin.readline
from collections import deque

def dfs(node,flag):
    op,left_node,right_node=tree[node]
    ret=0
    if op=="+":
        if flag==True:
            if left_node<=n: ret+=nums.pop()
            else:ret+=dfs(left_node,True)
            if right_node<=n: ret+=nums.pop()
            else:ret+=dfs(right_node,True)
        else:
            if left_node<=n: ret+=nums.popleft()
            else:ret+=dfs(left_node,False)
            if right_node<=n: ret+=nums.popleft()
            else:ret+=dfs(right_node,False)
    else:
        if flag==True:
            if left_node<=n: ret+=nums.pop()
            else:ret+=dfs(left_node,True)
            if right_node<=n: ret-=nums.popleft()
            else:ret-=dfs(right_node,False)
        else:
            if left_node<=n: ret+=nums.popleft()
            else:ret+=dfs(left_node,False)
            if right_node<=n: ret-=nums.pop()
            else:ret-=dfs(right_node,True)
            
    return ret
        
    
if __name__=="__main__":
    n=int(input())
    tree=[[] for _ in range(2*n)]
    nums=list()
    for node in range(1,n+1):
        a=int(input())
        nums.append(a)
    nums.sort()
    nums=deque(nums)
    for node in range(n+1,2*n):
        op,left_node,right_node=input().split()
        left_node,right_node=int(left_node),int(right_node)
        tree[node]=[op,left_node,right_node]
    print(dfs(2*n-1,True))
        
    
        