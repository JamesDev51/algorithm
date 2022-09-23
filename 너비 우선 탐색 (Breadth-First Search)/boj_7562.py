import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

def solve():
    que=deque()
    que.append((sy,sx))
    ch=[[-1]*l for _ in range(l+1)]
    ch[sy][sx]=0
    
    while que:
        y,x=que.popleft()
        for dy,dx in zip([-2,-1,1,2,2,1,-1,-2],[1,2,2,1,-1,-2,-2,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<l and 0<=nx<l and ch[ny][nx]==-1:
                ch[ny][nx]=ch[y][x]+1
                que.append((ny,nx))
    return ch[desy][desx]

if __name__=="__main__":
    for _ in range(int(input())):
        l=int(input())
        sy,sx=map(int,input().split())
        desy,desx=map(int,input().split())
        print(solve())