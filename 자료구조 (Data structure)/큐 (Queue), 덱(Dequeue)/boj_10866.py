import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline


if __name__=="__main__":
    n=int(input())
    que=deque()
    for _ in range(n):
        com=input().strip()
        if com=="front":print(que[0] if que else -1)
        elif com=="back":print(que[-1] if que else -1)
        elif com=="size":print(len(que))
        elif com=="empty":print(1 if not que else 0)
        elif com=="pop_front":print(que.popleft() if que else -1)
        elif com=="pop_back":print(que.pop() if que else -1)
        else:
            if "front" in com:que.appendleft(com[11:])
            else:que.append(com[10:])