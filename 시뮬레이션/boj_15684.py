import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
def sadari_game():
    for start_b in range(1,n+1):
        b=start_b
        a=0
        while a<=h:
            if ladder[a][b]:b+=1
            elif ladder[a][b-1]:b-=1
            a+=1
        if b!=start_b:return False
    return True

def dfs(depth,_a):
    global res
    if sadari_game():res=min(res,depth)
    if depth==3 or res<=depth:return
    for a in range(_a,h+1):
        for b in range(1,n):
            if not ladder[a][b] and not ladder[a][b+1]:
                ladder[a][b]=1
                dfs(depth+1,a)
                ladder[a][b]=0
                

if __name__=="__main__":
    n,m,h=map(int,input().split())
    ladder=[[0]*(11) for _ in range(31)]
    res=float('inf')
    for _ in range(m):
        a,b=map(int, input().split())
        ladder[a][b]=1
    dfs(0,1)
    print(res if res!=float('inf') else -1)