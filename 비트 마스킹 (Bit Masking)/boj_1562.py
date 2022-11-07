import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve(last,pos,status):
    if dp[last][pos][status]!=0: return dp[last][pos][status]
    
    if status==(1<<10)-1 and pos==n: return 1
    
    if 0<=last-1<=9 and pos+1<=n: dp[last][pos][status]+=solve(last-1,pos+1,status | 1<<last-1)
    if 0<=last+1<=9 and pos+1<=n: dp[last][pos][status]+=solve(last+1,pos+1,status | 1<<last+1)
    dp[last][pos][status]%=mod
    return dp[last][pos][status]
    
if __name__=="__main__":
    n=int(input())

    res=0
    mod=1e9
    dp=[[[0]*(1<<10) for _ in range(101)] for _ in range(10)] #last, pos, status

    for st in range(1,10): res+=solve(st,1,1<<st)%mod

    print(int(res%mod))
    