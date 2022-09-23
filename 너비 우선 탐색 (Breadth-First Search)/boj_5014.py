import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

def solve():
    que=deque()
    que.append(s)
    ch=[-1]*(f+1)
    ch[s]=0
    while que:
        stair=que.popleft()
        if stair+u<=f and ch[stair+u]==-1:
            ch[stair+u]=ch[stair]+1
            que.append(stair+u)
        if 1<=stair-d and ch[stair-d]==-1:
            ch[stair-d]=ch[stair]+1
            que.append(stair-d)
    return ch[g] if ch[g]!=-1 else "use the stairs"


    

if __name__=="__main__":
    f,s,g,u,d=map(int,input().split())
    print(solve())