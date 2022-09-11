import enum
import sys
sys.stdin = open("input.text",  "rt")
from collections import deque
import sys
input=sys.stdin.readline

def solve():
    cnt=0
    largest=max(que[i][1] for i in range(len(que)))
    while que:
        idx,val=que.popleft()
        if val==largest:
            cnt+=1
            if idx==m:return cnt
            largest=max(que[i][1] for i in range(len(que)))
        else:que.append((idx,val))
        

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().split())
        que=deque(enumerate(list(map(int,input().split())))) 
        print(solve())