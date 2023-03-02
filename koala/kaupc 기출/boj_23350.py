import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline


if __name__=="__main__":
    n,m=map(int,input().split())
    p_cnt=[0]*(m+1)
    stack,tmp_stack=[],[]
    que=deque()
    ans=0
    for _ in range(n):
        p,w=map(int, input().split())
        que.append((p,w))
        p_cnt[p]+=1
    while m:
        p,w=que.popleft()
        if p<m: 
            que.append((p,w))
            ans+=w
            continue
        
        while stack and stack[-1][0]==p and stack[-1][1]<w:
            poped=stack.pop()
            ans+=poped[1]
            tmp_stack.append(poped)
        stack.append((p,w))
        p_cnt[m]-=1
        if not p_cnt[m]:m-=1
        ans+=w
        while tmp_stack:
            poped=tmp_stack.pop()
            ans+=poped[1]
            stack.append(poped)
    print(ans)        
        
        