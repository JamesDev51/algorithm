import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

import heapq
if __name__=="__main__":
    h,w=map(int,input().split())
    mat=[list(input().strip()) for _ in range(h)]
    heap=[]
    dist=[[float('inf')]*w for _ in range(h)]
    wall=[[0]*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if mat[y][x]=='#':continue
            for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                ny,nx=y+dy,x+dx
                if 0<=ny<h and 0<=nx<w and mat[ny][nx]=='#':
                    wall[y][x]=1
            if mat[y][x]=='S':
                dist[y][x]=0
                heapq.heappush(heap,(0,y,x))
            if mat[y][x]=='E':
                ey,ex=y,x
                

    while heap:
        cnt,y,x=heapq.heappop(heap)
        if dist[y][x]<cnt:continue
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<h and 0<=nx<w and mat[ny][nx]!='#':
                if wall[y][x] and wall[ny][nx]: #벽 이동 가능
                    if cnt<dist[ny][nx]:
                        dist[ny][nx]=cnt
                        heapq.heappush(heap,(cnt,ny,nx))
                else:
                    if cnt+1<dist[ny][nx]:
                        dist[ny][nx]=cnt+1
                        heapq.heappush(heap,(cnt+1,ny,nx))
    print(dist[ey][ex])