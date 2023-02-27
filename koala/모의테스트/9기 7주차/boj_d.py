import sys
sys.stdin = open("input.text",  "rt")
import sys
sys.setrecursionlimit(10000000)
input=sys.stdin.readline
from copy import deepcopy

def check(s_idx,t_idx,used):
    if t_idx==len(t):return 1
    ret=0
    if s_idx<len(s) and s[s_idx]==t[t_idx]:
        ret=max(ret,check(s_idx+1,t_idx+1,used))
    if used==0 and ii==t[t_idx]:
        ret=max(ret,check(s_idx,t_idx+1,used+1))
    if used==1 and jj==t[t_idx]:
        ret=max(ret,check(s_idx,t_idx+1,used+1))
    return ret
    

if __name__=="__main__":
    n=int(input())
    s=list(input().strip())
    t=list(input().strip())
    i,j=map(int,input().split())
    jj=s.pop(j);ii=s.pop(i)
    print("YES" if check(0,0,0) else "NO")
