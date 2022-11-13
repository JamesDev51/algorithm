import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline


if __name__=="__main__":
    n=int(input())
    tree=[[] for _ in range(n+1)]
    for _ in range(n-1):
        n1,n2=map(int,input().split())
        tree[n1].append(n2)
        tree[n2].append(n1)
    ch=[0]*(n+1); ch[1]=1
    que=deque(); que.append(1)
    while que:
        parents=que.popleft()
        for child in tree[parents]:
            if not ch[child]:
                ch[child]=parents
                que.append(child)
    for i in range(2,n+1):
        print(ch[i])
    