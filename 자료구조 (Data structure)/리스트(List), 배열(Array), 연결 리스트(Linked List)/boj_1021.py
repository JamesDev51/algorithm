import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

def solve():
    que=deque(range(1,n+1))
    res=0
    
    for pos in poss:
        now_idx=que.index(pos)
        left,right=now_idx,len(que)-now_idx
        res+=min(left,right)
        if left<=right:
            for _ in range(left):que.append(que.popleft())
        else:
            for _ in range(right):que.appendleft(que.pop())
        que.popleft()
    return res

if __name__=="__main__":
    n,m=map(int,input().split())
    poss=list(map(int, input().split()))
    print(solve())