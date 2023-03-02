import sys
sys.stdin = open("input.text",  "rt")
import sys
import heapq
sys.setrecursionlimit(10000000)
input=sys.stdin.readline

def dijkstra():
    heap=[]
    heapq.heappush(heap,(mat[0][0],0,0))
    while heap:
        cost,y,x=heapq.heappop(heap)
        if ch[y][x]<cost:continue
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<n and 0<=nx<n and  cost+mat[ny][nx]<ch[ny][nx]:
                ch[ny][nx]=cost+mat[ny][nx]
                heapq.heappush(heap,(ch[ny][nx],ny,nx))
        
if __name__=="__main__":
    t=1
    while True:
        n=int(input())
        if not n:break
        mat=[list(map(int,input().split())) for _ in range(n)]
        ch=[[float('inf')]*n for _ in range(n)]
        ch[0][0]=mat[0][0]
        dijkstra()
        print(f"Problem {t}: {ch[n-1][n-1]}")
        t+=1
