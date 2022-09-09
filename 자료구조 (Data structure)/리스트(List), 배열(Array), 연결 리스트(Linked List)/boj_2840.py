import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

def solve():
    que=deque(["?"]*n)
    used=[]
    for cnt,letter in moves:
        for _ in range(int(cnt)):
            que.append(que.popleft())
        now=que.popleft()
        if now=="?":
            if letter not in used:used.append(letter); que.appendleft(letter)
            else: return "!"
        else:
            if now==letter: que.appendleft(letter)
            else: return "!"
    res=""
    res+=que.popleft()
    while que: res+=que.pop()
    return res
if __name__=="__main__":
    n,k=map(int,input().split())
    moves=[list(input().split()) for _ in range(k)]
    print(solve())
    