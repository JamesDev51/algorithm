import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from itertools import combinations

def check(idx,mixed):
    global answer,NR,NG,NB
    if mixed==8:return
    if mixed>=2: answer=min(answer,(abs(NR//mixed-R)+abs(NG//mixed-G)+abs(NB//mixed-B)))
    for n_idx in range(idx+1,n):
        NR,NG,NB=NR+rgbs[n_idx][0],NG+rgbs[n_idx][1],NB+rgbs[n_idx][2]
        check(n_idx,mixed+1)
        NR,NG,NB=NR-rgbs[n_idx][0],NG-rgbs[n_idx][1],NB-rgbs[n_idx][2]
        

if __name__=="__main__":
    n=int(input())
    rgbs=[list(map(int,input().split())) for _ in range(n)]
    R,G,B=map(int,input().split())
    answer=float('inf')
    NR,NG,NB=0,0,0
    check(-1,0)
    print(answer)