import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

if __name__=="__main__":
    n,m=map(int,input().split())
    y,x,d=map(int,input().split())
    mat=[list(map(int,input().split())) for _ in range(n)]
    ch=[[0]*m for _ in range(n)]
    dy,dx=[-1,0,1,0],[0,1,0,-1]
    res=0
    while True:
        if not mat[y][x] and not ch[y][x]:ch[y][x]=1;res+=1
        flag=False
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if not mat[ny][nx] and not ch[ny][nx]:
                flag=True
        if not flag:
            back_d=(d+2)%4
            nby,nbx=y+dy[back_d],x+dx[back_d]
            if not mat[nby][nbx]:y,x=nby,nbx;continue
            else:break
        else:
            d=(d+3)%4
            nfy,nfx=y+dy[d],x+dx[d]
            if not mat[nfy][nfx] and not ch[nfy][nfx]:y,x=nfy,nfx
            continue
    print(res)