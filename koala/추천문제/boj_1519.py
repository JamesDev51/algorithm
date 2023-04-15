import sys
sys.stdin = open("input.text",  "rt")
import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

def go(n):
    if n<10:return -1
    if dp[n]!=0:return dp[n]
    
    str_n=str(n)
    flag=False
    for size in range(len(str_n)-1,0,-1):
        for i in range(len(str_n)-size+1):
            start=int(str_n[i:i+size])
            if start==0:continue
            if go(n-start)==-1:
                dp[n]=1
                flag=True
                break
        if flag:break
    if not flag:dp[n]=-1
    return dp[n]    
    
if __name__=="__main__":
    n=int(input())
    dp=[0]*(n+1)
    go(n)
    if dp[-1]==-1:print(-1)
    else:
        res=float('inf')
        str_n=str(n)
        for size in range(len(str_n)-1,0,-1):
            for i in range(len(str_n)-size+1):
                start=int(str_n[i:i+size])
                if start==0:continue
                if go(n-start)==-1:
                    res=min(res,start)
        print(res)