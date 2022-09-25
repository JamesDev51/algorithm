import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve(day,love):
    global res
    if day==k:
        res=max(res,love)
        return
    for i in range(n):
        for j in range(n):
            if i!=j and a[i]>0 and a[j]>0:
                a[i]-=1; a[j]-=1
                solve(day+1,love+r[day][i]+m[day][j])
                a[i]+=1; a[j]+=1
            if i==j and a[i]>1:
                a[i]-=1; a[j]-=1
                solve(day+1,love+r[day][i]+m[day][j])
                a[i]+=1; a[j]+=1
                
                
        
    

if __name__=="__main__":
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    r=[list(map(int,input().split())) for _ in range(k)]
    m=[list(map(int,input().split())) for _ in range(k)]
    res=float('-inf')
    solve(0,0)
    print(res)