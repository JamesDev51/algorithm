import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

def solve():
    now=0; loc=0; 
    while sum(ch)!=n: #다 운반할 때까지 진행
        flag=False
        wei=max_m
        if loc==0:
            for i in range(n):
                idx,d,m,r=info[i]
                if d==loc and r<=now and not ch[idx]:
                    if m<=wei:
                        res_s[idx]=now if res_s[idx]==0 else res_s[idx]; 
                        res_e[idx]=now+t
                        ch[idx]=1
                        info[i][2]-=m
                        wei-=m
                    else:
                        res_s[idx]=now
                        info[i][2]-=wei
                        wei=0
                    flag=True
            
                if wei==0:break
                    
        else:
            pass
        
        if flag:now+=t
        else: #둘다 준비 안된 경우
            pass
        
        
        
if __name__=="__main__":
    n,max_m,t=map(int,input().split())
    res_s=[0]*n; res_e=[0]*n
    ch=[0]*(n)
    info=[]
    for idx in range(n):
        d,m,r=map(int,input().split())
        info.append((idx,d,m,r))
    solve()
    # for i in range(n):print(res_s[i],res_e[i])