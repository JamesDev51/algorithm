import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline


def solve():
    que=deque()
    ch=[-1]*(limit+1)
    ch[n]=0
    que.append(n)
    while que:
        loc=que.popleft()
        if loc==k: return ch[k] 
        if loc*2<=limit and ch[loc*2]==-1:
            ch[loc*2]=ch[loc]+1
            que.append(loc*2)
        if 0<=loc-1<=limit and ch[loc-1]==-1:
            ch[loc-1]=ch[loc]+1
            que.append(loc-1)
        if 0<=loc+1<=limit and ch[loc+1]==-1:
            ch[loc+1]=ch[loc]+1
            que.append(loc+1)
            


if __name__=="__main__":
    limit=100000
    n,k=map(int, input().split())
    print(solve())