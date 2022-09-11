import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline


if __name__=="__main__":
    que=deque(range(1,int(input())+1))
    flag=True
    while len(que)>1:
        if flag:que.popleft();flag=False
        else:que.append(que.popleft());flag=True
    print(que[0])