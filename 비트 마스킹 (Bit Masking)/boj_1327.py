import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

#비트마스크로 다시 풀어보기

if __name__=="__main__":
    n,k=map(int, input().split())
    arr=list(input().strip().split())
    ans=''.join(list(map(str,range(1,n+1))))
    que=deque()
    que.append(("".join(arr),0))

    ch=set()
    ch.add("".join(arr))
    
    while que:
        a,cnt= que.popleft()
        if a==ans:print(cnt);exit(0)
        for i in range(n-k+1):
            mid=a[i:i+k]
            tmp=a[:i]+mid[::-1]+a[i+k:]
            if tmp not in ch:
                ch.add(tmp)
                que.append((tmp,cnt+1))
    print(-1)