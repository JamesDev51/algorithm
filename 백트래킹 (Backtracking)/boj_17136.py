import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def check(sy,sx,size):
    for y in range(sy,sy+size):
        for x in range(sx,sx+size):
            if not mat[y][x]: return False
    return True

def attach(sy,sx,size):
    used[size]+=1
    for y in range(sy,sy+size):
        for x in range(sx,sx+size):
            mat[y][x]=0

def detach(sy,sx,size):
    used[size]-=1
    for y in range(sy,sy+size):
        for x in range(sx,sx+size):
            mat[y][x]=1
    
def dfs(y,x,cnt):
    global res
    if cnt>=res:return
    if y>=10:res=min(res,cnt);return
    if x>=10: dfs(y+1,0,cnt);return
    
    if mat[y][x]:
        for size in range(5,0,-1):
            if used[size]==5: continue
            if y+size>10 or x+size>10:continue
            if check(y,x,size):
                attach(y,x,size)
                dfs(y,x+size,cnt+1)
                detach(y,x,size)
    else:
        dfs(y,x+1,cnt)

if __name__=="__main__":
    mat=[list(map(int,input().split())) for _ in range(10)]
    res=float('inf')
    used=[0]*6
    dfs(0,0,0)
    print(res if res!=float('inf') else -1)