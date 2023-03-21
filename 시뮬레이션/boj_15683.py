import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from copy import deepcopy
cameras_moves=[
    [],
    [[0],[1],[2],[3]],
    [(1,3),(0,2)],
    [(0,1),(1,2),(2,3),(3,0)],
    [(3,0,1),(0,1,2),(1,2,3),(2,3,0)],
    [(0,1,2,3)]]
dy,dx = [-1,0,1,0],[0,1,0,-1]
def calculate_safe_area(ch):
    cnt=0
    for y in range(n):
        for x in range(m):
            if ch[y][x]==0:cnt+=1
    return cnt

def go(level,ch):
    if level==len(cameras):
        calculate_safe_area(ch)
        return calculate_safe_area(ch)
    ret=1e9
    div,y,x=cameras[level]
    for moves in cameras_moves[div]:
        
        cp_ch=deepcopy(ch)
        for d in moves:
            sy,sx=y,x
            while True:
                ny,nx=sy+dy[d],sx+dx[d]
                if 0<=ny<n and 0<=nx<m and mat[ny][nx]<6:
                    cp_ch[ny][nx]=1
                    sy,sx=ny,nx
                else:break
        ret=min(ret,go(level+1,cp_ch))
    return ret
    

if __name__=="__main__":
    n,m=map(int,input().split())
    mat=[list(map(int,input().split())) for _ in range(n)]
    ch=[[0]*m for _ in range(n)]
    cameras=[]
    for y in range(n):
        for x in range(m):
            if not mat[y][x]:continue
            elif 1<=mat[y][x]<=5: cameras.append((mat[y][x],y,x))
            ch[y][x]=1
    print(go(0,ch))
    