import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

if __name__=="__main__":
    n=int(input())
    mat=[list(map(int,input().split())) for _ in range(n)]
    white_status=dict()
    dp=[[[0]*8 for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if mat[y][x]==1:
                dp[y][x]=[1]*8
            if mat[y][x]==2:
                white_status[(y,x)]=[0]*8
    ans=-1
    for d,dy,dx in zip(list(range(8)),[-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]):
        if d in [0,1]:
            for y in range(n): 
                for x in range(n-1,-1,-1):
                    if mat[y][x]==0:continue
                    ny,nx=y+dy,x+dx
                    if 0<=ny<n and 0<=nx<n:
                        if mat[y][x]==1:
                                dp[y][x][d]=max(dp[y][x][d],dp[ny][nx][d]+1)
                                ans=max(ans,dp[y][x][d])
                        elif mat[y][x]==2:
                            white_status[(y,x)][d]=max(white_status[(y,x)][d],dp[ny][nx][d]) 
        elif d in [2,3]:
            for y in range(n-1,-1,-1): 
                for x in range(n-1,-1,-1):
                    if mat[y][x]==0:continue
                    ny,nx=y+dy,x+dx
                    if 0<=ny<n and 0<=nx<n:
                        if mat[y][x]==1:
                                dp[y][x][d]=max(dp[y][x][d],dp[ny][nx][d]+1)
                                ans=max(ans,dp[y][x][d])
                        elif mat[y][x]==2:
                            white_status[(y,x)][d]=max(white_status[(y,x)][d],dp[ny][nx][d]) 
        elif d in [4,5]:
            for y in range(n-1,-1,-1): 
                for x in range(n):
                    if mat[y][x]==0:continue
                    ny,nx=y+dy,x+dx
                    if 0<=ny<n and 0<=nx<n:
                        if mat[y][x]==1:
                                dp[y][x][d]=max(dp[y][x][d],dp[ny][nx][d]+1)
                                ans=max(ans,dp[y][x][d])
                        elif mat[y][x]==2:
                            white_status[(y,x)][d]=max(white_status[(y,x)][d],dp[ny][nx][d]) 
        elif d in [6,7]:
            for y in range(n): 
                for x in range(n):
                    if mat[y][x]==0:continue
                    ny,nx=y+dy,x+dx
                    if 0<=ny<n and 0<=nx<n:
                        if mat[y][x]==1:
                                dp[y][x][d]=max(dp[y][x][d],dp[ny][nx][d]+1)
                                ans=max(ans,dp[y][x][d])
                        elif mat[y][x]==2:
                            white_status[(y,x)][d]=max(white_status[(y,x)][d],dp[ny][nx][d]) 


    for value in white_status.values():
        for i in range(4):ans=max(ans,value[i]+value[i+4]+1)
    print(ans)