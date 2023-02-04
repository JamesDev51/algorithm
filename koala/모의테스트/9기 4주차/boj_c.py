import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def check(idx,cpu,priority):
    if idx==n: return 0 if cpu==m else float('-inf') 
    if dp[idx][cpu][priority]!=-1:return dp[idx][cpu][priority]
    
    new_cpu=min(cpu+tabs[idx][0],m) #m 이상 깎을 필요가 없음
    dp[idx][cpu][priority]=max(check(idx+1,cpu,priority),
                            check(idx+1,new_cpu, priority-tabs[idx][2]) + tabs[idx][1] if priority-tabs[idx][2]>=0 else float('-inf'))
    return dp[idx][cpu][priority]

if __name__=="__main__":
    n,m,k=map(int,input().split())
    tabs=[list(map(int,input().split())) for _ in range(n)]
    crom_total,cpu_total,prior_total=101,1001,501
    dp=[[[-1]*prior_total for _ in range(cpu_total)] for _ in range(crom_total)]
    answer=-1               
    for p in range(1,prior_total):
        ret=check(0,0,p)
        if ret>=k:
            answer=p
            break
    print(answer)