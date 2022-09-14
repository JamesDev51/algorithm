import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    stack=[]
    for y in range(m):
        for x in range(n):
            if not mat[y][x] and not ch[y][x]:
                size=1
                ch[y][x]=1
                stack.append((y,x))
                while stack:
                    yy,xx=stack.pop()    
                    for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                        ny,nx=yy+dy,xx+dx
                        if 0<=ny<m and 0<=nx<n and not mat[ny][nx] and not ch[ny][nx]:
                            ch[ny][nx]=1
                            size+=1
                            stack.append((ny,nx))
                res.append(size)
if __name__=="__main__":
    m,n,k=map(int,input().split())
    mat=[[0]*n for _ in range(m)]
    ch=[[0]*n for _ in range(m)]
    for _ in range(k):
        lbx,lby,rux,ruy=map(int,input().split())
        for y in range(lby,ruy):
            for x in range(lbx,rux):
                mat[y][x]=1

    res=[]
    solve()
    res.sort()
    print(len(res))
    print(*res)