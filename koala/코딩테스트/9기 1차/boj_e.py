import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def dfs(y,x,cnt):
    global answer
    if y==0 and x==c-1 and cnt==k: answer+=1
    for dy, dx in zip([-1,0,1,0],[0,1,0,-1]):
        ny,nx=y+dy,x+dx
        if 0<=ny<r and 0<=nx<c and not ch[ny][nx] and mat[ny][nx]!='T':
            ch[ny][nx]=1
            dfs(ny,nx,cnt+1)
            ch[ny][nx]=0
            

if __name__=="__main__":
    r,c,k=map(int,input().split())
    mat=[list(input().strip()) for _ in range(r)]
    y,x=r-1,0
    answer=0
    ch=[[0]*c for _ in range(r)]; ch[y][x]=1;
    dfs(y,x,1)
    print(answer)