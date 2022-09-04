import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

def solve():
    idx,move=que.popleft()
    if move>0:move-=1
    print(idx,end=" ")
    
    while que:
        if 0<move:
            move-=1
            que.append(que.popleft())
        elif move<0:
            move+=1
            que.appendleft(que.pop())
        else:
            idx,move=que.popleft()
            if move>0:move-=1
            print(idx,end=" ")

if __name__=="__main__":
    n=int(input())
    arr=map(int, input().split())
    que=deque()
    for i in range(1,n+1): que.append((i,next(arr)))
    solve()