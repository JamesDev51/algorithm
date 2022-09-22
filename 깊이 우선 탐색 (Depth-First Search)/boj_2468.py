import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def dfs(limit):
    stack=[]
    ch=[[0]*n for _ in range(n)]
    cnt=0
    for y in range(n):
        for x in range(n):
            if mat[y][x]>limit and not ch[y][x]:
                stack.append((y,x))
                ch[y][x]=1
                cnt+=1
                while stack:
                    yy,xx=stack.pop()       
                    for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                        ny,nx=yy+dy,xx+dx
                        if 0<=ny<n and 0<=nx<n and not ch[ny][nx] and mat[ny][nx]>limit:
                            ch[ny][nx]=1
                            stack.append((ny,nx))
    return cnt


def solve():
    res=float('-inf')
    for height in range(1,101): res=max(res,dfs(height))
    return res

if __name__=="__main__":
    n=int(input())
    mat=[list(map(int,input().split())) for _ in range(n)]
    print(solve())