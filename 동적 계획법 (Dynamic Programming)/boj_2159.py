import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def get_distance(y1,x1,y2,x2):
    return abs(y1-y2)+abs(x1-x2)

def check_coords(y,x):
    return (1<=y<=100000) and (1<=x<=100000)

if __name__=="__main__":
    n=int(input())
    sy,sx=map(int,input().split())
    coords=[list(map(int,input().split())) for _ in range(n)]
    dp=dict()
    
    dp[0]=dict()
    y,x=coords[0]
    for dy,dx in zip([0,-1,0,1,0],[0,0,1,0,-1]):
        ny,nx=y+dy,x+dx
        if not check_coords(ny, nx):continue
        if ny not in dp[0]:dp[0][ny]=dict()
        if nx not in dp[0][ny]:dp[0][ny][nx]=get_distance(sy, sx, ny, nx)
    for i in range(1,n):
        y,x=coords[i]
        dp[i]=dict()
        for dy,dx in zip([0,-1,0,1,0],[0,0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if ny not in dp[i]: dp[i][ny]=dict()
            if nx not in dp[i][ny]:dp[i][ny][nx]=float('inf')
            if not check_coords(ny, nx):continue
            py,px=coords[i-1]
            for ddy,ddx in zip([0,-1,0,1,0],[0,0,1,0,-1]):
                nny,nnx=py+ddy,px+ddx
                if not check_coords(nny, nnx):continue
                dp[i][ny][nx]=min(dp[i][ny][nx], dp[i-1][nny][nnx]+get_distance(ny, nx, nny, nnx))
    ans=float('inf')
    for y,x_list in dp[n-1].items():
        for x in x_list:
            ans=min(ans,dp[n-1][y][x])
    print(ans)
            
                
                
        