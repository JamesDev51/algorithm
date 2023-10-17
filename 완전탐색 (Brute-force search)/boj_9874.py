import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def dfs(cnt,idx):
    def loop_check(start_idx):
        x,y=coords[start_idx]
        visited=set()
        while True:
            if (x,y) in visited:return True #이미 방문한 곳이면 loop
            visited.add((x,y)) #방문 처리
            x,y=graph[(x,y)] #웜홀 통과 차례
            if (x,y) not in right_move:return False
            else:x,y=right_move[(x,y)]
            
    if cnt==n:
        for start_idx in range(n):
            if loop_check(start_idx):return 1 #하나라도 루프 있으면 1 반환
        return 0 #루프가 하나도 없으면 0
    
    ret=0
    for A in range(idx,n):  
        if visited[A]:continue
        visited[A]=1
        Ax,Ay=coords[A]
        for B in range(A+1,n):
            if visited[B]:continue
            visited[B]=1
            Bx,By=coords[B]
            graph[(Ax,Ay)]=(Bx,By) #웜홀 연결
            graph[(Bx,By)]=(Ax,Ay) #웜홀 연결
            ret+=dfs(cnt+2,A+1)
            visited[B]=0
        visited[A]=0
    return ret


n=int(input())
coords=[list(map(int,input().split())) for _ in range(n)]
coords.sort(key=lambda x:(x[1],x[0])) #y,x,순으로 오름차순 정렬

right_move=dict()#+x 했을 때 들어가는 홀
for i in range(n-1):
    x,y=coords[i]
    nx,ny=coords[i+1]
    if y==ny and x<nx:right_move[(x,y)]=(nx,ny) #y가 같으면 +x 했을 때 들어가짐

graph=dict()
visited=[0]*n
print(dfs(0,0))