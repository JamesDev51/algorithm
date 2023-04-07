import sys
sys.stdin=open("input.text","rt")
from collections import deque

LIMIT=4010

def go(tot_cnt):
    global mat
    res=0
    while tot_cnt>0:
        new_mat=dict()
        for row,col_mat in mat.items():
            for col, l in col_mat.items():
                d,k=l[0]
                n_row,n_col=row+dy[d],col+dx[d]
                
                if not 0<=n_row<=LIMIT or not 0<=n_col<=LIMIT: #범위를 벗어난 경우 (4010 *4010)
                    tot_cnt-=1;
                    continue

                if n_row in new_mat:
                    if n_col in new_mat[n_row]: #행,열 둘다 존재
                        new_mat[n_row][n_col].append((d,k));continue
                    else: #행만 존재
                        new_mat[n_row][n_col]=[(d,k)];continue
                else:
                    new_mat[n_row]=dict();new_mat[n_row][n_col]=[(d,k)];continue
        mat=dict() #초기화
        for row,col_mat in new_mat.items():
            for col,l in col_mat.items():
                if len(l)>1:
                    for _,k in l:res+=k;tot_cnt-=1
                else:
                    if row not in mat:mat[row]=dict()
                    mat[row][col]=l
    return res

dy,dx=[1,-1,0,0],[0,0,-1,1]
for t in range(1,int(input())+1):
    mat=dict()
    n=int(input())
    for _ in range(n):
        x,y,d,k=map(int,input().split())
        y=(y+1000)*2;x=(x+1000)*2
        if y not in mat:mat[y]=dict()
        mat[y][x]=[(d,k)]
    print(f"#{t} {go(n)}")