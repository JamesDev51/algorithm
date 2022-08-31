import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve(u,d,l,r):
    if u==d and l==r: return [0,0,0]
    if u+1==d and l+1==r: 
        if mat[u][l]==-1:return [0,0,1]
        elif mat[u][l]==0: return [1,0,0]
        else: return [0,1,0]
    res=[0,0,0]
    flag=True
    for y in range(u,d):
        for x in range(l,r):
            if y==u and x==l:start=mat[y][x]
            else: 
                if start!=mat[y][x]:flag=False
        if not flag:break
    else:
        if start==-1:res[2]+=1
        else:res[start]+=1
        return res
    
    for sy in range(u,d,(d-u)//3):
        for sx in range(l,r,(r-l)//3):
            ret=solve(sy,sy+(d-u)//3,sx,sx+(r-l)//3)
            res=[x+y for x,y in zip(res,ret)]
    return res

if __name__=="__main__":
    n=int(input())
    mat=[list(map(int,input().split())) for _ in range(n)]
    res=solve(0,n,0,n)
    print(res[2])
    print(res[0])
    print(res[1])

