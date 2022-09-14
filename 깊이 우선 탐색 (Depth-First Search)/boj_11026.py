import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def normal():
    cnt=0
    ch=[[0]*n for _ in range(n)]
    stack=[]
    for y in range(n):
        for x in range(n):
            if not ch[y][x]:
                cnt+=1
                ch[y][x]=1
                stack.append((y,x))
                while stack:
                    yy,xx=stack.pop()
                    for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                        ny,nx=yy+dy,xx+dx
                        if 0<=ny<n and 0<=nx<n and mat[y][x]==mat[ny][nx] and not ch[ny][nx]:
                            ch[ny][nx]=1
                            stack.append((ny,nx))
    return cnt
            

def abnormal():
    cnt=0
    ch=[[0]*n for _ in range(n)]
    stack=[]
    for y in range(n):
        for x in range(n):
            if not ch[y][x]:
                cnt+=1
                ch[y][x]=1
                stack.append((y,x))
                while stack:
                    yy,xx=stack.pop()
                    for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                        ny,nx=yy+dy,xx+dx
                        if 0<=ny<n and 0<=nx<n and not ch[ny][nx]:
                            if (mat[y][x]=='R' or mat[y][x]=='G') and (mat[ny][nx]=='R' or mat[ny][nx]=='G'):
                                ch[ny][nx]=1
                                stack.append((ny,nx))
                            if mat[y][x]=='B' and mat[ny][nx]=='B':
                                ch[ny][nx]=1
                                stack.append((ny,nx))
    return cnt
            
            
def solve():
    print(normal())
    print(abnormal())

if __name__=="__main__":
    n=int(input())
    mat=[list(input().strip()) for _ in range(n)]
    solve()