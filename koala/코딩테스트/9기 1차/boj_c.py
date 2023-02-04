import sys
sys.stdin = open("input.text",  "rt")
import sys
from copy import deepcopy
input=sys.stdin.readline

def check():
    ret=float('-inf')
    acc_cnt=1
    for y in range(n):
        ret=max(ret,acc_cnt)
        acc_cnt=1;now=mat[y][0]
        for x in range(1,n):
            if now==mat[y][x]:acc_cnt+=1
            else: ret=max(ret,acc_cnt); now=mat[y][x];acc_cnt=1
    for x in range(n):
        ret=max(ret,acc_cnt)
        acc_cnt=1;now=mat[0][x]
        for y in range(1,n):
            if now==mat[y][x]:acc_cnt+=1
            else: ret=max(ret,acc_cnt); now=mat[y][x];acc_cnt=1
    return ret

if __name__=="__main__":
    n=int(input())
    mat=[list(input().strip()) for _ in range(n)]
    answer=float('-inf')
    for y in range(n):
        for x in range(n):
            for dy,dx in zip([0,1],[1,0]):
                ny,nx=y+dy,x+dx
                if 0<=ny<n and 0<=nx<n and mat[y][x]!=mat[ny][nx]:
                    mat[y][x],mat[ny][nx]=mat[ny][nx],mat[y][x]
                    answer=max(answer,check())
                    mat[ny][nx],mat[y][x]=mat[y][x],mat[ny][nx]
    print(answer)