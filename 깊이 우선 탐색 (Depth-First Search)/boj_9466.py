import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(now):
    global cnt
    visited[now]=1
    next=select[now]
    if visited[next]:
        if not finished[next]:
            tmp=next
            while tmp!=now:tmp=select[tmp];cnt+=1
            cnt+=1
    else:dfs(next)
    finished[now]=1
            

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        select=list(map(int, input().split()))
        select.insert(0,0)
        
        visited=[0]*(n+1)
        finished=[0]*(n+1)
        cnt=0
        
        for now in range(1,n+1):
            if not visited[now]:
                dfs(now)
        print(n-cnt)