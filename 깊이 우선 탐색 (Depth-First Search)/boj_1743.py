import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    res=float('-inf')
    stack=[]
    for y in range(n):
        for x in range(m):
            if mat[y][x] and not ch[y][x]:
                size=1
                ch[y][x]=1
                stack.append((y,x))
                while stack:
                    yy,xx=stack.pop()
                    for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                        ny,nx=yy+dy,xx+dx
                        if 0<=ny<n and 0<=nx<m and mat[ny][nx] and not ch[ny][nx]:
                            ch[ny][nx]=1
                            size+=1
                            stack.append((ny,nx))
                res=max(res,size)
    return res     

if __name__=="__main__":
    n,m,k=map(int,input().split())
    mat=[[0]*m for _ in range(n)]
    ch=[[0]*m for _ in range(n)]
    for _ in range(k):
        r,c=map(int,input().split())
        mat[r-1][c-1]=1
    print(solve())