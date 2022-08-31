import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve(u,d,l,r):
    if u==d and l==r: return ""
    if u+1==d and l+1==r: return f"{mat[u][l]}"
    flag=True
    for y in range(u,d):
        for x in range(l,r):
            if y==u and x==l:start=mat[y][x]
            else:
                if start!=mat[y][x]:flag=False
        if not flag: break
    else:
        return f"{start}"
    

    ret="("
    for sy in range(u,d,(d-u)//2):
        for sx in range(l,r,(r-l)//2):
            ret+=solve(sy,sy+(d-u)//2,sx,sx+(r-l)//2)
    ret+=")"
    return ret
if __name__=="__main__":
    n=int(input())
    mat=[list(map(int,input().strip())) for _ in range(n)]
    res=solve(0,n,0,n)
    print(res)
