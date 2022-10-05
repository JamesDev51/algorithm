import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def dfs(y,x,dist):
    global res, alphas
    ch[y][x]=1; used[mat[y][x]]=1
    res=max(res,dist)
    for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
        ny,nx=y+dy,x+dx
        if 0<=ny<r and 0<=nx<c and not ch[ny][nx] and not used[mat[ny][nx]]:
            dfs(ny,nx,dist+1)
    ch[y][x]=0; used[mat[y][x]]=0
    
if __name__=="__main__":
    r,c=map(int,input().split())
    mat=[list(map(lambda x: ord(x)-65,input().strip())) for _ in range(r)] 
    ch=[[0]*c for _ in range(r)]
    used=[0]*27
    res=1
    dfs(0,0,1)
    print(res)