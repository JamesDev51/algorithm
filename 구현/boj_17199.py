import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n=int(input())
    graph=[[0]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):graph[i][i]=1
    for _ in range(n-1):
        a,b=map(int,input().split())
        graph[a][b]=1
    for mid in range(1,n+1):
        for start in range(1,n+1):
            for end in range(1,n+1):
                if graph[start][mid] and graph[mid][end]:
                    graph[start][end]=1
    for j in range(1,n+1):
        acc=0
        for i in range(1,n+1):
            acc+=graph[i][j]
        if acc==n:
            print(j)
            exit(0)
    print(-1)