import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

def solve():
    cnt=1
    que=deque(range(1,n+1))
    res="<"
    while que:
        if cnt==k:res+=f"{que.popleft()}, ";cnt=1
        else:que.append(que.popleft());cnt+=1
    res=res[:-2]+">"
    return res

if __name__=="__main__":
    n,k=map(int, input().split())
    print(solve())