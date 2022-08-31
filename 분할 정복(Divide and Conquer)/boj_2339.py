import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def check(u,d,l,r,y,x,dir):
    if dir==0: #가로가 가능한지 체크
        for i in range(l,r):
            if mat[y][i]==2:return False
    else: #세로가 가능한지 체크
        for i in range(u,d):
            if mat[i][x]==2: return False
    return True
    

def solve(u,d,l,r,prev):
    ret=0
    flag=True; j_cnt=0
    for y in range(u,d):
        for x in range(l,r):
            if mat[y][x]==1: #불순물인 경우
                flag=False
                if prev==-1: #처음
                    if check(u,d,l,r,y,x,0):ret+=(solve(u,y,l,r,0)*solve(y+1,d,l,r,0)) #가로가 가능
                    if check(u,d,l,r,y,x,1):ret+=(solve(u,d,l,x,1)*solve(u,d,x+1,r,1)) #세로가 가능
                elif prev==0: #가로
                    if check(u,d,l,r,y,x,1): ret+=(solve(u,d,l,x,1)*solve(u,d,x+1,r,1)) #세로가 가능
                else:  #세로
                    if check(u,d,l,r,y,x,0): ret+=(solve(u,y,l,r,0)*solve(y+1,d,l,r,0)) #가로가 가능
            elif mat[y][x]==2: j_cnt+=1
    if flag and j_cnt==1: 
        return 1
    else: return ret
if __name__=="__main__":
    n=int(input())
    mat=[list(map(int,input().split())) for _ in range(n)]
    res=solve(0,n,0,n,-1)
    print(res if res!=0 else -1)