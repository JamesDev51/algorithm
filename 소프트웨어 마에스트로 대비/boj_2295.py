import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from itertools import combinations_with_replacement

if __name__=="__main__":
    n=int(input())
    u=list(int(input()) for _ in range(n))
    u.sort()
    for idx in range(n-1,-1,-1):
        dest=u[idx]
        for i in range(idx-1,-1,-1):
            for j in range(i,-1,-1):
                for k in range(j,-1,-1):
                    s=u[i]+u[j]+u[k]
                    if s==dest:print(s);exit(0)
                    if s>dest:continue
        
        