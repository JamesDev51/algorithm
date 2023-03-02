import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
import heapq
from itertools import permutations

def init():
    for y in range(n):
        for x in range(n):
            if mat[y][x]==-1:budae=(y,x);mat[y][x]=0
            elif mat[y][x]==0:tals.append((y,x))    
    tals.insert(0,(budae))

def dijkstra(sy,sx):
    heap=[];heapq.heappush(heap,(0,sy,sx))
    costs=[[float('inf')]*n for _ in range(n)]; costs[sy][sx]=0
    while heap:
        cost,y,x=heapq.heappop(heap)
        if costs[y][x]<cost:continue
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<n and 0<=nx<n and cost+mat[ny][nx]<costs[ny][nx]:
                costs[ny][nx]=cost+mat[ny][nx]
                heapq.heappush(heap,(costs[ny][nx],ny,nx))
    return costs
                
def find_min_cost():
    if len(tals)==1:return 0
    ans=float('inf')
    costs=[[0]*len(tals) for _ in range(len(tals))]
    for i in range(len(tals)):
        sy,sx=tals[i]
        i_costs=dijkstra(sy,sx)
        for j in range(len(tals)):
            y,x=tals[j]
            costs[i][j]=i_costs[y][x]
    for perm in permutations(list(range(1,len(tals)))):
        now=0; acc_cost=0
        for talyung in perm:
            acc_cost+=costs[now][talyung]
            now=talyung
        acc_cost+=costs[now][0]
        ans=min(ans,acc_cost)
    return ans
            
        
n=int(input())
mat=[list(map(int,input().split())) for _ in range(n)]
tals=list()
init()
print(find_min_cost())