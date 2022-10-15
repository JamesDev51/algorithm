import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def dfs(y,x,l,p):
    global res
    if l==c:#모든 이동 완료
        res+=p
        return
    else:
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if 0<=ny<29 and 0<=nx<29 and not ch[ny][nx] and poss[i]!=0:
                ch[ny][nx]=1
                dfs(ny,nx,l+1,p*poss[i])
                ch[ny][nx]=0
                
if __name__=="__main__":
    c,e,w,s,n=map(int,input().split())
    poss=[n/100,e/100,s/100,w/100]
    ch=[[0]*29 for _ in range(29)]
    dy,dx=[-1,0,1,0],[0,1,0,-1]
    res=0
    ch[14][14]=1
    dfs(14,14,0,1)
    print("{: .10f}".format(res))