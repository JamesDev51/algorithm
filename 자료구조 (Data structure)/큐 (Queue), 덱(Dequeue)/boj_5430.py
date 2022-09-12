import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

def solve():
    if '' in que: que.remove('')
    if len(que)<p.count("D"):return "error"
    d=True
    for c in p:
        if c=="R":
            d=False if d else True
        if c=="D":
            if d:que.popleft()
            else: que.pop()
    if not d: que.reverse()
    return f"[{','.join(que)}]"

if __name__=="__main__":
    for _ in range(int(input())):
        p=input().strip()
        p=p.replace("RR","")
        n=int(input())
        que=deque(input().strip().lstrip("[").rstrip("]").split(","))
        print(solve())