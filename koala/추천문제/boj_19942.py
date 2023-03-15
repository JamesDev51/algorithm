import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def go(l,p,f,s,v,c,idx_list):
    global cost,res
    if mp<=p and mf<=f and ms<=s and mv<=v and c<cost:
        cost=c
        res=idx_list
    if l==n+1:return
    now_p,now_f,now_s,now_v,now_c=ingredients[l]
    go(l+1,p+now_p,f+now_f,s+now_s,v+now_v, c+now_c, idx_list+[l])
    go(l+1,p,f,s,v,c,idx_list)
    

if __name__=="__main__":
    n=int(input())
    mp,mf,ms,mv=map(int,input().split())
    ingredients=[[]]+[list(map(int,input().split())) for _ in range(n)]
    cost=float('inf');res=[]
    go(1,0,0,0,0,0,[])
    print(cost if cost!=float('inf') else -1)
    print(*res)
    